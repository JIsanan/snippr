from django_filters import rest_framework as filters
from django.db.models import Count
from rest_framework.viewsets import ViewSet, ModelViewSet, ReadOnlyModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.pagination import LimitOffsetPagination
from snippr.models.commit import Commit, Language, Snippet, Activity, Report
from snippr.models.tracking import Tracking
from snippr.serializers.user import UserSerializer
from snippr.serializers.commit import CommitSerializer, SnippetSerializer, LanguageSerializer, TrackingSerializer

import datetime


class CommitFilter(filters.FilterSet):
    language = filters.CharFilter(field_name='language__name')
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = Commit
        fields = ['language', 'title']


class CommitViews(ModelViewSet):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Commit.objects.all().annotate(num_of_upvotes=Count('upvote')).order_by('-num_of_upvotes', '-date_created')
    serializer_class = CommitSerializer
    filterset_class = CommitFilter
    pagination_class = LimitOffsetPagination

    def list(self, request):
        print(request.query_params)
        user = request.user.pk
        queryset = self.filter_queryset(self.get_queryset())
        open_count = queryset.filter(status='O').count()
        closed_count = queryset.filter(status='C').count()
        all_count = queryset.count()
        status_filter = request.query_params.get('status', None)
        if status_filter is not None:
            queryset = queryset.filter(status=status_filter)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(
                page, many=True, context={'request': user})
            return self.get_paginated_response(
                {'commits': serializer.data,
                 'open_count': open_count,
                 'closed_count': closed_count,
                 'all_count': all_count
                 })
        serializer = self.get_serializer(
            queryset, many=True, context={'request': user})
        return Response({'commits': serializer.data, 'something': 'something'})

    def create(self, request):
        language = Language.objects.filter(name=request.data['language']).first()
        retval = {}
        retval['message'] = 'something you inputted is wrong'
        if language and 'code' in request.data:
            obj = request.data.copy()
            obj['user'] = request.user.pk
            obj['language'] = language.pk
            data = CommitSerializer(data=obj)
            if data.is_valid() is True:
                commit = data.save()
                snippet = Snippet.objects.create(commit=commit, code=request.data['code'])  
                snippet = SnippetSerializer(snippet)
                retval = data.data
                retval['snippet'] = snippet.data
                retval['message'] = 'successfully created'
        return Response(retval)

    @action(detail=True, methods=['get'])
    def upvote(self, request, pk=None):
        user_obj = request.user
        commit = self.get_object()
        ret = {}
        ret['upvote_count'] = commit.upvote.filter(is_active=True).count()
        ret['upvote'] = True
        ret['downvote'] = False
        if(user_obj and commit):
            upvote = commit.upvote.filter(user=user_obj).first()
            if(upvote and not upvote.is_active):
                upvote.is_active = True
                upvote.save()
                ret['upvote_count'] += 1
            elif(not upvote):
                commit.upvote.create(
                    activity_type=Activity.UPVOTE, user=user_obj)
                ret['upvote_count'] += 1
        return Response(ret)

    @action(detail=True, methods=['get'])
    def downvote(self, request, pk=None):
        user_obj = request.user
        commit = self.get_object()
        ret = {}
        ret['upvote_count'] = commit.upvote.filter(is_active=True).count()
        ret['upvote'] = False
        ret['downvote'] = True
        if(user_obj and commit):
            upvote = commit.upvote.filter(user=user_obj).first()
            if(upvote and upvote.is_active):
                upvote.is_active = False
                upvote.save()
                ret['upvote_count'] -= 1
            elif(not upvote):
                commit.upvote.create(
                    activity_type=Activity.UPVOTE,
                    user=user_obj,
                    is_active=False)
                ret['upvote_count'] -= 1
        return Response(ret)

    @action(detail=True, methods=['post'])
    def comment(self, request, pk=None):
        user_obj = request.user
        commit = self.get_object()
        ret = {}
        if_exists = Tracking.objects.filter(user=request.user, commit=commit).first()
        if if_exists:
            if 'overwrite' not in request.data:
                ret['message'] = 'already has commit'
                return Response(ret)
            else:
                if_exists.delete()
        tracking_data = request.data.copy()
        tracking_data['user'] = request.user.pk
        tracking_data['snippet'] = commit.snippets.first().pk
        tracking_data['commit'] = commit.pk
        tracking = TrackingSerializer(data=tracking_data)
        if tracking.is_valid() is True and not hasattr(commit, 'resolved'):
            track = tracking.save()
            ret['message'] = "successfully commented"
            track = TrackingSerializer(track)
            ret['comment'] = track.data
        return Response(ret)

    @action(detail=True, methods=['post'])
    def edit_comment(self, request, pk=None):
        user_obj = request.user
        commit = self.get_object()
        ret = {}
        track = Tracking.objects.filter(user=request.user, commit=commit).first()
        ret['message'] = 'no comment yet'
        if track:
            track.latest_update = datetime.datetime.now()
            track.snippet = commit.snippets.first()
            track.code = request.data['code']
            track.description = request.data['description']
            track.save()
            ret['message'] = 'editing successful'
        return Response(ret)

    @action(detail=True, methods=['post'])
    def resolve(self, request, pk=None):
        user_obj = request.user
        commit = self.get_object()
        ret = {}
        if commit.user.pk != request.user.pk:
            ret['message'] = 'not your commit'
            return Response(ret)
        track = Tracking.objects.filter(pk=request.data['track_id']).first()
        ret['message'] = 'comment does not exist'
        if track:
            commit.status = 'C'
            commit.save()
            track.resolved = commit
            track.save()
            ret['message'] = 'resolved'
        return Response(ret)

    @action(detail=True, methods=['get'])
    def report(self, request, pk=None):
        commit = self.get_object()
        Report.objects.create(commit=commit,user=request.user)
        ret = {'message': 'successfully reported'}
        return Response(ret)


class LanguageViews(ReadOnlyModelViewSet):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class TrackingViews(ModelViewSet):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Tracking.objects.all()
    serializer_class = TrackingSerializer

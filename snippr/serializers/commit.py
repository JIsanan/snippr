from rest_framework import serializers
from rest_framework.authtoken.models import Token

from snippr.models.commit import Commit


class CommitSerializer(serializers.ModelSerializer):
	username = serializers.SerializerMethodField()

	class Meta:
		model = Commit
		fields = (
			'pk', 'user', 'username', 'language', 'code',)

	def get_username(self, obj):
		ret = obj.user.username
		return ret
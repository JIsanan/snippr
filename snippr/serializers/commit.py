from rest_framework import serializers
from rest_framework.authtoken.models import Token

from snippr.models.commit import Commit


class CommitSerializer(serializers.ModelSerializer):
	class Meta:
		model = Commit
		fields = (
			'pk', 'user', 'language', 'code',)

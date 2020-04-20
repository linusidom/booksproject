from rest_framework import serializers
from accounts.models import UserModel

class UserModelSerializer(serializers.ModelSerializer):
	class Meta():
		model = UserModel
from django.contrib.auth.models import User,Group
from rest_framework import serializers
from .models import Text2json

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username','email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class Text2jsonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text2json
        fields = ('id', 'title', 'i_LAIa', 'i_LAIb', 'msg_llm', )# 'fileds-name' must be in the model!
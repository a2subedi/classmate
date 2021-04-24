from rest_framework import serializers
from .models import Notice

class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = '__all__'

class FavNoticeSerializer(serializers.Serializer):
    user_id = serializers.CharField(max_length=20)
    notice_id = serializers.CharField(max_length=20)

    def create(self, validated_data):
        '''
        if user is not in list add user to list
        else remove user from list
        '''
        pass
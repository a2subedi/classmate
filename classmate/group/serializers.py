from django.http import JsonResponse
from rest_framework import serializers
from .models import Group, LinkUserGroup
from django.contrib.auth.models import User


class JoinGroupObj:
    def __init__(self, group_key, user_id):
        self.group_key = group_key
        self.user_id = user_id

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

# class GroupJoinSerializer(serializers.Serializer):
#     Group_key = serializers.CharField(max_length=20)
#     user_id = serializers.CharField(max_length=20)

#     def create(self,*args, **kwargs):
#         pass

    # def create(self, validated_data):
    #     print(validated_data.Group_key, validated_data['user_id'])
    #     groupKey = validated_data['Group_key']
    #     groups = Group.objects.all()
    #     group_keys = [group.key for group in groups]
    #     user = User.objects.get(id=validated_data['user_id'])

    #     if groupKey in group_keys:
    #         group = Group.objects.get(key=groupKey)
    #         inst = LinkUserGroup.objects.create(group=group, user=user)
    #         inst.save()
    #         # return JsonResponse({'status':'success','message':f'{user} is added to {group}'})
    #         print('user is joined')
    #         return JoinGroupObj(groupKey, validated_data['user_id'])
    #     else:
    #         # return JsonResponse({'status':'error', 'message':'The group do not exist'})
    #         print(validated_data)
    #     return JoinGroupObj(groupKey, validated_data['user_id'])
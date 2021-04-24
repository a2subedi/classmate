from rest_framework import generics,viewsets, status
from rest_framework.response import Response
from .models import Group

from .serializers import GroupSerializer

class GroupListView(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

# class GroupDetailView(generics.RetrieveAPIView):
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer

# class JoinGroup(generics.CreateAPIView):
#     serializer_class = GroupJoinSerializer

#     def create(self, request, *args, **kwargs):
#         response = super().create(request, *args, **kwargs)

#         if request.method == 'POST':
#             groupKey = form.cleaned_data['group_key']
#             groups = Group.objects.all()
#             group_keys = [group.key for group in groups]
#             if groupKey in group_keys:
#                 group = Group.objects.get(key=groupKey)
#                 inst = LinkUserGroup.objects.create(group=group, user=request.user) 
#                 inst.save()
#                 return Response({
#             'status': 200,
#             'message': 'Testimonials fetched',
#             'data': response.data
#         })
#             else:
#                 return  Response({
#             'status': 200,
#             'message': 'Testimonials fetched',
#             'data': response.data
#         })

        

# def join_group(request, group_key):
#     if request.method == 'POST':
#             groupKey = form.cleaned_data['group_key']
#             groups = Group.objects.all()
#             group_keys = [group.key for group in groups]
#             if groupKey in group_keys:
#                 group = Group.objects.get(key=groupKey)
#                 inst = LinkUserGroup.objects.create(group=group, user=request.user) 
#                 inst.save()
#                 serializer = GroupJoinSerializer()
#                 return Response(serializer.data)
#             else:
#                 return Response(status=status.HTTP_404_NOT_FOUND)
    
    
# def join_group(request):
#     # if request.method == 'POST':
#     #         groupKey = form.cleaned_data['group_key']
#     #         groups = Group.objects.all()
#     #         group_keys = [group.key for group in groups]
#     #         if groupKey in group_keys:
#     #             group = Group.objects.get(key=groupKey)
#     #             inst = LinkUserGroup.objects.create(group=group, user=request.user)
#     #             inst.save()
#     #             return redirect('/')
#     #         else:
#     #             print('groupKey do not match with any availabel key')
#     # else:
#     #     form = UserGroupForm()
#     # return render(request, 'group/enroll-group.html', {'form': form})

#     print(request.body)


def join_group(request):
    print(request.body)
    if request.method == 'POST':
        # groupKey = request.body['group_key']
        # find the group key here
        groups = Group.objects.all()
        group_keys = [group.key for group in groups]
        if groupKey in group_keys:
            group = Group.objects.get(key=groupKey)
            inst = LinkUserGroup.objects.create(group=group, user=request.user) 
            inst.save()
            return Response({
        'status': 200,
        'message': 'Testimonials fetched',
        'data': response.data
    })
        else:
            return  Response({
        'status': 200,
        'message': 'Testimonials fetched',
        'data': response.data
    })
    return None
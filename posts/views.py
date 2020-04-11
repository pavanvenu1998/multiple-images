from django.shortcuts import render, get_object_or_404

from .models import Post, PostImage
from rest_framework.response import Response

def blog_view(request):
    posts = Post.objects.all()
    return render(request, 'blog.html', {'posts':posts})

def detail_view(request, id):
    post = get_object_or_404(Post, id=id)
    photos = PostImage.objects.filter(post=post)
    return render(request, 'detail.html', {
        'post':post,
        'photos':photos
    })

# if request.method == 'POST':
    def post(self,request,*args,**kwargs):
        # images = dict(six.iterlists(request.POST))
        images = dict(request.data.lists())['image']
        flag = 1
        arr = []
        for image  in images:
            # modified_data = modify_input_for_multiple_files(vehicle_name,images)
            # file_serializer = ImageSerializer(data=modified_data)
            if file_serializer.is_valid():
                file_serializer.save()
                arr.append(file_serializer.data)
            else:
                flag = 0
        if flag == 1:
            return Response(arr)
        #     return Response({"status": "true",},status=status.HTTP_201_CREATED)
        # return Response({"status": "false","message":file_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
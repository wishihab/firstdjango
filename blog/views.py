from django.shortcuts import render
from blog.models import Post
# Create your views here.
# Create Retrieve Update Delete

# List all the post

def post_list_view(request):
    # post_title = Post_objects.all()
    post_objects = Post.objects.all()
    content = {
        # 'post_title': post_title,
        'post_objects': post_objects
    }
    return render(request, "posts/index.html", content)
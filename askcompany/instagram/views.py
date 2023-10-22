from .models import Post
from django.shortcuts import render

def post_list(request):
    qs=Post.objects.all()
    q=request.GET.get('q','')
    if q:
        qs=qs.filter(message__icontains=q)
        # instagram/templates/instagram/post_list.html
    return render(request,'instagram/post_list.html',{
        'post_list':qs,
        'q':q
    })
from .models import Post
from django.shortcuts import render

def post_list(request):
    # 전체 가져올 준다
    qs=Post.objects.all()
    # 검색어추가
    q=request.GET.get('q','')
    # 검색어가 있다면 
    if q:
        # 메세지에 포함된것
        qs=qs.filter(message__icontains=q)
     # instagram/templates/instagram/post_list.html
     # render(view함수의 request,원하는 Html,{참조할 이름:객체}) 
    return render(request,'instagram/post_list.html',{
        'post_list':qs,
        'q':q
    })
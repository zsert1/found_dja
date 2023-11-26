from django.http import HttpRequest, HttpResponse, Http404
from .models import Post
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
# 클래스 기반 뷰 코드가 간결
post_list = ListView.as_view(model=Post)
#  함수 기반 view 확장성및 커스텀 기능 용이
# def post_list(request):
#     # 전체 가져올 준다
#     qs = Post.objects.all()
#     # 검색어추가
#     q = request.GET.get('q', '')
#     # 검색어가 있다면
#     if q:
#         # 메세지에 포함된것
#         qs = qs.filter(message__icontains=q)
#      # instagram/templates/instagram/post_list.html
#      # render(view함수의 request,원하는 Html,{참조할 이름:객체})
#     return render(request, 'instagram/post_list.html', {
#         'post_list': qs,
#         'q': q
#     })


# def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
#     post = get_object_or_404(pk=pk)

#     # try:
#     #     post = Post.objects.get(pk=pk)
#     # except Post.DoesNotExist:
#     #     raise Http404
#     return render(request, 'instagram/post_detail.html', {'post': post})
#  클래스 vieww
post_detail = DetailView.as_view(model=Post)


def archives_year(request, year):
    return HttpResponse(f"{year}년 archives")

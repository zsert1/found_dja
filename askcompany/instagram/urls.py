
from django.urls import path, include, re_path, register_converter
from .import views


class YearConverter:
    regex = r"20\d{2}"

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return str(value)


register_converter(YearConverter, "year")
app_name = "instagram"  # URL Reverse에서 nameSpace역할을 하게된다
urlpatterns = [
    path("", views.post_list),
    path('<int:pk>/', views.post_detail),
    path('archives/<year:year>/', views.archives_year),
    # re_path(r'archives/(?P<year>20\d{2})/', views.archives_year)

]

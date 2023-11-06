# found_dja

장고 기본

- conda activate askcompany
- python manage.py runserver
- python manage.py <앱 이름>
- 앱만든후 urls.py생성
- 프로젝트 settings의 INSTALLED_APPS에 추가한 앱이름 추가
- project의 url에 앱 url추가  
  `path('blog/',include('blog.urls')),`

# 미디어 파일 등록 방법

- pip install pillow 설치
- 프로젝트 settings에 설정  
   `MEDIA_URL='/media/'
MEDIA_ROOT=os.path.join(BASE_DIR,'media')`
- 이미지 파일을 사용할 앱의 모델에 설정

# 개발 순서

- djang api 개발 순서
- 앱 model.py에 사용할 모델 정의
- view.py에서 queryset 설정 후 호출될 api에 따른 반환값 적용
- urls에 주소에 따른 호출될 views 설정

## List view

- 모델명 소문자\_list 이름의 QuerySet을 템플릿에 전달
- **페이징처리 지원**

## 정렬 지정하기

- 정렬을 원하는 앱의 모델의 클래스에  
  `class Meta:
        ordering = ['-id']` 추가 예제는 id 역순

## django-debug-toolbar

- 현재 request/response에 대한 다양한 디버깅 정보제공
- https://django-debug-toolbar.readthedocs.io/en/latest/installation.html  
  따라 적용

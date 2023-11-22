# found_dja

장고 기본

- conda activate <프로젝트 이름>
- python manage.py runserver
- python manage.py <앱 이름>
- 앱만든후 urls.py생성
- 프로젝트 settings의 INSTALLED_APPS에 추가한 앱이름 추가
- project의 url에 앱 url추가  
  `path('blog/',include('blog.urls')),`

# 슈퍼계정 만들기

- pyhon manage.py createsuperuser

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
- 모델 변경 후  
   `python manage.py makemigrations 앱이름`  
   `python manage.py sqlmigrate 앱이름 마이그레이션 파일이름`

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
  - 웹페이지에 템플릿에 <body> 태그가 있어야 동작

## 특정앱에 유저모델 생성

- 해당 프로젝트의 settings `AUTH_USER_MODEL = 'auth.User` 추가

## 1:N의 모델의 값 가져오기

- 같은 데이터를 가져온다
  `Comment.objects.filter(post_id=4)`  
  `Comment.objects.filter(post__id=4)`
  `Comment.objects.filter(post=post)`  
  `post.comment_set.all()`
  - 위에서 reverse_name는 **comment_set** 이다
- reverse_name충돌이 발생한다면?
  - 어느 한쪽의 reverse_name 포기
  - 어느 한쪽 또는 FK의 reverse_name변경
    - ex)FK(User,..., related_name="reverse_name")

# 1:1 관계정의

- OneToOneField 필드사용

# Many to Many Field

- M:N 관계에서 어느쪽이라도 필드 지정가능
  `class Tag(models.Model):
name = models.CharField(max_length=50, unique=True)
post_set = models.ManyToManyField(Post)`
- RDBMS지만 , DB에 따라 NoSql기능도 지원

### Migrations

- 모델의 변경 내역을 “데이터 베이스 스키마”로 반영시키는 효율적인 방법을 제공 관련 명령어
- 마이그레이션 파일생성

```
python manage,py makemigrations <앱이름>
```

- 지정 데이터 베이스 마이그레이션 적용

```
python manage,py migrate <앱이름>
```

- 마이그레이션 적용 현황 출력

```
python manage,py showmigrations <앱이름>
```

- 지정 마이그레이션의 SQL출력 내역

```
python manage,py sqlmigrate <앱이름> <마이그레이션-이름>
```

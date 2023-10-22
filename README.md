# found_dja

장고 기본

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

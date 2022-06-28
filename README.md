# djangoWeb 

장고 기반 crud 게시판 구현
### 기능
* Post crud
* User crud
* Reply 
* post_like
* social login by kakao
* email authentication
* image upload

### 사용기술

* Allauth 기반 소셜 로그인 1 kakao 2 naver
* 배포 : AWS EC2 - 윈도우서버
* DB : AWS s3

### 설치 환경
* python 3.10
* pip install django
* pip install django-allauth
- pip install Pillow
- pip install boto3
- pip install django-storages
- pip freeze > requirements.txt
- pip install -r requirements.txt

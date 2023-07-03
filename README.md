# PROmet 웹사이트

django를 사용하여 만든 간단한 취업 포털/커뮤니티 웹사이트

## 시작하기

python 및 pip가 설치되어 있는지 확인하십시오. 고유한 dockerfile을 만들어 애플리케이션을 고정 표시하거나 로컬 서버에서 실행하여 애플리케이션을 테스트할 수 있습니다.

### 설치 및 실행

다음을 사용하여 프로젝트에 필요한 종속성을 설치합니다.

```python
pip install -r requirements.txt
```

로컬에서 프로젝트를 실행하려면

```python
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## 전개

EC2 인스턴스에 django 애플리케이션을 배포하는 방법에 대한 자세한 블로그가 있습니다. 아래 링크를 따르십시오.

[EC2에서 Django 웹사이트 호스팅](https://dev.to/waji97/hosting-a-django-website-on-ec2-part-1-4758)

또한 Docker 컨테이너에 앱을 배포하기 위한 파일 `Dockerfile`과 `nginx.conf`파일을 포함했습니다.

## 사용한 기술

* [Django](https://docs.djangoproject.com/en/4.2/) 
* [HTML](https://devdocs.io/html/) 
* [CSS](https://devdocs.io/css/) 
* [JS](https://devdocs.io/javascript/) 
* [Bootstrap](https://getbootstrap.com/docs/5.0/getting-started/introduction/)

## 협력 인원

* **이종욱** - *Project Manager* - [jongouk](https://github.com/jongouk)
* **이예나** - *Front End* - [yena](https://github.com/yena)
* **김건태** - *Front End* - [kimgeontae1](https://github.com/kimgeontae1)
* **송찬호** - *Back End* - [sch8536](https://github.com/sch8536)


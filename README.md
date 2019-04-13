# blogdemo
### 部署环境
* centos 7
* Python 3.6
* Django 2.1
* uwsgi  2.0
* nginx  1.14

### 项目环境
    pip install -Ur requirements.txt

修改python3.6/site-packages/django_markdown/urls.py为

    from django.urls import path
    from .views import preview
    
    urlpatterns =[
        path('preview/', preview, name='django_markdown_preview'),
    ]

### 迁移

    python manage.py makemigrations
    python manage.py migrate
    
### 创建超级用户

    python manage.py createsuperuser

### 收集静态文件

    python manage.py collectstatic
    
### 重建搜索索引

    python manage.py rebuild_index

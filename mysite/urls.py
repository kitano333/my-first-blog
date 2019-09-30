"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#includeを追加。
#ここで、include関数を使いたいのでfrom django.urls…の行を変更しそのインポートを追加する必要があります。

urlpatterns = [
    path('admin/', admin.site.urls),
#admin/ で始まる全てのURLについて、Djangoが返すべきビューをこの行で指定しています。
    path('', include('blog.urls')),
]
#これでDjangoは'http://127.0.0.1:8000/' に来たリクエストは blog.urls へリダイレクトするようになり、それ以降はそちらを参照するようになります。

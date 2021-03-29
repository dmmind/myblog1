"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
import sys
print(sys.path)
# sys.path.append('D:/web_djo/myblog')
# sys.path.append(os.path.join(os.path.dirname(__file__), '../blog'))

from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
# 导入静态文件模块
from django.conf import settings
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('list-<int:lid>.html', views.list, name='list'),   # 整形参数lid
    path('show-<int:sid>.html', views.show, name='tags'),   # 整形参数sid
    path('tag/<tag>', views.tag, name='tags'),
    path('s/', views.search, name='search'),
    path('about', views.about, name='about'),
    path('ueditor/', include('DjangoUeditor.urls')),  # 添加DjangoUeditor的url
    re_path('^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})
]

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

#import socialaccount.views

import board.views

import reply.views

import user.views
from config import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', board.views.mainPage),

    path('board/create', board.views.create),
    path('board/list', board.views.list),
    path('board/read/<int:bid>', board.views.read),
    path('board/delete/<int:bid>', board.views.delete),
    path('board/update/<int:bid>', board.views.update),
    path('user/myProfile', user.views.myProfile),


    path('reply/create/<int:bid>', reply.views.create),
    path('reply/list', reply.views.list),
    path('reply/read/<int:rid>', reply.views.read),
    path('reply/delete/<int:bid>/<int:rid>', reply.views.delete),
    path('reply/update/<int:bid>/<int:rid>', reply.views.update),
    path('user/signup', user.views.signup),
    path('user/login', user.views.login),
    path('user/logout', user.views.logout),
    path('user/delete', user.views.userDelete),
    path('user/delete', user.views.userDelete),
    path('like/<int:bid>',board.views.like),


    #path('kakao', socialaccount.views.kakaoLoginPage),
    path('accounts/', include('allauth.urls')),


    #path('accounts/profile', accounts.views.profile),
] + static(settings.MEDIA_URL)
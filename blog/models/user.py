from datetime import datetime

from django.db import models

from utils.base_model import SoftDeleteModel


class User(SoftDeleteModel):
    email = models.EmailField(verbose_name='유저 이메일', unique=True)
    password = models.CharField(verbose_name='유저 비밀번호', max_length=30)
    nickname = models.CharField(verbose_name='유저 닉네임', unique=True, max_length=20)
    recent_login = models.DateTimeField(verbose_name='최근 접속일자', default=datetime.now())

    class Meta:
        db_table = 'user'
        verbose_name = '블로그 가입 유저'

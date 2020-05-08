from datetime import datetime

from django.db import models

from utils.abstract_models import SoftDeleteModel


class User(SoftDeleteModel):
    email = models.EmailField(verbose_name='유저 이메일', unique=True)
    password = models.CharField(verbose_name='유저 비밀번호', max_length=30)
    nickname = models.CharField(verbose_name='유저 닉네임', unique=True, max_length=20)
    recent_login = models.DateTimeField(verbose_name='최근 접속일자', default=datetime.now())

    class Meta:
        db_table = 'user'
        verbose_name = '블로그 가입 유저'
        ordering = ['id']


class Board(SoftDeleteModel):
    title = models.CharField(verbose_name='게시판 이름', max_length=300, null=False, blank=False)
    desc = models.CharField(verbose_name='게시판 상세설명', max_length=300, default='', null=False, blank=True)

    class Meta:
        db_table = 'board'
        verbose_name = '게시판'


class Post(SoftDeleteModel):
    user_id = models.BigIntegerField()
    board_id = models.BigIntegerField()
    title = models.CharField(verbose_name='게시글 제목', max_length=300)
    body = models.TextField(verbose_name='게시글 본문')
    view_count = models.BigIntegerField(verbose_name='조회수', default=0)
    ip = models.CharField(verbose_name='작성자 ip', max_length=15, default='0.0.0.0')
    modify_password = models.CharField(verbose_name='게시물 수정 비밀번호', max_length=20)

    class Meta:
        db_table = 'post'
        verbose_name = '게시글'


class GuestBook(SoftDeleteModel):
    user_id = models.BigIntegerField(verbose_name='작성자 id')
    body = models.TextField(verbose_name='방명록 본문')

    class Meta:
        db_table = 'guestbook'
        verbose_name = '방명록'

# from django.contrib.auth.base_user import AbstractBaseUser
# from django.contrib.auth.models import PermissionsMixin
from django.db import models

from utils.abstract_models import SoftDeleteModel


# class User(AbstractBaseUser, PermissionsMixin, SoftDeleteModel):
class User(SoftDeleteModel):
    email = models.EmailField(verbose_name='유저 이메일', unique=True)
    password = models.CharField(verbose_name='유저 비밀번호', max_length=128)
    nickname = models.CharField(verbose_name='유저 닉네임', unique=True, max_length=20)
    last_login = models.DateTimeField(verbose_name='최근 접속일자', blank=True, null=True)

    # USERNAME_FIELD = 'nickname'
    # REQUIRED_FIELDS = ['email', 'password']

    class Meta:
        # swappable = 'AUTH_USER_MODEL'
        db_table = 'user'
        verbose_name = '블로그 가입 유저'
        ordering = ['id']

    def __str__(self):
        return self.nickname


class Board(SoftDeleteModel):
    title = models.CharField(verbose_name='게시판 이름', max_length=300, null=False, blank=False)
    desc = models.CharField(verbose_name='게시판 상세설명', max_length=300, default='', null=False, blank=True)

    class Meta:
        db_table = 'board'
        verbose_name = '게시판'
        ordering = ['id']

    def __str__(self):
        return self.title


class Post(SoftDeleteModel):
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='writer_set', verbose_name='글쓴이')
    board = models.ForeignKey(to=Board, on_delete=models.CASCADE, related_name='board_set', verbose_name='게시판 종류')
    title = models.CharField(verbose_name='게시글 제목', max_length=300)
    body = models.TextField(verbose_name='게시글 본문')
    view_count = models.BigIntegerField(verbose_name='조회수', default=0)
    ip = models.CharField(verbose_name='작성자 ip', max_length=15, default='0.0.0.0')
    modify_password = models.CharField(verbose_name='게시물 수정 비밀번호', max_length=20)

    class Meta:
        db_table = 'post'
        verbose_name = '게시글'
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class GuestBook(SoftDeleteModel):
    visitor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='visitor_set', verbose_name='방문자')
    body = models.TextField(verbose_name='방명록 본문')

    class Meta:
        db_table = 'guestbook'
        verbose_name = '방명록'
        ordering = ['-created_at']

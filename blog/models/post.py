from django.db import models

from utils.base_model import SoftDeleteModel


class Post(SoftDeleteModel):
    user_id = models.BigIntegerField()
    board_id = models.BigIntegerField()
    title = models.CharField(verbose_name='게시글 제목', max_length=300)
    body = models.TextField(verbose_name='게시글 본문')
    view_count = models.BigIntegerField(verbose_name='조회수', default=0)
    ip = models.CharField(verbose_name='작성자 ip', default='0.0.0.0')
    modify_password = models.CharField(verbose_name='게시물 수정 비밀번호', max_length=20)

    class Meta:
        db_table = 'post'
        verbose_name = '게시글'

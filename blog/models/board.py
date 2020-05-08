from django.db import models

from utils.base_model import SoftDeleteModel


class Board(SoftDeleteModel):
    title = models.CharField(verbose_name='게시판 이름', max_length=300, null=False, blank=False)
    desc = models.CharField(verbose_name='게시판 상세설명', max_length=300, default='', null=False, blank=True)

    class Meta:
        db_table = 'board'
        verbose_name = '게시판'

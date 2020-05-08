from django.db import models

from utils.base_model import SoftDeleteModel


class GuestBook(SoftDeleteModel):
    user_id = models.BigIntegerField(verbose_name='작성자 id')
    body = models.TextField(verbose_name='방명록 본문')

    class Meta:
        db_table = 'guestbook'
        verbose_name = '방명록'

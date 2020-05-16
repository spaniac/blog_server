from datetime import datetime

from django.db import models


class BaseModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(null=False, blank=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, blank=False, auto_now=True)

    class Meta:
        abstract = True


class SoftDeleteModel(BaseModel):
    is_deleted = models.BooleanField(default=False, null=False, blank=False)
    deleted_at = models.DateTimeField(default=None, null=True, blank=False)

    class Meta:
        abstract = True

    # def soft_delete(self):
    #     self.is_deleted = True
    #     self.deleted_at = datetime.now()
    #     self.save()

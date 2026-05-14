from django.db import models

class SoftDeleteQuerySet(models.QuerySet):
    def not_deleted(self):
        return self.filter(is_deleted=False)

    def deleted(self):
        return self.filter(is_deleted=True)
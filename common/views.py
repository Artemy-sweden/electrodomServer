from django.db import models


class DBMixin(models.Model):
    using = 'default'  # По умолчанию, используем default базу данных

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        using_db = getattr(self, 'using', self.using)
        super().save(using=using_db, *args, **kwargs)

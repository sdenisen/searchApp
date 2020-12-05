from django.db import models


# Create your models here.

class Details(models.Model):
    id = models.AutoField(verbose_name="#", auto_created=True, primary_key=True, serialize=False)
    asv_id = models.IntegerField(verbose_name="ASV ключ", blank=True, null=True)
    full_name = models.TextField(verbose_name="Наименование")

    class Meta:
        managed = False
        db_table = 'details'
        app_label = 'equipment_parts'

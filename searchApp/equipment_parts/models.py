from django.db import models


# Create your models here.

class Details(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    asv_id = models.IntegerField(blank=True, null=True)
    full_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'details'
        app_label = 'equipment_parts'

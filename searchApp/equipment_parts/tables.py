import django_tables2 as tables
from .models import Details


class DetailsTable(tables.Table):
    class Meta:
        model = Details
        template_name = "bootstrap4_table.html"

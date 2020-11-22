import django_tables2 as tables
from .models import Details


class DetailsTable(tables.Table):
    class Meta:
        model = Details
        # add class="paleblue" to <table> tag
        attrs = {'class': 'paleblue'}
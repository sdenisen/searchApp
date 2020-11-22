from django.db.models.functions import Lower
from django.shortcuts import render

# Create your views here.
from equipment_parts.models import Details


def filter(request):
    return render(request, "master_page.html")


def view_search_results(request):
    _text = request.GET["items"]
    print(_text)
    list_of_search_query = _text.split(" ")
    # Details.objects.annotate(full_name_lower=Lower("full_name")).filter(full_name_lower__contains="Подшипник".lower()).values().all()[:5]
    print(list_of_search_query)
    i_details = Details.objects.annotate(full_name_lower=Lower("full_name"))
    for a in list_of_search_query:
        i_details = i_details.filter(full_name_lower__contains=a)

    table_data = i_details.values("asv_id", "full_name")
    print (i_details.query)

    return render(request, "master_page.html", {"table_data": table_data})

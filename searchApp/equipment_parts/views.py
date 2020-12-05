from django.db.models.functions import Lower
from django.shortcuts import render
from .models import Details
from .tables import DetailsTable


def filter(request):
    table_view = DetailsTable(Details.objects.all())
    table_view.paginate(page=request.GET.get("page", 1), per_page=25)
    return render(request, "master_page.html", {"table_view": table_view})


def view_search_results(request):
    init_text = request.GET["filter"]
    list_of_search_query = init_text.strip().lower().split(" ")
    i_details = Details.objects.annotate(full_name_lower=Lower("full_name"))
    for a in list_of_search_query:
        i_details = i_details.filter(full_name_lower__contains=a)

    table_data = i_details.values("asv_id", "full_name")

    table_view = DetailsTable(table_data)
    table_view.paginate(page=request.GET.get("page", 1), per_page=25)
    return render(request, "master_page.html", {"table_view": table_view,
                                                "search_field": init_text})


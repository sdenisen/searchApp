from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView

from equipment_parts.models import Details
from equipment_parts.api.serializers import DetailSerializer


class DetailsListView(ListAPIView):
    queryset = Details.objects.all()
    serializer_class = DetailSerializer


class DetailsDetailView(RetrieveAPIView):
    queryset = Details.objects.all()
    serializer_class = DetailSerializer


class DetailsDestroyView(DestroyAPIView):
    queryset = Details.objects.all()
    serializer_class = DetailSerializer



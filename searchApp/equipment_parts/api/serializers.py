from rest_framework import serializers

from equipment_parts.models import Details


class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Details
        fields = ('id', 'asv_id', 'full_name')

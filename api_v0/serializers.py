from rest_framework import serializers
from being.models import Being


class BeingListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Being
        fields = [
            'id',
            'name',
            'state',
            'url',
        ]
        read_only_fields = [
            'state',
        ]


class BeingDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Being
        fields = [
            'id',
            'name',
            'state',
            'url',
        ]
        read_only_fields = [
            'name',
        ]
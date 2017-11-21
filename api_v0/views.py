# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from being.models import Being
from feed_events.models import BeingsEvent, BeingsListEvent
from api_v0.serializers import BeingListSerializer, BeingDetailSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.shortcuts import get_object_or_404


class BeingList(ListCreateAPIView):
    queryset = Being.objects.all()
    serializer_class = BeingListSerializer

    def post(self, request, *args, **kwargs):
        bel = BeingsListEvent(event='POST')
        bel.save()
        return self.create(request, *args, **kwargs)


class BeingDetail(RetrieveUpdateDestroyAPIView):
    queryset = Being.objects.all()
    serializer_class = BeingDetailSerializer

    def delete(self, request, *args, **kwargs):
        bel = BeingsListEvent(event='DELETE')
        bel.save()
        return self.destroy(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        bel = BeingsListEvent(event='PATCH')
        bel.save()
        being = get_object_or_404(Being, pk=kwargs['pk'])
        prev_state = being.state
        be = BeingsEvent(being=being, prev_state=prev_state)
        be.save()
        return self.update(request, *args, **kwargs)
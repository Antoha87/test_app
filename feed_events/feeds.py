from django.contrib.syndication.views import Feed
from django_push.publisher.feeds import Feed as Push
from django.conf import settings
from being.models import Being
from feed_events.models import BeingsListEvent, BeingsEvent
from django.core.urlresolvers import reverse


class Rss(Feed):
    title = 'RSS'
    link = '/channels/rss/'
    description = 'RSS chanel'

    def items(self):
        return Being.objects.all()


class Atom(Push):
    title = 'Atom'
    link = '/channels/atom/'
    subtitle = 'Atom chanel'

    def items(self):
        return Being.objects.all()


class AtomList(Push):
    title = 'Atom beings list'
    link = "/channels/atom/list-display/"
    subtitle = 'Atom chanel'

    def items(self):
        return BeingsListEvent.objects.all().order_by('-id')

    def item_title(self, item):
        return item.get_event()

    def item_description(self, item):
        return 'Event is  -%s' % item.get_event()


class AtomDetail(Push):
    title = 'Atom being detail'
    link = "/channels/atom/detail/"
    subtitle = 'Atom chanel'

    def get_object(self, request, slug):
        return Being.objects.get(slug=slug.lower())

    def items(self, obj):
        return BeingsEvent.objects.filter(being=obj)

    def item_title(self, item):
        return 'PATCH change state to -%s' % item.being.state

    def item_description(self, item):
        return 'Prev state is -%s' % item.prev_state





from django import template
from django.core.cache import cache
from analytics.models import Analytic


register = template.Library()

def retrieve_analytics(reference=None):
    analytics = cache.get('analytics')
    if not analytics:
        queryset = Analytic.objects.first()
        cache.set('analytics', queryset, 3600)
    return analytics


@register.inclusion_tag('analytics/google_analytics.html')
def google_analytics():
    return {'analytics': retrieve_analytics()}

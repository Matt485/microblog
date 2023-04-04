from django.core import signing
from django.core.exceptions import SuspiciousOperation
from django.http import HttpResponse
from django.urls import reverse

MAX_AGE_SECONDS = 60


def generate_temp_url(data=None):
    # signing.dumps() returns a "URL-safe, signed base64 compressed JSON string"
    # with a timestamp
    return reverse('temp', args=[signing.dumps(data)])


def index(request):
    return HttpResponse(f'<a href="{generate_temp_url()}">temporary link</a>')

def temp(request, signed_data):
    try:
        # load data and check expiration
        data = signing.loads(signed_data, max_age=MAX_AGE_SECONDS)
    except signing.BadSignature:
        # triggers an HttpResponseBadRequest (status 400) when DEBUG is False
        raise SuspiciousOperation('invalid signature')
    # success
    return HttpResponse(f'Here\'s your data: {data}')

# Create your views here.

from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from models import Temperature, Probe

def record(request, temperature, probeid):
    if request.method not in ['POST', 'PUT']:
        raise PermissionDenied
    probe = Probe.objects.get(pk=probeid)
    temp = Temperature( probe=probe, temperature=temperature)
    temp.save()
    return HttpResponse("Temperature %s recorded by probe %s (id %s)" %
(temperature, probe.location, temp.id ), content_type="text/plain")

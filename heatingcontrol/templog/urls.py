from django.conf.urls import patterns, include

urlpatterns = patterns('',
    ('^record/(?P<probeid>\d+)/(?P<temperature>[\d.]+)$', 'templog.views.record'),
)

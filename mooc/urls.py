from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^', include('mooc.core.urls',namespace='core')),
    url(r'^cursos/', include('mooc.courses.urls',namespace='courses')),
    url(r'^admin/', include(admin.site.urls)),
)

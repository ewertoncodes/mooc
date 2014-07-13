from django.conf.urls import patterns, include, url


urlpatterns = patterns('mooc.courses.views',
	url(r'^$', 'index', name='index'),
 
)  
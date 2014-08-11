from django.conf.urls import patterns,url

from Flick import views

urlpatterns = patterns('', 
	url(r'^$', views.index, name='index'),
	url(r'^card/(?P<cardName>[A-Za-z0-9]+)/$', views.card, name='card'),
	url(r'^cards/$', views.cards, name='cards'),
	url(r'^cards/new/$', views.newcard, name='newcard'),
	url(r'^patterns/$', views.patterns, name='patterns'),
	url(r'^patterns/new/$', views.newpattern, name='newpattern'),
    
	)

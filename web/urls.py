from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

import web.views
handler404 = 'web.views.page_not_found'	# this works if we are the ROOT_URLCONF

urlpatterns = patterns('',
	# web
	(r'^$', web.views.index),
	(r'^news/$', web.views.news),	# TODO: add news/blog feed
	(r'^download/$', web.views.download),
	(r'^documentation/$', web.views.documentation),
	(r'^wisdom/$', web.views.wisdom),
	(r'^about/$', web.views.about),

)


from django.conf.urls.defaults import *
# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

import web.urls
import web.views
handler404 = 'web.views.page_not_found'	# this works if we are the ROOT_URLCONF

urlpatterns = patterns('',

	(r'^$', include(web.urls)),

	# Uncomment the admin/doc line below to enable admin documentation:
	#(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	# Uncomment the next line to enable the admin:
	#(r'^admin/', include(admin.site.urls)),

)


from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse
from django.views.generic import RedirectView
from django.views.decorators.csrf import csrf_exempt
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import debug_toolbar

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'auth.views.home', name='home'),
    url(r'^$', RedirectView.as_view(permanent=False, url='/mm/member_list')),
    url(r'^zinc/member_list$', RedirectView.as_view(permanent=False, url='/mm/member_list')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^rfid/', include('rfid.urls')),
    url(r'^zinc/', include('zoho_integration.urls')),
    #url(r'^pp/', include('paypal_integration.urls')),
    url(r'^mm/', include('member_management.urls')),
    url(r'^memberpoints/', include('memberpoint.urls')),
    url(r'^ckeditor/', include('ckeditor.urls')),
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^audit/', include('audit.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()


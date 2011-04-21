# Copyright 2011 HubSpot, Inc.
#
#   Licensed under the Apache License, Version 2.0 (the 
# "License"); you may not use this file except in compliance 
# with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, 
# software distributed under the License is distributed on an 
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, 
# either express or implied.  See the License for the specific 
# language governing permissions and limitations under the 
# License.

from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

import marketplacetest.views as views

urlpatterns = patterns(
    '',
    ('^marketplacetest/$', direct_to_template, { 'template' : 'home.html' }),
    ('^marketplacetest/home$',   direct_to_template, { 'template' : 'home.html' }),
    ('^marketplacetest/other$',  direct_to_template, { 'template' : 'other.html'}),
    ('^marketplacetest/images$', direct_to_template, { 'template' : 'images.html'}),
    ('^marketplacetest/remote_css$', direct_to_template, { 'template' : 'remote_css.html'}),
    ('^marketplacetest/remote_js$', direct_to_template, { 'template' : 'remote_js.html'}),
    ('^marketplacetest/ajax$', direct_to_template, { 'template' : 'ajax.html'}),
    ('^marketplacetest/params_get$', views.params_get),
    ('^marketplacetest/form$', views.form),
    ('^marketplacetest/form_plus_redir$', views.form_plus_redir),
    ('^marketplacetest/redir_dest$', direct_to_template, { 'template' : 'redir_dest.html'}), 
    ('^marketplacetest/verify_signed_request$', views.verify_signed_request),
                      
    # Example:
    # (r'^marketplacetest/', include('marketplacetest.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)

from django.conf.urls import patterns, include, url
from BET.views import hello
from BET.views import current_datetime
from django.contrib import admin
#from haystack.views import SearchView
from BET.forms import *
# Without threading...

# urlpatterns = patterns('haystack.views',
#     url(r'^search/$', SearchView(
#         template='search/search.html',
#         form_class=PinsRangeSearchForm,
#     ), name='search'),
# )

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'estimation_tool.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^time/$', current_datetime),
    url(r'^hello/$', hello),
    #url(r'^search/$', include('haystack.urls')),
    url(r'^showdetail/(?P<part_number>[\d-]+)/$', 'BET.views.show_detail', name='showdetail'),
    url(r'^showdetail/(?P<part_number>[\d-]+)/showsimilar/$', 'BET.views.show_similar', name='showthesimilar'),
    url(r'^showdetail/(?P<part_num>[\d-]+)/formula/$', 'BET.views.show_est_formula', name='showformula'),
    url(r'^accounts/login/$',  'BET.views.login', name='login'),
    url(r'^index/$',  'BET.views.index', name='index'),
    url(r'^search/$',  'BET.views.index2', name='search'),
    url(r'^advancedsearch/$',  'BET.views.AdvancedSearch', name='advancedsearch'),
)
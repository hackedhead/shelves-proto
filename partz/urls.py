from django.conf.urls import patterns, include, url

from partz.views import ProjectDetailView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'shelves.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^(?P<slug>[-_\w]+)/$', ProjectDetailView.as_view(), name='project-detail'),

)

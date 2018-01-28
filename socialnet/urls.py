from django.conf.urls import include, url

from socialnet.views.user import landing, about_me, resume, links
from socialnet.views.project import projects, project
from socialnet.views.post import posts, post
from socialnet.views.photo import photos

urlpatterns = [
    url(r'^$',          landing,     name='views.user.landing'),
    url(r'^about_me/$',  about_me,    name='views.user.about_me'),
    url(r'^resume/$',    resume,      name='views.user.resume'),
    url(r'^links/$',     links,       name='views.user.links'),

    url(r'^projects/$', projects, name='views.project.projects'),
    url(r'^project/(?P<id>\d+)$', project, name='views.project.project'),

    url(r'^posts/$', posts, name='views.post.posts'),
    url(r'^post/(?P<id>\d+)/$', post, name='views.post.post'),
    
    url(r'^photos$', photos, name='views.photo.photos'),
]

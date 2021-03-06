from django.conf.urls import patterns, include, url
from django.contrib import admin
from blogapp.api import PostResource
from blogapp.api import CommentResource

post_resource = PostResource()
comment_resource = CommentResource()

urlpatterns = patterns('',
    url(r'^blogapp/', include('blogapp.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/', include(post_resource.urls)),
    url(r'^api/v1/', include(comment_resource.urls)),
)

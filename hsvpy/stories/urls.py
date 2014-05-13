from django.conf.urls import patterns, include, url

import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name="stories"),
    url(r'^story/(?P<story_id>[0-9]+)/$', views.show_story, name="show-story"),
    url(r'^add-story/$', views.add_story, name="add-story"),
    url(r'^edit-story/(?P<story_id>[0-9]+)/$', views.edit_story, name="edit-story"),
    url(r'^add-paragraph/(?P<story_id>[0-9]+)/$', views.edit_paragraph, name="add-paragraph"),
    url(r'^edit-paragraph/(?P<story_id>[0-9]+)/(?P<para_id>[0-9]+)/$', views.edit_paragraph,
        name="edit-paragraph"),
)


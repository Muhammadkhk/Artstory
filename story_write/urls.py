from django.urls import path

from .views import (edit_story_privat, edit_story_public, story_detail_privat, storyListview,
story_detail,write_comment,storyListviewprivate, write_story)

urlpatterns = [
    path('write', write_story, name='write'),
    path('public', storyListview.as_view(),name='public'),
    path('private/<storyId>', story_detail_privat, name='story_detail_private'),
    path('private/editpage/<storyId>', edit_story_privat, name='editstory_detail_private'),
    path('public/<storyId>', story_detail, name='story_detail'),
    path('public/editpage/<storyId>', edit_story_public, name='editstory_detail_public'),
    path('write_comment', write_comment, name='write_comment'),
    path('private', storyListviewprivate.as_view(),name='private'),
]
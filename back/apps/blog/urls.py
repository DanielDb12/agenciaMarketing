from django.urls import path

from .views import *



urlpatterns = [
    path('list',BlogListView.as_view()),
    path('by_category',ListPostsByCategory().as_view()),
    path('detail/<slug>',BlogDetailView.as_view()),
    path('search',BlogSearch.as_view()),
]

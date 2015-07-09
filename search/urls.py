from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.search_index, name='search_index'),
    url(r'query/', views.exec_search, name="Search")
]

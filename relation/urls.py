from django.urls import path
from . import views

urlpatterns=[
    path('home',views.relation_home,name='home'),
    path('page1',views.relation_page1,name='page1'),
    path('page2',views.relation_page2,name='page2'),
    path('page3',views.relation_page3,name='page3'),

]
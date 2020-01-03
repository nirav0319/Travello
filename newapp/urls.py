
from django.urls import path
from newapp import views
urlpatterns = [
    path('',views.index,name='index'),
    path('about.html/',views.about,name='about'),
    path('contact.html/',views.contact,name='contact'),
    path('destinations.html/',views.destinations,name='destinations'),
    path('elemets.html/',views.elements,name='elements'),
    path('news.html/',views.news,name='news'),
    path('index.html',views.index,name='index')

]

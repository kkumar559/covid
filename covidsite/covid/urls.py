from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('about/',views.about,name='about'),
    path('faq1/',views.faq1,name='faq1'),
    path('faq2/',views.faq2,name='faq2'),
    path('faq3/',views.faq3,name='faq3'),
    path('faq4/',views.faq4,name='faq4'),

]
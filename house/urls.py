from unicodedata import name
from django.urls import path

from house import views

urlpatterns =[
    path('all-plots/', views.view_all_plots, name='all-plots'),
    path('view-plot/<int:id>', views.view_plot, name='view-plot'),
]
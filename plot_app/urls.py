from django.urls import path
from.import views
from .views import plot_data


urlpatterns =   [
     path('',views.plot_data,name='plot_data'),
     path('display_Images/',views.display_Images,name='display_Images'),
     path('generatepdf', views.generate_pdf, name='generate_pdf'),
     path('load-districts', views.load_districts, name='load_districts'),
     path('delete-all-states/', views.delete_all_states, name='delete_all_states'),
   
]


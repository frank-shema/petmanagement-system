from django.urls import path
from . import views
from .views import (
    estateListingView,
    addEstateView,
    deleteEstateView,
    estateDetailView,
    updateEstateView,
    EstatesListView
)

urlpatterns = [
    path('estates/', estateListingView, name="estate_listings"),  
    path('v1/estates/create/', addEstateView, name='add_estate'),
    path('v1/estates/update/<int:pk>/', updateEstateView, name='update_estate'),
    path('v1/estates/delete/<int:pk>/', deleteEstateView, name='delete_estate'),
    path('v1/estates/details/<int:pk>/', estateDetailView, name='estate_detail'),
    path('get-chart-data/', views.get_chart_data, name='get_chart_data'),
    path('estates/all',EstatesListView.as_view(),name="estates_list")
]

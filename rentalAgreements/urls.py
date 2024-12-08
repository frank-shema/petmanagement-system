from django.urls import path
from .views import create_rental_agreement, rental_agreement_list, update_rental_agreement \
    , update_rental_agreement_status, rental_agreement_detail, delete_rental_agreement,RentalAgreementListView

app_name = 'pet_agreements'

urlpatterns = [
     path('list/', rental_agreement_list, name='rental_agreement_list'),
    path('create/<int:estate_id>/', create_rental_agreement, name='create_rental_agreement'),
    path('update/<int:agreement_id>/', update_rental_agreement, name='update_rental_agreement'),
    path('update-status/<int:agreement_id>/', update_rental_agreement_status, name='update_rental_agreement_status'),
    path('detail/<int:agreement_id>/', rental_agreement_detail, name='rental_agreement_detail'),
    path('delete/<int:agreement_id>/', delete_rental_agreement, name='delete_rental_agreement'),
    path('all/',RentalAgreementListView.as_view(),name="all_agreements"),
]

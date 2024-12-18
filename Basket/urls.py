from django.urls import path
from . import views

urlpatterns = [
    path('basket_list/', views.BasketListView.as_view(), name='BasketList'),
    path('basket_list/<int:id>/', views.BasketDetailView.as_view(), name='basket_detail'),
    path('basket_list/<int:id>/update/', views.CreateBasketView.as_view(), name='update_basket'),
    path('basket_list/<int:id>/delete/', views.DeleteBasketView.as_view(), name='delete_basket'),
    path('create_basket/', views.CreateBasketView.as_view(), name='CreateBasket'),
    path('list_of_orders/', views.ListOfOrdersView.as_view(), name='List_of_orders'),
]
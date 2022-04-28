from django.urls import path


from .views import (
    remove_from_cart,
    reduce_quantity_item,
    add_to_cart,
    ProductListView,
    ProductDetailView,
    # PlantaStoreHomeView,
    OrderSummaryView,
    CheckoutView,
    PaymentView
)

app_name ="store"

urlpatterns = [
    # path('', PlantaStoreHomeView.as_view(), name='home-view'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('product/<pk>', ProductDetailView.as_view(), name="product-detail"),
    path('add-to-cart/<pk>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<pk>/', remove_from_cart, name='remove-from-cart'),
    path('order-summary', OrderSummaryView.as_view(), name='order-summary'),
    path('reduce-quantity-item/<pk>/', reduce_quantity_item, name='reduce-quantity-item'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment')
]


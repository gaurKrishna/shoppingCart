from django.conf.urls import url
from . import views

app_name = 'home'

urlpatterns = [
    # shoppingcart/addproduct/
    url(r'^addproduct/$', views.ProductCreate.as_view(), name='product_create'),
    # shoppingcart/
    url(r'^$', views.HomepageView.as_view(), name='homepage'),
    # shoppingcart/search/
    url(r'^search/$', views.SearchView, name='search'),
    # shoppingcart/filter/
    url(r'^filter/$', views.filter, name='filter'),
    # shoppingcart/register/
    url(r'^register/$', views.UserRegistration.as_view(), name='registration'),
    # shoppingcart/login/
    url(r'^login/$', views.UserLogin.as_view(), name='login'),
    # shoppingcart/logout/
    url(r'^logout/$', views.UserLogout, name='logout'),
    # shoppingcart/details/prosuct_id/
    url(r'^details/(?P<pk>[0-9]+)/$', views.ProductDetails.as_view(), name = 'product_details'),
    # shoppingcart/addtocart/
    url(r'^addtocart/$', views.AddToCart, name='add_to_cart'),
    # shoppingcart/mycart/
    url(r'^mycart/$', views.CartView, name='Cart_details'),
    # shoppingcart/mycart/delete/cart.id/
    url(r'^mycart/delete/(?P<pk>[0-9]+)/$', views.RemoveFromCart.as_view(), name='remove_from_cart'),
]
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'

urlpatterns = [
    path('login', views.login_user, name='login'),
    path('logout', views.logout_request, name='logout'),

    path(
        'get_dealer_reviews/<int:dealer_id>',
        views.get_dealer_reviews,
        name='get_dealer_reviews'
    ),

    path('get_car_makes', views.get_car_makes, name='get_car_makes'),

    path(
        'get_car_models/<int:make_id>',
        views.get_car_models,
        name='get_car_models'
    ),

    path('add_review', views.add_review, name='add_review'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
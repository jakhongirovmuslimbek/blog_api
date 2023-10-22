from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('posts.urls')),

    #new
    path('api-auth/', include('rest_framework.urls')),                                  #for login/logout

    # authentication
    path('api/dj-rest-auth/', include('dj_rest_auth.urls')),                            #api/dj-rest-auth/login and api/dj-rest-auth/logout
    path('api/dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),

    # authentication - registration
    path('api/allauth/', include('allauth.urls')),

    #documents
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/redoc', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('api/schema/swagger', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger'),
]

"""
admin/
api/ post
api/ post/detail/<int:pk>
api/ users
api/ users/<int:pk>
api-auth/
api/dj-rest-auth/
api/dj-rest-auth/registration/
api/allauth/ signup/ [name='account_signup']
api/allauth/ login/ [name='account_login']
api/allauth/ logout/ [name='account_logout']
api/allauth/ reauthenticate/ [name='account_reauthenticate']
api/allauth/ password/change/ [name='account_change_password']
api/allauth/ password/set/ [name='account_set_password']
api/allauth/ inactive/ [name='account_inactive']
api/allauth/ email/ [name='account_email']
api/allauth/ confirm-email/ [name='account_email_verification_sent']
api/allauth/ ^confirm-email/(?P<key>[-:\w]+)/$ [name='account_confirm_email']
api/allauth/ password/reset/ [name='account_reset_password']
api/allauth/ password/reset/done/ [name='account_reset_password_done']
api/allauth/ ^password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$ [name='account_reset_password_from_key']
api/allauth/ password/reset/key/done/ [name='account_reset_password_from_key_done']

api/schema/ [name='schema']
api/schema/redoc [name='redoc']
api/schema/swagger [name='swagger']
"""

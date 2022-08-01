from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('CRUD.urls')),
    path('rest_crud/', include('rest_crud.urls')),
    path('login_rfw/', include('rest_login.urls')),
    # path('img/', include('imageupload.urls')),
    path('app1/', include('app1.urls')),
    # path('app2/',include('restimage.urls')),
    path('ses/', include('sessionlogin.urls')),
    path('cur', include('currency_app.urls')),
    path("accounts/", include("django.contrib.auth.urls")),  # new
    path('image', include('imagefolder.urls')),
    path('oto/', include('oto.urls')),
    path('otm/', include('onetomany.urls')),
    # path('salt', include('salt.urls')),
    path('lvl', include('sessionlvl.urls')),
    path('mtm', include('manytomany.urls')),
    # path('oauth', include('oauth.urls')),
    #path('oauthlogin', include('oauthlogin.urls')),
    # path('api',include('oauthsession.urls')),
    path('con', include('country_currency.urls')),
    path('val', include('password_validate.urls')),
    path('age', include('agetoyear.urls')),
    path('app', include('testapp.urls')),
    path('age2', include('dob_to_age.urls')),
    path('diff',include('days_cal.urls')),
    path('rest2',include('restlogin.urls')),
    path('bar',include('barcode_generator.urls')),
    path('dec',include('Decimalapp.urls')),
    path('qr',include('QRcodeapp.urls')),
    path('timezone',include('timezoneapp.urls')),
    path('reset',include('resetapp.urls')),
    path('bmi',include('BMIapp.urls')),
    path('log',include('logginapp.urls'))

]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('admin/', admin.site.urls),
    path('user/', include('api.users.urls')),
    path('banks/', include('api.banks.urls')),
    path('accounts/', include('api.accounts.urls')),
    path('transactions/', include('api.transactions.urls')),

]

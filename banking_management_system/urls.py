from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('admin/', admin.site.urls),
    path('user/', include('apis.users.urls')),
    path('banks/', include('apis.banks.urls')),
    path('accounts/', include('apis.accounts.urls')),
    path('transactions/', include('apis.transactions.urls')),

]

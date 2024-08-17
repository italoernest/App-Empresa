from django.contrib import admin
from django.urls import path, include

from business.views import BusinessListView, BusinessCreateView, BusinessUpdateView, BusinessDeleteView
from suppliers.views import SuppliersListView, SuppliersCreateView, SuppliersUpdateView, SuppliersDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("allauth.urls")),

    #Rotas da Business
    path("business/list", BusinessListView.as_view(), name="business_list"),
    path("business/create", BusinessCreateView.as_view(), name="business_create"),
    path("business/update/<int:pk>", BusinessUpdateView.as_view(), name="business_update"),
    path("business/delete/<int:pk>", BusinessDeleteView.as_view(), name="business_delete"),

    #Rotas da Suppliers
    path("suppliers/list", SuppliersListView.as_view(), name="suppliers_list"),
    path("suppliers/create",  SuppliersCreateView.as_view(), name="suppliers_create"),
    path("suppliers/update/<int:pk>",  SuppliersUpdateView.as_view(), name="suppliers_update"),
    path("suppliers/delete/<int:pk>",  SuppliersDeleteView.as_view(), name="suppliers_delete"),

    
]

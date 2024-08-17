from django.contrib import admin
from django.urls import path, include

from business.views import BusinessListView, BusinessCreateView, BusinessUpdateView, BusinessDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("allauth.urls")),

    #Rotas da Business
    path("business/list", BusinessListView.as_view(), name="business_list"),
    path("business/create", BusinessCreateView.as_view(), name="business_create"),
    path("business/update/<int:pk>", BusinessUpdateView.as_view(), name="business_update"),
    path("business/delete/<int:pk>", BusinessDeleteView.as_view(), name="business_delete"),
]

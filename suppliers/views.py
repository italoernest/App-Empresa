from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Suppliers

class SuppliersListView(ListView):
        model = Suppliers

class SuppliersCreateView(CreateView):
        model = Suppliers
        fields = ["nome_empresa", "cnpj", "inscricao_estadual", "telefone", "whatsapp", "logradouro", "numero", "complemento", "bairro", "cidade", "estado", "cep", "observacao"]
        success_url = reverse_lazy("suppliers_list")

class SuppliersUpdateView(UpdateView):
    model = Suppliers
    fields = ["nome_empresa", "cnpj", "inscricao_estadual", "telefone", "whatsapp", "logradouro", "numero", "complemento", "bairro", "cidade", "estado", "cep", "observacao"]
    success_url = reverse_lazy("suppliers_list")
        
class SuppliersDeleteView(DeleteView):
       model = Suppliers
       success_url = reverse_lazy("suppliers_list")
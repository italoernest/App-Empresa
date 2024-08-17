from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Business

class BusinessListView(ListView):
        model = Business

class BusinessCreateView(CreateView):
        model = Business
        fields = ["nome_empresa", "cnpj", "inscricao_estadual", "telefone", "whatsapp", "logradouro", "numero", "complemento", "bairro", "cidade", "estado", "cep", "observacao"]
        success_url = reverse_lazy("business_list")

class BusinessUpdateView(UpdateView):
    model = Business
    fields = ["nome_empresa", "cnpj", "inscricao_estadual", "telefone", "whatsapp", "logradouro", "numero", "complemento", "bairro", "cidade", "estado", "cep", "observacao"]
    success_url = reverse_lazy("business_list")

class BusinessDeleteView(DeleteView):
       model = Business
       success_url = reverse_lazy("business_list")

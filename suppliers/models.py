from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from validate_docbr import CNPJ  # Certifique-se de que o pacote validate-docbr está instalado

# Função para validar o CNPJ
def validar_cnpj(value):
    cnpj = CNPJ()
    if not cnpj.validate(value):
        raise ValidationError("CNPJ inválido. Por favor, insira um CNPJ válido.")

class Suppliers(models.Model):
      # Nome da Empresa
    nome_empresa = models.CharField(max_length=255, verbose_name="Nome da Empresa")
    
    # CNPJ com validador
    cnpj = models.CharField(
        max_length=18, 
        unique=True, 
        verbose_name="CNPJ", 
        validators=[validar_cnpj]
    )
    
    # Inscrição Estadual com validador de 13 dígitos
    inscricao_estadual_validator = RegexValidator(
        regex=r'^\d{13}$',
        message="A Inscrição Estadual deve conter exatamente 13 dígitos"
    )
    inscricao_estadual = models.CharField(
        max_length=13, 
        blank=True, 
        null=True, 
        validators=[inscricao_estadual_validator],
        verbose_name="Inscrição Estadual"
    )

    # Telefone com validador
    telefone_validator = RegexValidator(
        regex=r'^\(\d{2}\)\d{4}-\d{4}$',
        message="O telefone deve estar no formato (00)0000-0000"
    )
    telefone = models.CharField(
        max_length=14, 
        blank=True, 
        null=True, 
        validators=[telefone_validator],
        verbose_name="Telefone"
    )
    
    # WhatsApp com validador
    whatsapp_validator = RegexValidator(
        regex=r'^\(\d{2}\)9\d{4}-\d{4}$',
        message="O WhatsApp deve estar no formato (00)90000-0000"
    )
    whatsapp = models.CharField(
        max_length=15, 
        blank=True, 
        null=True, 
        validators=[whatsapp_validator],
        verbose_name="WhatsApp"
    )

    # Logradouro
    logradouro = models.CharField(max_length=255, verbose_name="Logradouro")
    
    # Número
    numero = models.CharField(max_length=10, verbose_name="Número", default="S/N")
    
    # Complemento
    complemento = models.CharField(max_length=255, blank=True, null=True, verbose_name="Complemento")
    
    # Bairro
    bairro = models.CharField(max_length=100, verbose_name="Bairro")
    
    # Cidade
    cidade = models.CharField(max_length=100, verbose_name="Cidade")

    # Estado: Lista de siglas dos estados brasileiros
    ESTADOS_CHOICES = [
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
    ]
    estado = models.CharField(
        max_length=2, 
        choices=ESTADOS_CHOICES, 
        verbose_name="Estado"
    )
    
    # CEP
    cep = models.CharField(max_length=9, verbose_name="CEP")
    
    # Observação
    observacao = models.TextField(blank=True, null=True, verbose_name="Observação")

    # O campo created_at será inserido automaticamente
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    
    # O campo updated_at será atualizado automaticamente quando o objeto for salvo
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"

    def __str__(self):
        return self.nome_empresa
    
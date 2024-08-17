# Generated by Django 5.1 on 2024-08-17 03:05

import business.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_empresa', models.CharField(max_length=255, verbose_name='Nome da Empresa')),
                ('cnpj', models.CharField(max_length=18, unique=True, validators=[business.models.validar_cnpj], verbose_name='CNPJ')),
                ('inscricao_estadual', models.CharField(blank=True, max_length=13, null=True, validators=[django.core.validators.RegexValidator(message='A Inscrição Estadual deve conter exatamente 13 dígitos', regex='^\\d{13}$')], verbose_name='Inscrição Estadual')),
                ('telefone', models.CharField(blank=True, max_length=14, null=True, validators=[django.core.validators.RegexValidator(message='O telefone deve estar no formato (00)0000-0000', regex='^\\(\\d{2}\\)\\d{4}-\\d{4}$')], verbose_name='Telefone')),
                ('whatsapp', models.CharField(blank=True, max_length=15, null=True, validators=[django.core.validators.RegexValidator(message='O WhatsApp deve estar no formato (00)90000-0000', regex='^\\(\\d{2}\\)9\\d{4}-\\d{4}$')], verbose_name='WhatsApp')),
                ('logradouro', models.CharField(max_length=255, verbose_name='Logradouro')),
                ('numero', models.CharField(default='S/N', max_length=10, verbose_name='Número')),
                ('complemento', models.CharField(blank=True, max_length=255, null=True, verbose_name='Complemento')),
                ('bairro', models.CharField(max_length=100, verbose_name='Bairro')),
                ('cidade', models.CharField(max_length=100, verbose_name='Cidade')),
                ('estado', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], max_length=2, verbose_name='Estado')),
                ('cep', models.CharField(max_length=9, verbose_name='CEP')),
                ('observacao', models.TextField(blank=True, null=True, verbose_name='Observação')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(blank=True, null=True, verbose_name='Atualizado em')),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
            },
        ),
    ]
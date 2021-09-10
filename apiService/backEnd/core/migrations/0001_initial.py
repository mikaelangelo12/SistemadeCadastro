# Generated by Django 3.2.7 on 2021-09-09 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='consultaClinica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('sobreNome', models.CharField(max_length=200)),
                ('datadeNascimento', models.DateField()),
                ('cpf', models.CharField(max_length=11)),
                ('Endereço', models.CharField(max_length=200)),
                ('Bairro', models.CharField(max_length=200)),
                ('Cidade', models.CharField(max_length=200)),
                ('Cep', models.CharField(max_length=200)),
                ('sus', models.CharField(max_length=15)),
                ('telefone', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
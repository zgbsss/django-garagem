# Generated by Django 4.2.5 on 2023-09-12 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0001_initial'),
        ('garagem', '0003_veiculo_descricao_remove_veiculo_acessorio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veiculo',
            name='capa',
            field=models.ManyToManyField(related_name='+', to='uploader.image'),
        ),
    ]

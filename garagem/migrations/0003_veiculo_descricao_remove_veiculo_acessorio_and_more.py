# Generated by Django 4.2.5 on 2023-09-12 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0001_initial'),
        ('garagem', '0002_veiculo_capa'),
    ]

    operations = [
        migrations.AddField(
            model_name='veiculo',
            name='descricao',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.RemoveField(
            model_name='veiculo',
            name='acessorio',
        ),
        migrations.RemoveField(
            model_name='veiculo',
            name='capa',
        ),
        migrations.AddField(
            model_name='veiculo',
            name='acessorio',
            field=models.ManyToManyField(related_name='veiculos', to='garagem.acessorio'),
        ),
        migrations.AddField(
            model_name='veiculo',
            name='capa',
            field=models.ManyToManyField(default=None, related_name='+', to='uploader.image'),
        ),
    ]

# Generated by Django 5.1.6 on 2025-02-09 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classificação', models.CharField(choices=[('A', 'Material'), ('B', 'Equipamento'), ('C', 'Mão de Obra')], max_length=1)),
                ('codigo_insumo', models.IntegerField()),
                ('descrição_insumo', models.TextField()),
                ('unidade', models.CharField(max_length=50)),
                ('origem_preço', models.CharField(choices=[('C', 'C'), ('CC', 'CC')], max_length=50)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='insumos',
        ),
    ]

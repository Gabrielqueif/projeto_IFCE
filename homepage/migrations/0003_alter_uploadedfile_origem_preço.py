# Generated by Django 5.1.6 on 2025-02-09 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_uploadedfile_delete_insumos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadedfile',
            name='origem_preço',
            field=models.CharField(choices=[('C', 'C'), ('CC', 'CC')], max_length=2),
        ),
    ]

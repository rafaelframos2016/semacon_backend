# Generated by Django 5.0.6 on 2024-06-23 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projeto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projeto',
            name='data_criacao',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='projeto',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/projetos'),
        ),
    ]

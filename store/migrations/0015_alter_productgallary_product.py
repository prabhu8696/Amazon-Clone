# Generated by Django 4.2.2 on 2023-08-05 07:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_alter_productgallary_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productgallary',
            name='product',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='store.product'),
        ),
    ]

# Generated by Django 3.2.4 on 2021-06-28 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default="{% static 'images/demo.png' %}", null=True, upload_to='media/products'),
        ),
    ]

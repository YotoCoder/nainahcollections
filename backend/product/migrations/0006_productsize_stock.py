# Generated by Django 4.2.1 on 2023-05-27 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_productsize'),
    ]

    operations = [
        migrations.AddField(
            model_name='productsize',
            name='stock',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]

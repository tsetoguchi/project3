# Generated by Django 2.0.7 on 2018-08-01 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_cart_menu'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='pizza',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Pizza'),
        ),
    ]
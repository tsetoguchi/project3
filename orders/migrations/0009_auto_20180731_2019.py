# Generated by Django 2.0.7 on 2018-07-31 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20180731_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='options',
            name='pizza',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Pizza'),
        ),
        migrations.AlterField(
            model_name='options',
            name='sub',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Sub'),
        ),
        migrations.AlterField(
            model_name='options',
            name='topping',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Topping'),
        ),
    ]
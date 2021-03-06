# Generated by Django 2.0.7 on 2018-07-30 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20180730_1546'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pizzas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pizzas', to='orders.Pizza')),
                ('subs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subs', to='orders.Sub')),
                ('toppings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='toppings', to='orders.Topping')),
            ],
        ),
    ]

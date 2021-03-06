# Generated by Django 2.0.7 on 2018-07-31 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_menu'),
    ]

    operations = [
        migrations.CreateModel(
            name='Options',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pizza', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Pizza')),
                ('sub', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Sub')),
                ('topping', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Topping')),
            ],
        ),
        migrations.RemoveField(
            model_name='menu',
            name='pizzas',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='subs',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='toppings',
        ),
        migrations.DeleteModel(
            name='Menu',
        ),
    ]

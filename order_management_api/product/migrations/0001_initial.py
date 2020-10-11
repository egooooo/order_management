# Generated by Django 2.2.4 on 2020-10-11 07:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, max_length=32)),
                ('price', models.BigIntegerField(default=0)),
                ('discount', models.BigIntegerField(default=0)),
            ],
            options={
                'db_table': 'products',
                'ordering': ['pk'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.SmallIntegerField(choices=[(0, 'New'), (1, 'Completed'), (2, 'Paid')], db_index=True, default=0)),
                ('cashier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cashier', to='users.UserProfile')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product')),
                ('shop_assistant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shop_assistant', to='users.UserProfile')),
            ],
            options={
                'db_table': 'orders',
                'ordering': ['pk'],
                'abstract': False,
            },
        ),
    ]

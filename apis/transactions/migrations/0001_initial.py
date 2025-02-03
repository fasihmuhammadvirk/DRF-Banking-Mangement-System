# Generated by Django 5.1.5 on 2025-02-03 12:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=16)),
                ('transaction_type', models.CharField(choices=[('Deposit', 'Deposit'), ('Withdrawal', 'Withdrawal')], max_length=16)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account', to='accounts.account')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]

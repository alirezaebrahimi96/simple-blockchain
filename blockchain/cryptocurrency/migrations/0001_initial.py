# Generated by Django 4.0.2 on 2022-02-07 05:11

import cryptocurrency.utils
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(default=cryptocurrency.utils.create_new_ref_number, max_length=32, unique=True)),
                ('wallet', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.IntegerField(default=cryptocurrency.utils.create_new_ref_number, primary_key=True, serialize=False, unique=True)),
                ('amount', models.IntegerField()),
                ('reciption', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reciption', to='cryptocurrency.node')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='cryptocurrency.node')),
            ],
        ),
        migrations.CreateModel(
            name='Blockchain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField()),
                ('timestamp', models.IntegerField()),
                ('proof', models.IntegerField()),
                ('previous_hash', models.IntegerField()),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cryptocurrency.transaction')),
            ],
        ),
    ]

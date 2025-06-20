# Generated by Django 5.0.3 on 2025-06-19 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=15)),
                ('address', models.TextField()),
                ('bio', models.TextField(blank=True, null=True)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]

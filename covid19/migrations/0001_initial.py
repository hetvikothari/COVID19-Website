# Generated by Django 3.2.3 on 2021-05-30 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sno', models.IntegerField()),
                ('state_name', models.CharField(max_length=100)),
                ('active', models.IntegerField()),
                ('positive', models.IntegerField()),
                ('cured', models.IntegerField()),
                ('death', models.IntegerField()),
                ('new_active', models.IntegerField()),
                ('new_positive', models.IntegerField()),
                ('new_cured', models.IntegerField()),
                ('new_death', models.IntegerField()),
                ('state_code', models.IntegerField()),
            ],
        ),
    ]

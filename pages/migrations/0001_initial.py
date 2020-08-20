# Generated by Django 3.0.4 on 2020-08-20 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ir', models.CharField(help_text='Enter IR', max_length=160, verbose_name='IR')),
                ('casetype', models.CharField(help_text='Enter Case Type', max_length=160, verbose_name='Case Type')),
                ('status', models.CharField(help_text='Enter Exhibit Type or Status', max_length=160, verbose_name='Exhibit Type or Status')),
                ('region', models.CharField(help_text='Enter Region or District', max_length=160, verbose_name='Region or District')),
                ('client', models.CharField(help_text='Enter Region or District', max_length=160, verbose_name='Client Name')),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
            },
        ),
    ]
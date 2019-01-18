# Generated by Django 2.1.5 on 2019-01-18 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Merchant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=120)),
                ('name', models.CharField(max_length=32)),
                ('surename', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=254)),
                ('autoservice_name', models.CharField(max_length=120)),
                ('reg', models.IntegerField()),
                ('vat', models.IntegerField()),
                ('tel', models.CharField(help_text='Telephone number', max_length=15, null=True)),
                ('address', models.CharField(max_length=120)),
                ('iban', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('photo_url', models.ImageField(upload_to='photos/')),
                ('approved', models.BooleanField()),
            ],
        ),
    ]
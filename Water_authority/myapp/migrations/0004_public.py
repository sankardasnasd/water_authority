# Generated by Django 4.2.5 on 2023-11-07 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_charges_fromunit_alter_charges_tounit_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Public',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('Complaint', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
            ],
        ),
    ]
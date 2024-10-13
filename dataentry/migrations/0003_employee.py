# Generated by Django 5.1.1 on 2024-10-13 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataentry', '0002_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.IntegerField()),
                ('employee_name', models.CharField(max_length=25)),
                ('designation', models.CharField(max_length=25)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('retirement', models.DecimalField(decimal_places=2, max_digits=10)),
                ('other_benefits', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_benefits', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_compensation', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]

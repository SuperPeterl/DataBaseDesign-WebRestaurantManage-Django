# Generated by Django 4.1.7 on 2023-03-23 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posApp', '0014_alter_sales_tablename'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='added_stock',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='sales',
            name='tablename',
            field=models.CharField(default='Table1', max_length=100),
        ),
    ]
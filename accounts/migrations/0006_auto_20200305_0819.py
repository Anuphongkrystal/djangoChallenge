# Generated by Django 3.0.2 on 2020-03-05 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20200305_0813'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='deescription',
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
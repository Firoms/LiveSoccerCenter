# Generated by Django 3.1.2 on 2021-06-01 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0006_auto_20210601_2041"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="files",
            field=models.FileField(null=True, upload_to="Post/%Y/%m/%d/"),
        ),
    ]

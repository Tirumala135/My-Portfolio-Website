# Generated by Django 5.0.1 on 2024-02-23 06:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("profile1", "0006_experience_companyimage"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="category",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="blog",
            name="thumbnail",
            field=models.ImageField(null=True, upload_to="images/"),
        ),
    ]

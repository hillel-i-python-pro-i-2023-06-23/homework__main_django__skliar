# Generated by Django 4.2.3 on 2023-08-12 22:53

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        (
            "fill_contacts",
            "0001_squashed_0005_remove_phoneuser_is_auto_generate_and_more",
        ),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="phoneuser",
            options={"ordering": ["name"]},
        ),
    ]

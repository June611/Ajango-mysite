# Generated by Django 4.2.6 on 2023-10-26 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("qa", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Text2json",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("i_LAIa", models.CharField(max_length=30)),
                ("i_LAIb", models.TextField()),
                ("msg_llm", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

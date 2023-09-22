# Generated by Django 4.2.5 on 2023-09-20 15:52

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Statue",
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
                ("session_number", models.CharField(max_length=128)),
                (
                    "status_in_shafafstu",
                    models.CharField(choices=[("1", "1"), ("0", "0")], max_length=1),
                ),
                ("ordernumber", models.CharField(max_length=128)),
                ("date", models.CharField(max_length=64)),
                ("description", models.TextField()),
                ("source", models.CharField(max_length=128)),
                ("cost", models.CharField(max_length=128)),
                ("ghaedi", models.CharField(max_length=128)),
                ("point1", models.CharField(max_length=128)),
                ("banafi", models.CharField(max_length=128)),
                ("point2", models.CharField(max_length=128)),
                ("gharibzade", models.CharField(max_length=128)),
                ("point3", models.CharField(max_length=128)),
                ("bibak", models.CharField(max_length=128)),
                ("point4", models.CharField(max_length=128)),
                ("behbahhani", models.CharField(max_length=128)),
                ("point5", models.CharField(max_length=128)),
                ("kazemi", models.CharField(max_length=128)),
                ("point6", models.CharField(max_length=128)),
                ("mahdaviyanpor", models.CharField(max_length=128)),
                ("point7", models.CharField(max_length=128)),
            ],
            options={
                "ordering": ["session_number"],
                "indexes": [
                    models.Index(
                        fields=["session_number"], name="brshora_sta_session_160b47_idx"
                    )
                ],
            },
        ),
    ]

# Generated by Django 5.0.6 on 2024-06-30 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Todo",
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
                ("title", models.TextField(max_length=255)),
                ("note", models.TextField(blank=True, max_length=255, null=True)),
                ("status", models.BooleanField(default=1)),
                ("is_completed", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "indexes": [
                    models.Index(fields=["status"], name="crm_todo_status_8466d9_idx"),
                    models.Index(fields=["id"], name="crm_todo_id_ae2943_idx"),
                    models.Index(
                        fields=["is_completed"], name="crm_todo_is_comp_69683a_idx"
                    ),
                ],
            },
        ),
    ]

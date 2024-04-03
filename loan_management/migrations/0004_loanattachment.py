# Generated by Django 5.0.3 on 2024-04-03 00:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("loan_management", "0003_delete_loanattachment"),
    ]

    operations = [
        migrations.CreateModel(
            name="LoanAttachment",
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
                ("attachment", models.FileField(upload_to="loan_attachments/")),
                (
                    "loan",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="attachments",
                        to="loan_management.loan",
                    ),
                ),
            ],
        ),
    ]

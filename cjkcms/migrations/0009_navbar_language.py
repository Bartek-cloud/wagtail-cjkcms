# Generated by Django 4.2.1 on 2023-06-04 21:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cjkcms", "0008_alter_layoutsettings_navbar_langselector"),
    ]

    operations = [
        migrations.AddField(
            model_name="navbar",
            name="language",
            field=models.CharField(
                blank=True,
                choices=[("_all_", "All languages")],
                default="_all_",
                help_text="Select a language to limit display to specific locale.",
                max_length=10,
                verbose_name="Show in language",
            ),
        ),
    ]

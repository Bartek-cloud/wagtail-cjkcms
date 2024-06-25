# Generated by Django 5.0.2 on 2024-03-21 15:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cjkcms", "0020_socialmediasettings_github_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="layoutsettings",
            name="navbar_color_scheme",
        ),
        migrations.AddField(
            model_name="layoutsettings",
            name="color_scheme",
            field=models.CharField(
                blank=True,
                choices=[],
                default="",
                help_text="Default light/dark/custom theme. (MD/Bootstrap only)",
                max_length=50,
                verbose_name="Color scheme",
            ),
        ),
        migrations.AddField(
            model_name="layoutsettings",
            name="light_dark_switch",
            field=models.BooleanField(
                default=False,
                help_text="Show switch to toggle light/dark theme (MD/Bootstrap only)",
                verbose_name="Light/Dark switch",
            ),
        ),
        migrations.AlterField(
            model_name="layoutsettings",
            name="frontend_theme",
            field=models.CharField(
                blank=True,
                choices=[],
                default="",
                help_text="Change the source of your Bootstrap theme.",
                max_length=50,
                verbose_name="Theme variant",
            ),
        ),
        migrations.AlterField(
            model_name="layoutsettings",
            name="navbar_collapse_mode",
            field=models.CharField(
                blank=True,
                choices=[],
                default="",
                help_text="Control on what screen sizes to show and collapse the navbar menu links.",
                max_length=50,
                verbose_name="Collapse navbar menu",
            ),
        ),
        migrations.AlterField(
            model_name="layoutsettings",
            name="navbar_format",
            field=models.CharField(
                blank=True,
                choices=[],
                default="",
                max_length=50,
                verbose_name="Navbar format",
            ),
        ),
        migrations.AlterField(
            model_name="layoutsettings",
            name="navbar_langselector",
            field=models.CharField(
                blank=True,
                choices=[],
                default=None,
                help_text="Choose lang choice selector",
                max_length=255,
                null=True,
                verbose_name="Language selector",
            ),
        ),
    ]

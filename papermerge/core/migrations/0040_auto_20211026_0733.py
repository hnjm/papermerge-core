# Generated by Django 3.2.7 on 2021-10-26 05:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0039_auto_20210216_1014'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='home_folder',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='home_owner', to='core.folder'),
        ),
        migrations.AddField(
            model_name='user',
            name='inbox_folder',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='inbox_owner', to='core.folder'),
        ),
    ]
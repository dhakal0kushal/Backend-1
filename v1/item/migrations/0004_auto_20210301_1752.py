# Generated by Django 3.1.7 on 2021-03-01 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20210223_1925'),
        ('item', '0003_auto_20210223_1925'),
    ]

    operations = [
        migrations.AddField(
            model_name='customizationitem',
            name='branch',
            field=models.ForeignKey(default='fddd9241-298e-4902-9e63-1d61cbff80f0', on_delete=django.db.models.deletion.CASCADE, to='shop.shopbranch'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='modifiergroup',
            name='branch',
            field=models.ForeignKey(default='fddd9241-298e-4902-9e63-1d61cbff80f0', on_delete=django.db.models.deletion.CASCADE, to='shop.shopbranch'),
            preserve_default=False,
        ),
    ]
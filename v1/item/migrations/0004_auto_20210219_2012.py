# Generated by Django 3.1.4 on 2021-02-19 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_auto_20210219_1916'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customization_items',
            options={'verbose_name_plural': 'Customization_Items'},
        ),
        migrations.AlterField(
            model_name='customization_items',
            name='item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='item.item'),
        ),
        migrations.AlterField(
            model_name='customization_items',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

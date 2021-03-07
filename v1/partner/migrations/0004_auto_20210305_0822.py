# Generated by Django 3.1.7 on 2021-03-05 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0003_partnerapplication'),
    ]

    operations = [
        migrations.RenameField(
            model_name='partner',
            old_name='name',
            new_name='detailed_address',
        ),
        migrations.RenameField(
            model_name='partner',
            old_name='street_address',
            new_name='shop_name',
        ),
        migrations.RenameField(
            model_name='partnerapplication',
            old_name='name',
            new_name='designation',
        ),
        migrations.RenameField(
            model_name='partnerapplication',
            old_name='street_address',
            new_name='detailed_address',
        ),
        migrations.RemoveField(
            model_name='partner',
            name='status',
        ),
        migrations.AddField(
            model_name='partner',
            name='state',
            field=models.CharField(default='wdc', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='partnerapplication',
            name='shop_name',
            field=models.CharField(default='test shop', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='partnerapplication',
            name='state',
            field=models.CharField(default='WDC', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='partnerapplication',
            name='status',
            field=models.IntegerField(choices=[(0, 'New'), (1, 'Pending'), (2, 'Waiting-Response'), (3, 'Triaged'), (4, 'Completed'), (5, 'Cancelled'), (6, 'Rejected')], default=0),
        ),
    ]

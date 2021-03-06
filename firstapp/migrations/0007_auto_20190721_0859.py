# Generated by Django 2.2.3 on 2019-07-21 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0006_auto_20190721_0845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marks',
            name='aggregate',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='marks',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='result', to='firstapp.Student'),
        ),
        migrations.AlterField(
            model_name='student',
            name='fName',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='student',
            name='rollNo',
            field=models.IntegerField(unique=True),
        ),
    ]

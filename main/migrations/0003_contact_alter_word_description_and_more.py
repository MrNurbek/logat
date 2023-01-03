# Generated by Django 4.0.6 on 2022-12-31 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_word_description10_word_description2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='word',
            name='description',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name="So'z izohi"),
        ),
        migrations.AlterField(
            model_name='word',
            name='description10',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name="So'z izohi10"),
        ),
        migrations.AlterField(
            model_name='word',
            name='description2',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name="So'z izohi2"),
        ),
        migrations.AlterField(
            model_name='word',
            name='description3',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name="So'z izohi3"),
        ),
        migrations.AlterField(
            model_name='word',
            name='description4',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name="So'z izohi4"),
        ),
        migrations.AlterField(
            model_name='word',
            name='description5',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name="So'z izohi5"),
        ),
        migrations.AlterField(
            model_name='word',
            name='description6',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name="So'z izohi6"),
        ),
        migrations.AlterField(
            model_name='word',
            name='description7',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name="So'z izohi7"),
        ),
        migrations.AlterField(
            model_name='word',
            name='description8',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name="So'z izohi8"),
        ),
        migrations.AlterField(
            model_name='word',
            name='description9',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name="So'z izohi9"),
        ),
    ]
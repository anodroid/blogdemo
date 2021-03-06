# Generated by Django 2.1.7 on 2019-03-30 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190330_2212'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='create_date',
            new_name='created_date',
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visit_date', models.DateField(auto_now_add=True, verbose_name='访问日期')),
                ('count', models.IntegerField(default=0, verbose_name='日访问量')),
            ],
            options={
                'verbose_name': '日访问量',
                'verbose_name_plural': '日访问量',
            },
        ),
    ]

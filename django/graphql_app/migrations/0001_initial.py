# Generated by Django 3.1.4 on 2020-12-13 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_active', models.BooleanField(default=True, verbose_name='アクティブフラグ')),
                ('is_staff', models.BooleanField(default=False, verbose_name='システム管理者フラグ')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='メールアドレス')),
                ('tel_number', models.CharField(max_length=255, null=True, verbose_name='電話番号')),
                ('name', models.CharField(max_length=100, null=True, verbose_name='名前')),
                ('name_kana', models.CharField(max_length=200, null=True, verbose_name='フリガナ')),
            ],
            options={
                'verbose_name': 'ユーザー',
                'verbose_name_plural': 'ユーザー',
                'db_table': 'user',
            },
        ),
    ]

# Generated by Django 5.0.7 on 2024-07-30 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_crud', '0002_alter_authors_table_alter_books_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='authors',
            options={'verbose_name_plural': 'authors'},
        ),
        migrations.AlterModelOptions(
            name='books',
            options={'verbose_name_plural': 'books'},
        ),
        migrations.AlterModelTable(
            name='authors',
            table=None,
        ),
        migrations.AlterModelTable(
            name='books',
            table=None,
        ),
    ]

# Generated by Django 4.2.1 on 2023-06-01 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_books_book_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='book_author',
            field=models.CharField(default='Author', max_length=30),
        ),
        migrations.AlterField(
            model_name='books',
            name='book_desc',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='books',
            name='book_genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book', to='app1.bookgenre'),
        ),
        migrations.AlterField(
            model_name='books',
            name='book_name',
            field=models.CharField(max_length=30),
        ),
    ]
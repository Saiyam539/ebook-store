# Generated by Django 4.2.1 on 2023-06-02 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_remove_wishlist_books_ptr_wishlist_book_cover_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='WishList',
        ),
    ]
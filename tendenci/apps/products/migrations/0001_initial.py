# Generated by Django 3.2.12 on 2022-11-22 13:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tagging.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('files', '0007_auto_20200902_1545'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('entities', '0005_entity_show_for_donation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='name')),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allow_anonymous_view', models.BooleanField(default=True, verbose_name='Public can view')),
                ('allow_user_view', models.BooleanField(default=True, verbose_name='Signed in user can view')),
                ('allow_member_view', models.BooleanField(default=True)),
                ('allow_user_edit', models.BooleanField(default=False, verbose_name='Signed in user can change')),
                ('allow_member_edit', models.BooleanField(default=False)),
                ('create_dt', models.DateTimeField(auto_now_add=True, verbose_name='Created On')),
                ('update_dt', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('creator_username', models.CharField(max_length=150)),
                ('owner_username', models.CharField(max_length=150)),
                ('status', models.BooleanField(default=True, verbose_name='Active')),
                ('status_detail', models.CharField(default='active', max_length=50)),
                ('name', models.CharField(default='', max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('brand', models.CharField(blank=True, default='', max_length=200)),
                ('url', models.URLField(blank=True, default='', help_text='URL outside of this site for the product.')),
                ('item_number', models.CharField(blank=True, default='', max_length=200)),
                ('summary', models.TextField(blank=True, default='', help_text='A brief summary that can be shown in search results.')),
                ('description', models.TextField(default='')),
                ('tags', tagging.fields.TagField(blank=True, help_text='Tag 1, Tag 2, ...', max_length=255)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.category')),
                ('creator', models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_creator', to=settings.AUTH_USER_MODEL)),
                ('entity', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_entity', to='entities.entity')),
                ('owner', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_owner', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='ProductFile',
            fields=[
                ('file_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='files.file')),
                ('photo_description', models.CharField(blank=True, max_length=50, verbose_name='Description')),
                ('position', models.IntegerField(blank=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
            options={
                'ordering': ('position',),
            },
            bases=('files.file',),
        ),
    ]

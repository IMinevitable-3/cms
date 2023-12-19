# Generated by Django 5.0 on 2023-12-19 16:04

import django.db.models.deletion
import modelcluster.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0003_rename_topicindex_topicindexpage'),
        ('wagtaildocs', '0012_uploadeddocument'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topicpage',
            name='documents',
        ),
        migrations.CreateModel(
            name='TopicPageRelatedLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wagtaildocs.document')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_links', to='topic.topicpage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
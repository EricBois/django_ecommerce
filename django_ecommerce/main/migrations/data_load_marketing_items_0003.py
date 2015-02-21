# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


#start with a list of all the data we want to add.
init_marketing_data = [
    {
        "img":"ericface.jpg",
        "heading":"Your Own Profile",
        "caption":"Create your own profile and share your story and exploits with others",
        "button_title":"Sign Up Now"
    },
    {
        "img":"discover.jpg",
        "heading":"Find New Trails",
        "caption":"Discover new area you never heard about",
        "button_title":"Sign Up Now"    },
    {
        "img":"meet.jpg",
        "heading":"Make New Friends",
        "caption":"Meet new people and join them on their own adventure",
        "button_title":"Sign Up"
    },
]
def create_marketing_items(apps, schema_editor):

    MarketingItem = apps.get_model("main", "MarketingItem")
    
    #stare data in database
    [MarketingItem(**d).save() for d in init_marketing_data]


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_statusreport'),
    ]

    operations = [
        migrations.RunPython(create_marketing_items)
    ]

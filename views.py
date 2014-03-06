from flask import request, url_for, abort, current_app
from flask.views import MethodView
from quokka.core.models import Content
from datetime import datetime

import time 
import json

class PostList(MethodView):
    
    def get(self):
             
        filters = {
            'published': True,
            'available_at__lte': datetime.now(),   
            'show_on_channel': True,
            'model': 'posts.post'
        }
        contents = Content.objects().filter(**filters)
        
        posts = []
        for content in contents:

            post = {
                'title': content.title,
                'image': content.get_main_image_url(),
                'body': content.get_text()[:250],
                'c_time': time.mktime(content.created_at.timetuple()),
                'long_slug' : content.long_slug
            }
            posts.append(post)
        return json.dumps(posts)

class PostDetail(MethodView):
    
    def get(self, long_slug):
            
        filters = {
            'published' : True,
            'available_at__lte' : datetime.now(),
            'model' : 'posts.post'
        }
        try:
            content = Content.objects.get(
                long_slug = long_slug,
                **filters
            )
        except Content.DoesNotExist:
            abort(404)
 
        post = {
            'title': content.title,
            'image': content.get_main_image_url(),
            'body': content.get_text(),
            'c_time': time.mktime(content.created_at.timetuple()),
            'long_slug' : content.long_slug
        }

        return json.dumps(post)


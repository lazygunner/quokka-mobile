from flask import request, url_for, abort, current_app
from flask.views import MethodView
from quokka.core.models import Content
from datetime import datetime

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
                'image': content.get_main_image_url()
            }

        
        return 'hehe'
        

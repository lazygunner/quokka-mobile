from flask import request, url_for, abort, current_app
from flask.views import MethodView
from quokka.core.models import Content
from datetime import datetime

class PostList(MethodView):
    
    def get(self):
             
        filters = {
            'published': True,
            'available_at__lte': datetime.now(),   
            'show_on_channel': True
        }
        print '1'
        contents = Content.objects().filter(**filters)
        print contents
        
        return 'hehe'
        

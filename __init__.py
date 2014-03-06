from quokka.core.app import QuokkaModule

module = QuokkaModule("mobile", __name__,
                        template_folder="templates")


from .views import PostList, PostDetail


#module.add_to_template_global()


# urls
module.add_url_rule('/mobile/posts', view_func=PostList.as_view('posts'))
module.add_url_rule('/mobile/posts/<path:long_slug>/', view_func=PostDetail.as_view('post_detail'))

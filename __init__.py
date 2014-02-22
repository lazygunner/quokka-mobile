from quokka.core.app import QuokkaModule

module = QuokkaModule("mobile", __name__,
                        template_folder="templates")


from .views import PostList


#module.add_to_template_global()


# urls
module.add_url_rule('/mobile/posts/', view_func=PostList.as_view('posts'))

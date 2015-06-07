# The Meme as a service API
class MAASApi:

    # Constructor for the API
    def __init__(self):
        pass

    # Handler for the API
    @staticmethod
    def handler(jinja_env, img, bottom_caption=None, top_caption=None):
        template_varibles = {
            "bottom_caption": bottom_caption,
            "top_caption": top_caption,
            "img_url": img
        }

        template = jinja_env.get_template("api.html")
        return template.render(template_varibles)
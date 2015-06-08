# All imports
import urllib

# The image dictionary
IMAGE_DICT = {
    "obama": "/static/img/obama.jpg",
    "404": "/static/img/404.png"
}


# The Meme as a service API
class MAASApi:

    # Constructor for the API
    def __init__(self):
        pass

    # Get the image URL
    @staticmethod
    def image_url(img):
        if img in IMAGE_DICT:
            return IMAGE_DICT[img]
        else:
            return IMAGE_DICT["404"]

    # Handler for the API
    @staticmethod
    def handler(request, response, jinja_env, img, top_caption=None, bottom_caption=None):
        template_varibles = {
            "bottom_caption": bottom_caption,
            "top_caption": top_caption,
            "img_url": MAASApi.image_url(img),
            "meme_url": request.url
        }

        template = jinja_env.get_template("api.html")
        response.write(template.render(template_varibles))
# The image dictionary
IMAGE_DICT = {
    "obama": "/static/img/obama.jpg"
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
            return img

    # Handler for the API
    @staticmethod
    def handler(jinja_env, img, top_caption=None, bottom_caption=None):
        template_varibles = {
            "bottom_caption": bottom_caption,
            "top_caption": top_caption,
            "img_url": MAASApi.image_url(img)
        }

        template = jinja_env.get_template("api.html")
        return template.render(template_varibles)
# The Meme as a service API
class MAASApi:

    # Constructor for the API
    def __init__(self):
        pass

    # Handler for the API
    @staticmethod
    def handler(response, img, bottom_caption=None, top_caption=None):
        response.write(img + ";" + str(top_caption) + ";" + str(bottom_caption))
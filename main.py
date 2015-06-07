# All imports
import webapp2
from MAASApi import MAASApi

# All constant definitions
DEBUG = True


# The Index handler class
class IndexHandler(webapp2.RequestHandler):

    # Handle GET requests for the index page
    def get(self):
        self.response.write('Hello world!')


# The API handler class
class ApiHandler(webapp2.RequestHandler):

    # Handle GET requests for the API
    def get(self, img, bottom_caption=None, top_caption=None):
        MAASApi.handler(self.response, img, bottom_caption, top_caption)

# Initialize the application
app = webapp2.WSGIApplication([
    ('/', IndexHandler),
    ('/?([^/]*)', ApiHandler),
    ('/?([^/]*)/?([^/]*)', ApiHandler),
    ('/?([^/]*)/?([^/]*)/?([^/]*)', ApiHandler)
], debug=DEBUG)

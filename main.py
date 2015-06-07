# All imports
import os
import webapp2
import jinja2
from MAASApi import MAASApi

# All constant definitions
DEBUG = True

# Setup jinja environment
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), "templates")),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True
)


# The Index handler class
class IndexHandler(webapp2.RequestHandler):

    # Handle GET requests for the index page
    def get(self):
        template = JINJA_ENVIRONMENT.get_template("index.html")
        self.response.write(template.render())


# The API handler class
class ApiHandler(webapp2.RequestHandler):

    # Handle GET requests for the API
    def get(self, img, top_caption=None, bottom_caption=None):
        result = MAASApi.handler(JINJA_ENVIRONMENT, img, top_caption, bottom_caption)
        self.response.write(result)

# Initialize the application
app = webapp2.WSGIApplication([
    ('/', IndexHandler),
    ('/?([^/]*)', ApiHandler),
    ('/?([^/]*)/?([^/]*)', ApiHandler),
    ('/?([^/]*)/?([^/]*)/?([^/]*)', ApiHandler)
], debug=DEBUG)

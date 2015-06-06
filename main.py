import webapp2


# The Index handler class
class IndexHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')


# The API handler class
class ApiHandler(webapp2.RequestHandler):
    def get(self):
        pass

app = webapp2.WSGIApplication([
    ('/', IndexHandler),

], debug=True)

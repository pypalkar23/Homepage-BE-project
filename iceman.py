import webapp2,jinja2,os


template_dir=os.path.join(os.path.dirname(__file__),'html')
jinja_env=jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
	autoescape=True)


class MainPage(webapp2.RequestHandler):
    def render_str(self,template,**params):
		"""pass parameters to template and render it"""
		t=jinja_env.get_template(template)
		return t.render(params)
		
    def write(self,*a,**kw):
    	self.response.out.write(*a,**kw)

    def render(self,template,**kw):
		self.write(self.render_str(template,**kw))

    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.render('front.html')

    '''def post(self):
        pass'''

class Desktop(MainPage):
    def get(self):
        self.response.headers['Content-Type']='text/html'
        self.render('desktop.html')

class Mobile(MainPage):
    def get(self):
        self.response.headers['Content-Type']='text/html'
        self.render('mobile.html')


application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/desktop', Desktop),
    ('/mobile', Mobile),
], debug=True)

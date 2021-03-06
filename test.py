from app import app
import unittest

class FlaskTestCase(unittest.TestCase):

	# Ensure that flask was setup correctly
	def test_index(self):
		tester = app.test_client(self)
		response = tester.get('/login', content_type = 'html/text')
		self.assertEqual(response.status_code, 200)

	# Ensure login page loads correctly
	def test_login_page_loads(self):
		tester = app.test_client(self)
		response = tester.get('/login', content_type = 'html/text')
		self.assertTrue('Please login' in response.data)

	# Ensure login behaves correctly given the correct credentials
	def test_correct_login(self):
		tester = app.test_client(self)
		response = tester.post(
			'/login',
			data=dict(username='admin',password='admin'), 
			follow_redirects = True
		)
		self.assertIn('You were just logged in',response.data)

	# Ensure login behaves correctly given the incorrect credentials
	def test_incorrect_login(self):
		tester = app.test_client(self)
		response = tester.post(
			'/login',
			data=dict(username='wrong',password='wrong'), 
			follow_redirects = True
		)
		self.assertIn('Invalid credentials. Please try again',response.data)

	# Ensure logout behaves correctly 
	def test_logout(self):
		tester = app.test_client(self)
		tester.post(
			'/login',
			data=dict(username='admin',password='admin'), 
			follow_redirects = True
		)
		response = tester.get('/logout', follow_redirects = True)
		self.assertIn('You were just logged out',response.data)

	# Ensure that the main page requires login
	def test_main_route_requires_login(self):
		tester = app.test_client(self)
		response = tester.get('/', follow_redirects = True)
		self.assertTrue('You need to login first' in response.data)

	# Ensures logout requires user to be logged in
	def test_logout_requires_login(self):
		tester = app.test_client(self)
		response = tester.get('/logout', follow_redirects = True)
		self.assertTrue('You need to login first' in response.data)

	# Ensures posts are displayed on main page
	def test_posts_show_on_main_page(self):
		tester = app.test_client(self)
		response = tester.post(
			'/login',
			data=dict(username='admin',password='admin'), 
			follow_redirects = True
		)
		self.assertIn('Hello from the shell',response.data)


if __name__ == '__main__':
	unittest.main()





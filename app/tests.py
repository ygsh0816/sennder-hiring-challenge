from django.test import TestCase, RequestFactory
from django.urls import reverse
from .helpers import GetMoviesData
from .views import MoviesListView


class HomeViewTest(TestCase):
    """TestCase class to test the HomeView"""
    def test_view_url_exists_at_desired_location(self):
        """
        Test case to verify that the url exists at the desired location
        """
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """
        Test case to verify that the url is accessible by the URL name
        """
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """
        Test case to verify that the correct template is used by the View
        """
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')


class MoviesListViewTest(TestCase):
    """TestCase class to test the MoviesListView"""
    def test_view_url_exists_at_desired_location(self):
        """
        Test case to verify that the url exists at the desired location
        """
        response = self.client.get('/movies/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """
        Test case to verify that the url is accessible by the URL name
        """
        response = self.client.get(reverse('get-movies'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """
        Test case to verify that the correct template is used by the View
        """
        factory = RequestFactory()
        request = factory.get('/movies/')
        response = MoviesListView.as_view()(request)
        self.assertEqual(response.template_name, 'movies.html')

    def test_context_data(self):
        """
        Test case to verify that the context data contains the movies list
        """
        factory = RequestFactory()
        request = factory.get('/movies/')
        response = MoviesListView.as_view()(request)
        self.assertIsNotNone(response.context_data['movies'])


class GetMoviesDataTest(TestCase):
    """TestCase class to test the helper class GetMoviesData"""
    def test_people_response_is_list(self):
        """
        Test case to verify that the people API returns a list of People
        """
        data = GetMoviesData()
        response = data.get_all_people()
        self.assertEqual(type(response), list)

    def test_films_response_is_list(self):
        """
        Test case to verify that the films API returns a list of Films
        """
        data = GetMoviesData()
        response = data.get_all_people()
        self.assertEqual(type(response), list)

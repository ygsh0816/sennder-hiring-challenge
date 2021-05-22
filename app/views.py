from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt

from .helpers import GetMoviesData


class HomeView(TemplateView):
    """
    Home View
    """
    template_name = 'home.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        """Dispatch method of TemplateView is overridden"""
        return super(HomeView, self).dispatch(request, *args, **kwargs)

    def get_template_names(self):
        """Method to return template used for this view.
        This method is used when there are multiple templates used in the view """
        template = self.template_name
        return template


class MoviesListView(TemplateView):
    """
    List View to get all the movies from the database
    """
    template_name = 'movies.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        """Dispatch method of TemplateView is overridden"""
        return super(MoviesListView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        """method to return context data"""
        context = super(MoviesListView, self).get_context_data()
        movies_and_people = []

        movie = GetMoviesData()
        movies = movie.get_all_films()
        people = movie.get_all_people()

        for movie in movies:
            movie_data = {'movie_name': movie['title'], 'movie_id': movie['id']}
            peo_of_mov = [x['name'] for x in people if movie['id'] in x['films'][0]]
            movie_data['people'] = peo_of_mov
            movies_and_people.append(movie_data)

        context.update({'movies': movies_and_people})
        return context

    def get_template_names(self):
        """Method to return template used for this view.
        This method is used when there are multiple templates used in the view """
        template = self.template_name
        return template

import requests
from django.conf import settings
from .endpoints import *


class GetMoviesData:
    """
    Class to get different kinds of data related to movies
    """
    def __init__(self):
        """Constructor of the class GetMoviesData"""
        self.__session = requests.Session()

    def get_all_films(self):
        """
        Method to get all films from films endpoint of APIs.
        :return: Json response of films
        """
        try:
            response = self.__session.get(settings.GHIBLIA_BASE_URL + GET_ALL_FILMS)
            return response.json()
        except requests.ConnectionError as error:
            print(error)

    def get_all_people(self):
        """
        Method to get all people from People endpoint of APIs.
        :return: Json response of people
        """
        try:
            response = self.__session.get(settings.GHIBLIA_BASE_URL + GET_ALL_PEOPLE)
            return response.json()
        except requests.ConnectionError as error:
            print(error)

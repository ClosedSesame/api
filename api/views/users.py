from sqlalchemy.exc import IntegrityError, DataError
from .models.schemas import users
from pyramid_restful.viewsets import APIViewSet
from ..models import WeatherLocation, Account
from pyramid.response import Response
import requests
import json
import os



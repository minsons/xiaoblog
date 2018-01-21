from flask import Blueprint
blog = Blueprint('main',__name__)
from . import views
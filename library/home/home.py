from flask import Blueprint, render_template, redirect, url_for, session, request

import library.adapters.repository as repo

import library.utilities.utilities as utilities
import library.home.services as services

# configure blueprint
home_blueprint = Blueprint(
    "home_bp", __name__)


@home_blueprint.route('/', methods=['GET'])
def home():

    form_search = utilities.SearchForm()

    featured_books = services.get_random_books()

    return render_template(
        "home/home.html",
        form_search=form_search,
        featured_books=featured_books
    )

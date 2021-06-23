from app import main
from flask import render_template, request, redirect, url_for
from . import main


@main.route('/')
def index():
    title = 'AutoMech'


    return render_template('viewmech.html', title=title)

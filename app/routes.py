from flask import Blueprint, request

from app.pages.index import index_page
from app.pages.earthquake import earthquake_page
from app.pages.three_d import three_d_page
from app.pages.about import about_page
from app.pages.faq import faq_page
from app.pages.contact import contact_page, contact_success_page
from app.pages.not_found import not_found_page


main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/')
def index():
    return index_page()

@main_blueprint.route('/earthquake')
def earthquake():
    last_day = request.args.get("last_day", 1, type=int)
    if last_day > 360:
        last_day = 360
    if last_day < 1:
        last_day = 1
    return earthquake_page(last_day)

@main_blueprint.route('/3d_earthquake')
def three_d():
    return three_d_page()

@main_blueprint.route('/about')
def about():
    return about_page()

@main_blueprint.route('/faq')
def faq():
    return faq_page()

@main_blueprint.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        return contact_success_page(name=name, email=email, message=message)
    
    # GET isteği için iletişim sayfasını döndür
    return contact_page()

@main_blueprint.errorhandler(404)
def not_found(e):
    return not_found_page(e)
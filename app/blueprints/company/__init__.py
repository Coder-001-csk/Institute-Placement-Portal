from flask import Blueprint

company_bp = Blueprint('company', __name__, template_folder='../../../templates/company')

from . import routes
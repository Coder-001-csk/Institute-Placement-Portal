from flask import Blueprint

auth_bp = Blueprint('auth', __name__, template_folder='../../../templates/auth')

from . import routes  # Import routes at the end to avoid circular imports
from . import auth_bp

@auth_bp.route('/')
def index():
    return "Auth Blueprint - To be implemented in Phase 3"
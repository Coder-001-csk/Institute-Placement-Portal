from . import company_bp

@company_bp.route('/')
def index():
    return "Company Blueprint - To be implemented in Phase 5"
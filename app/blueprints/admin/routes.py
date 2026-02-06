from . import admin_bp

@admin_bp.route('/')
def index():
    return "Admin Blueprint - To be implemented in Phase 4"
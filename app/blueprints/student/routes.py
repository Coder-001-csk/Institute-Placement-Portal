from . import student_bp

@student_bp.route('/')
def index():
    return "Student Blueprint - To be implemented in Phase 6"
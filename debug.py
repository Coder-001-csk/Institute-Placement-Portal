import sys
import os

print("Python version:", sys.version)
print("Current directory:", os.getcwd())
print("\nTrying to import auth_bp...")

try:
    from app.blueprints.auth import auth_bp
    print("✅ Successfully imported auth_bp")
except ImportError as e:
    print(f"❌ ImportError: {e}")
    print("\nChecking auth blueprint files...")
    auth_path = os.path.join('app', 'blueprints', 'auth')
    if os.path.exists(auth_path):
        print("Auth folder exists:", os.listdir(auth_path))
    else:
        print("Auth folder does not exist!")
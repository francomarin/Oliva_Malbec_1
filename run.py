from app import create_app
from app.utils.initializers import initialize_roles

app = create_app()

with app.app_context():
    initialize_roles()

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)
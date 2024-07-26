from app import db
from app.models.role import Role

def initialize_roles():
    role_names = ["ESTUDIANTE", "DOCENTE", "ADMINISTRADOR"]
    for role_name in role_names:
        if not Role.query.filter_by(name=role_name).first():
            role = Role(name=role_name)
            db.session.add(role)
        db.session.commit()
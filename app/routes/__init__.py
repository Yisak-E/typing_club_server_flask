from app.routes.test_route import type_bp


def register_routes(app):
    app.register_blueprint(type_bp)


import flask

admin_page = flask.Blueprint(
    name = "admin",
    import_name = "admin",
    template_folder = "templates",
    static_url_path = "/admin/"
)
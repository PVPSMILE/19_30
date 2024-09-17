import flask

def render_admin():
    return flask.render_template(template_name_or_list = "admin.html")
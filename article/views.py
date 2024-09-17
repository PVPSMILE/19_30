import flask

def show_article():
    return flask.render_template(template_name_or_list = "article.html")
from pages.login_page import Login


def before_all(context):
    context.login = Login()


def after_all(context):
    context.login.close()

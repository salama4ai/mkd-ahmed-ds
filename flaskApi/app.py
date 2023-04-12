from flask import Flask
from views.dashboard import dash

# pwd = %pwd
# don't name the app "flask" if the package is also named flask to not conflect with the package name
app = Flask(__name__, instance_relative_config=True, instance_path=r".\instance")
app.config.from_object("config.default")
app.config.from_pyfile("config.py")
# app.config.from_envvar("APP_SETTINGS")

app.register_blueprint(dash)#, url_prefix="/dash/") ## url_prefix either used here or in the views .py file or not used at all




# # add as many templates as you want and import them as that
# from views.home import home
# app.register_blueprint(home)



if __name__ == '__main__':
    app.run(port=8000, debug=app.config["DEBUG"])
from flask import render_template, Blueprint, request

# there isn't any restriction on the string here "dashboard" in our example
form = Blueprint("formm", __name__)



posts = [{"title": "al fatehah",
          "reader": "el-menshawy",
          "ayat": 7}, 
         {"title": "al-falaq",
          "reader": "el-hosary",
          "ayat": 6
            }]



# when you want to add multiple routes for the same page you can add as many route as you want, if any of them visited the function will run

@dash.route("/form")
@dash.route("/")
def m():
    return render_template(r"form\index.html")  


# you can name the functions as you want there isn't any restrictions, example here function named main, but don't name multiple functions with the same name

@dash.route("/query/<path:query>")
def main(query):
    path = requests.args.get("query")
    return "the most advanced"

# note the 
@dash.route("/", methods=["POST", "GET"])
def methodd():
    if request.method=="GET":
        redirect("/home")
    return "the most advanced"


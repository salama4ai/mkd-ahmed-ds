from flask import Flask
app = Flask(__name__)

@app.route("/", method="Post")
def query():
    return ""

if __name__=="__main__":
    app.run(port=3000, debug=False)
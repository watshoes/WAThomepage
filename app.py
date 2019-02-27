from flask import Flask, render_template, url_for, send_from_directory, request
from create_spreadsheet import Spreadsheet
from gmailConnector import GmailConnector
#sheet = Spreadsheet()
goog = GmailConnector()
app = Flask(__name__, static_url_path='')

@app.route("/",methods=["POST","GET"])
def index():
    if request.method == "POST":
        message = goog.create_message(request.form['email'],'sean@watshoes.co',request.form['name']+ " sending from website",request.form['message'])
        serv = goog.serv()
        goog.send_message(serv,"sean",message)

    return render_template("index.html")

@app.route("/images/<path:path>")
def send_images(path):
        return send_from_directory('images',path)

@app.route("/assets/<path:path>")
def send_assets(path):
    return send_from_directory("assets",path)

if __name__ == "__main__":
    app.run(debug=True)

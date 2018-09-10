from flask import Flask, render_template, url_for, send_from_directory, request
from create_spreadsheet import Spreadsheet
sheet = Spreadsheet()
app = Flask(__name__, static_url_path='')

@app.route("/",methods=["POST","GET"])
def index():
    if 'gender' in request.form:
        sheet.add_values(request.form)
    return render_template("index.html")
@app.route("/images/<path:path>")
def send_images(path):
        return send_from_directory('images',path)
@app.route("/assets/<path:path>")
def send_assets(path):
    return send_from_directory("assets",path)
if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, url_for, send_from_directory, request
import boto3
import urllib3
from upload_to_lambda import UploadLambda
import os
from werkzeug.utils import secure_filename


UPLOAD_PATH = "/Users/seanbrown/projects/WAThomepage/pics"
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
upload = UploadLambda()

app = Flask(__name__, static_url_path='')
app.config["UPLOAD_FOLDER"] = UPLOAD_PATH

"""
Todo:
    Make only the shoe upload section of index page
    change instead of the whole page.
"""
pool = urllib3.PoolManager()
"""
Send the shoe to the lambda function to be run through the neuralnet
"""

@app.route("/",methods=["POST","GET"])
def index():
    if request.method == "POST":
        #This part will handle the uploading of a shoe and run it  through our nueral network
        if "shoe_upload" in request.files:
            shoe = request.files["shoe_upload"]
            print("check here",shoe.filename.split('.')[1])
            if shoe.filename.split('.')[1] in ALLOWED_EXTENSIONS:
                filename = secure_filename(shoe.filename)
                shoe.save(os.path.join(app.config["UPLOAD_FOLDER"],filename))
                wat  = upload.upload(os.path.join(app.config["UPLOAD_FOLDER"],filename))
                return render_template("index.html", answer_shoe=wat)

    return render_template("index.html", answer_shoe="")

if __name__ == "__main__":
    app.run(debug=True)

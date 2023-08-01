

from re import DEBUG, sub
from flask import Flask, render_template, request, redirect, send_file, url_for
from werkzeug.utils import secure_filename, send_from_directory
import os
import subprocess


app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_word():
    # subprocess.run(['python3', 'detect.py', '--weights', 'runs/train/yolov5s_results/weights/best.pt', '--img', '416', '--conf', '0.4','--source', 'Pothole-Detection-1/test/images'])
    return render_template('index.html')


# @app.route('/', methods=['POST'])
# def predict():
#     imagefile = request.files['imagefile']
#     image_path = "./images/" +imagefile.filename
#     imagefile.save(image_path)
#     return render_template('index.html')


@app.route("/opencam", methods=['GET'])
def opencam():
    print("here")
    subprocess.run(['python3', 'detect.py', '--weights', 'runs/train/yolov5s_results/weights/best.pt', '--img', '416', '--conf', '0.4','--source', 'Pothole-Detection-1/test/images'])
    return 'done'


if __name__ == '__main__':
    app.run(port=3000, debug=True)
    
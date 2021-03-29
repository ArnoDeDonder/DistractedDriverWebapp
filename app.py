import os
from flask import Flask, request
from PIL import Image
from fastai.vision.all import *

UPLOAD_FOLDER = './upload'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

model = load_learner("export.pkl")

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if(request.method == 'POST'):
        if 'image' not in request.files:
                return 'there is no image in form!'
        image = Image.open(request.files['image'].stream)
        out = model.predict(tensor(image))
        return out[0]
    else:
        return "API operational"

if __name__ == '__main__':
    app.run()
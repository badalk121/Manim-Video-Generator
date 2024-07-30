import os
from flask import render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from app import app
from app.forms import InputForm
from manim import *

UPLOAD_FOLDER = 'app/static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

class VideoScene(Scene):
    def __init__(self, text, image_path):
        self.text = text
        self.image_path = image_path
        super().__init__()

    def construct(self):
        bg_image = ImageMobject(self.image_path).scale_to_fit_height(7)
        self.add(bg_image)
        
        text_chunks = self.text.split('\n')
        text_objs = [Text(chunk, font_size=24).to_edge(UP) for chunk in text_chunks]
        
        for text_obj in text_objs:
            self.add(text_obj)
            self.wait(2)
            self.remove(text_obj)

def generate_video(text, image_path):
    scene = VideoScene(text, image_path)
    scene.render()

@app.route('/', methods=['GET', 'POST'])
def index():
    form = InputForm()
    if form.validate_on_submit():
        text = form.text.data
        if 'image' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['image']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            generate_video(text, filepath)
            return redirect(url_for('success'))
    return render_template('index.html', form=form)

@app.route('/success')
def success():
    return "Video has been generated successfully!"

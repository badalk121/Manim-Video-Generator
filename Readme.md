# Manim Video Generator
This project is a Flask web app that generates videos using Manim. Users can input text and an optional background image. The UI is modern and responsive, with options for video resolution and FPS. The project includes setup instructions for running on VS Code.


## Features
- Input text and optional background image
- Long text formatted like a presentation
- Image positioning options (background or foreground)
- Modern, responsive UI
- Options for video resolution and FPS


## Requirements
- Python 3.7 or higher
- Virtual environment (venv)
- Flask
- Flask-WTF
- Manim


## Setup Instructions
1. **Clone the repository**

   ```shell
   git clone https://github.com/badalk121/Manim-Video-Generator.git
   cd manim_video_generator
   ```
   
2. **Initialize a virtual environment**
   ```shell
   python -m venv venv
   ```

3. **Activate the virtual environment**
   For Windows:
   ```shell
   venv\Scripts\activate
   ```
   For macOS/Linux:
   ```shell
   source venv/bin/activate
   ```
   
4. **Install required packages**
   ```shell
   pip install -r requirements.txt
   ```
    
5. **Run the Flask application**
   ```shell
   python run.py
   ```

6. Access the web app
Open a web browser and go to http://127.0.0.1:5000

## File Descriptions
1. **run.py**: Entry point for running the Flask application.
2. **app/__init__.py**: Initializes the Flask app.
3. **app/routes.py**: Contains the route definitions and video generation logic.
4. **app/forms.py**: Defines the form for inputting text and image.
5. **app/templates/index.html**: HTML template for the web app.
6. **app/static/styles.css**: CSS for styling the web app.


## Running the Project on VS Code
1. **Open the project folder in VS Code:**
   ```shell
   code .
   ```

2. **Open a terminal in VS Code and activate the virtual environment (If you created one):**
   ```shell
   venv\Scripts\activate
   ```

3. **Run the Flask application**
   ```shell
   python run.py
   ```

## License
**This project is licensed under the MIT License - see the LICENSE file for details.**

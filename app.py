from openai import open_ai
import json
import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        song_name = request.form.get('song_name')
        return redirect(url_for('result', song_name=song_name))
    return render_template('index.html')

@app.route('/result/<song_name>')
def result(song_name):
    genre_info = get_genre(song_name)
    return render_template('result.html', genre_info=genre_info, song_name=song_name)

def get_genre(music_name):
    config_file_path = "config.json"
    open_ai_key, open_ai_model = get_credentials(config_file_path=config_file_path)
    genre_name = open_ai(music_name=music_name, open_ai_key=open_ai_key, open_ai_model=open_ai_model)
    return genre_name

def get_credentials(config_file_path):
    """Retrieve credentials from the JSON config file."""
    if not os.path.exists(config_file_path):
        raise FileNotFoundError(f"Config file not found: {config_file_path}")

    try:
        with open(config_file_path, 'r') as file:
            config = json.load(file)
            api_key = config['OPEN_AI_KEY']
            open_ai_model = config['OPEN_AI_MODEL']
            return api_key, open_ai_model
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON format: {e}")
    except KeyError as e:
        raise KeyError(f"Missing key in configuration file: {e}")
    except Exception as e:
        raise Exception(f"Failed to retrieve credentials: {e}")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)


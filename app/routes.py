from app import app
from flask import render_template
import requests
from app.forms import SearchForm


@app.route('/', methods=['GET', 'POST'])
def index():
    form = SearchForm()
    if form.validate_on_submit():
        response = requests.get(f'https://www.googleapis.com/books/v1/volumes?q={form.query.data}')
        volumeInfo = json_extract(response.json(), 'title')
        print(volumeInfo)
        return render_template('books.html', title='Home', books=volumeInfo, form=form)
    return render_template('index.html', form=form)


def json_extract(obj, key):
    """Recursively fetch values from nested JSON."""
    arr = []

    def extract(obj, arr, key):
        """Recursively search for values of key in JSON tree."""
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    values = extract(obj, arr, key)
    return values

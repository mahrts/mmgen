"""This script run the flask meme generator app."""

import random
import os
from urllib.parse import urlparse
import requests
from flask import Flask, render_template, request
from QuoteEngine.QuoteEngine import Ingestor, QuoteModel
from MemeGenerator.MemeGenerator import MemeEngine

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    # TODO: Use the Ingestor class to parse all files in the
    # quote_files variable
    quotes = []
    for file in quote_files:
        quotes += Ingestor.parse(file)

    images_path = "./_data/photos/dog/"
    imgs = []
    for root, _, files in os.walk(images_path):
        imgs += [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """
    image_url = request.form.get("image_url")
    answer = requests.get(image_url, allow_redirects = True)

    # get extension from URL
    path = urlparse(image_url).path
    ext = os.path.splitext(path)[1]

    # fallback if no extension
    if ext == "":
        ext = ".jpg"
    tmp =  f"{meme.output_dir}/{random.randint(0, 100000000)}.{ext}"
    with open(tmp, 'wb') as out:
        out.write(answer.content)

    quote = QuoteModel(request.form.get('author'), request.form.get('body'))

    path = meme.make_meme(tmp, quote.body, quote.author)
    os.remove(tmp)

    return render_template('meme.html', path=path)

if __name__ == "__main__":
    app.run()

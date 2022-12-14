import cohere
import os
import textwrap

from dotenv import load_dotenv
from flask import Flask, request
from googletrans import Translator

load_dotenv()

app = Flask(__name__)
translator = Translator()

api_key = os.getenv("API_KEY")
co = cohere.Client(api_key)


def get_translation(received_data):
    translated_text = translator.translate(received_data)
    return translated_text.text


def get_summary(received_data):
    prompt = textwrap.dedent(f'''Passage: {received_data}
    TLDR: ''')

    print(prompt)

    #parameters to change outcome of summary
    prediction = co.generate(
        max_tokens = 100,
        model = os.getenv("MODEL"), #model size
        prompt = prompt, #the prompt
        stop_sequences = [". ", ".\n"], # Good enough for end of sentence and paragraph
        temperature = 0.1, #number to determine likelihood of random responses
        k = 200, #ensures top k of number of tokens to generate
        p = 0.75, #p ensures that only the most likely tokens, with total probability mass of p, are considered for generation at each step
        frequency_penalty = 0.5, #penalizes new tokens based on their existing frequency in the text so far
        presence_penalty = 0.5, #penalizes new tokens based on whether they appear in the text so far
    )

    print(prediction.generations[0])
    return prediction.generations[0].text


@app.route("/")
def index():
    return "heAR"


@app.route('/summary')
def summary():
    res = request.args.get("q")
    return get_summary(res)


@app.route('/translate')
def translate():
    res = request.args.get("q")
    return get_translation(res)


if __name__ == "__main__":
    app.run()

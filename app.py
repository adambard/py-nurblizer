import re
from flask import Flask, render_template, request
app = Flask(__name__)

with open("nouns.txt") as f:
    NOUNS = [l.strip().lower() for l in f]

def nurble(text):
    text = text.upper()
    words = re.sub(r'[^a-z ]', '', text.lower()).split()

    for word in words:
        if word not in NOUNS:
            text = re.sub(r'(\b)' + word + r'(\b)', r'\1<span class="nurble">nurble</span>\2', text, flags=re.I)

    return text.replace('\n', '<br>')

@app.route("/", methods=['GET'])
def index_view():
    return render_template("index.html")

@app.route("/nurble", methods=['POST'])
def nurble_view():
    return render_template("nurble.html", text=nurble(request.form.get('text', '')))

if __name__ == "__main__":
    app.run()

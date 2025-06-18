from flask import Flask, render_template
import random

app = Flask(__name__)

# Local list of quotes
quotes = [
    {"content": "Stay hungry, stay foolish.", "author": "Steve Jobs"},
    {"content": "Be yourself; everyone else is already taken.", "author": "Oscar Wilde"},
    {"content": "Simplicity is the ultimate sophistication.", "author": "Leonardo da Vinci"},
    {"content": "The only limit to our realization of tomorrow is our doubts of today.", "author": "Franklin D. Roosevelt"},
]

@app.route('/')
def index():
    quote = random.choice(quotes)
    return render_template('rand_quote.html', quote=quote)

if __name__ == '__main__':
    app.run(port=5004,debug=True)

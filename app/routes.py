

from flask import Flask, render_template, request, redirect, url_for
from app.models.llm_ans import run_analysis

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def main():
    response = None
    urls = None

    if request.method == 'POST':
        urls = request.form['urls']
        response = run_analysis(urls)

    return render_template('index.html', urls=urls, response=response)

@app.route("/ask-again")
def ask_again():
    return redirect(url_for('main'))

if __name__ == "__main__":
    app.run(debug=True)
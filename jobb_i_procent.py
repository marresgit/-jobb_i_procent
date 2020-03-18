
from flask import Flask, escape, request, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def main():
   return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')

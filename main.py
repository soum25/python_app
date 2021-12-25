<<<<<<< HEAD
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5550)
=======
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():  
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5555)
>>>>>>> 527ab00488a7c072aa3ef12b19a24e0443ec37f9

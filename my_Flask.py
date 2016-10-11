from flask import Flask, render_template

app = Flask(__name__)

stream1 = 'My experience with streem 1 was good i learn alot and i made a cool website'

stream2 = 'My experience with streem 2 is ok. I am struggling at the moment but i will get there.'


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/stream')
def list_streem():
    return render_template('index.html', stream=stream1, second=stream2)


if __name__ == '__main__':
    app.run()

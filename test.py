from flask import Flask

app = Flask('__main__')

@app.route('/')
def test():
    return "<h1> Hello There!!</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
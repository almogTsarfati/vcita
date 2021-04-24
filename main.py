from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['POST'])
def api():
    content = request.get_data()
    print(content.decode())
    return content.decode()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
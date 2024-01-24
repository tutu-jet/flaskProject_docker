from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0')  # 在Flask应用程序中，确保将app.run()方法更改为app.run(host='0.0.0.0')，以便Flask应用程序可以在Docker容器外部访问。

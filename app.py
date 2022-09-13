from flask import Flask
app=Flask(__name__)

@app.get('/')
def run():
    return 'hello world'

if __name__ == '__main__':
    app.run('0.0.0.0', 8000)
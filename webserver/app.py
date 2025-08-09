from flask import Flask, Response
app = Flask(__name__)

@app.route("/")
def index():
    return "Web server is running"

@app.route("/metrics")
def metrics():
    return Response('webapp_up 1\n', mimetype='text/plain')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
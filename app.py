import os
from flask import Flask 
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

@app.route("/")
def hello():
    return "hello world! ... again.."


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            # debug must be set to False before deployment
            debug=True)
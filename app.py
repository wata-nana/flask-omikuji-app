from flask import Flask, render_template
from random import choice

app = Flask(__name__)


@app.route("/omikuji")
def omikuji():
    fotune_list = ["大吉", "吉", "凶"]
    result = choice(fotune_list)

    return render_template("omikuji.html", result=result)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)

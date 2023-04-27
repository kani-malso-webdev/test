from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/", methods=["POST"])
def index():
    output = request.get_json()
    data = {
        "result": output
    }

    print(output)

    return "success"

if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0')
from flask import Flask, request
app = Flask(__name__)


@app.route("/", methods=["POST"])
def index():
    output = request.get_json()
   

    print(output)

    return "success"

if __name__ == "__main__":
    app.run(debug=True)

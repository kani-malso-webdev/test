from flask import Flask, request
import firebase_admin
from firebase_admin import credentials , db
app = Flask(__name__)

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{

    "databaseURL": "https://saathi-9eb76-default-rtdb.firebaseio.com/"
})

ref1 = db.reference("test")
@app.route("/", methods=["POST"])
def index():
    output = request.get_json()
    ref1.set(output)

    print(output)

    return "success"

if __name__ == "__main__":
    app.run(debug=True)
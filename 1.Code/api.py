from flask import *

app = Flask(__name__)



@app.route("/")
def hello():

    return "welcome to number plate detection"

@app.route("/<string:n>")
def details(n):
    dic1 = {
        "GJ18AH3054": {
            "name": "Abhi Soni",

            "email-id": "soniabhi@gmail.com",
            "Adhaar-no":"534653475867"

        },
        "1T20BOM": {
            "name": "MEET Soni",
            "email-id": "sonimeet@gmail.com",
            "Adhaar-no": "534653475867"

        },
        "HR26DK8337": {
            "name": "Aman Soni",
            "email-id": "soniaman@gmail.com",
            "Adhaar-no": "534653475867"

        },
        "MH12DE1433": {
            "name": "ANKIT Soni ",
            "email-id": "soniankit@gmail.com",
            "Adhaar-no": "534653475867"
        },
        "KL21S8086": {
            "name": "RAJ Soni",
            "email-id": "soniraj@gmail.com",
            "Adhaar-no": "534653475867"
        },
        "TN07CM1347": {
            "name": "RAJ Soni",
            "email-id": "soniraj@gmail.com",
            "Adhaar-no": "534653475867"
        },
        "21BH2345AA": {
            "name": "ANKIT Soni ",
            "email-id": "soniankit@gmail.com",
            "Adhaar-no": "534653475867"
        },
        "GJ03LK0563": {
            "name": "ANKIT Soni ",
            "email-id": "soniankit@gmail.com",
            "Adhaar-no": "534653475867"
        }
    }
    for i in dic1:
        if i == n:
            name = dic1[i]["name"]
            email = dic1[i]["email-id"]
            adhar=dic1[i]["Adhaar-no"]
            result = {
                "name": name,
                "email-id": email,
                "adhaar-no":adhar
            }

            return jsonify(result)
        # return jsonify({
        #     "name": "yash",
        #     "email": "yash@mail.com"
        # })
    else:
        return jsonify({
            "name": "try",
            "email": "try@mail.com"
        })


# def show_user(username):
#     return f'hello{username}'
#
# app.add_url_rule('/user/<username>', 'show_user', show_user)
if __name__ == "__main__":
    app.run(debug=True)
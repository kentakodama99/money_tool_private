from flask import Flask,render_template,send_file,jsonify
import csv

app = Flask(__name__, static_folder="./frontend/dist", static_url_path="")

PATH = "./test.csv"

#RestApi
class objectCsv(object):
    def __init__(self):
        f = open(PATH, "r",encoding="ms932",errors="",newline='') # ms932にエンコードしないと使えない。
        read_file = csv.DictReader(f, delimiter=",",quotechar='"',skipinitialspace=True)
        self.read_file = read_file
        
    def getCsv(self):
        csv_list = []
        for row in self.read_file:
            csv_list.append(row)
        return csv_list

    def addCsv(self):
        return "addCsv"

    def putCsv(self):
        return "putCsv"

    def deleteCsv(self):
        return "deleteCsv"

@app.route('/users')
def list_user():
    object_csv =  objectCsv()
    csv_list = object_csv.getCsv()
    return jsonify(csv_list)

@app.errorhandler(404)
def index(_):
    return send_file("./frontend/dist/index.html")

if __name__ == "__main__":
    app.run(host='localhost')
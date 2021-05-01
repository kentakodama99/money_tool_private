from flask import Flask,render_template,send_file,jsonify,request
import csv
from flask_cors import CORS

app = Flask(__name__, static_folder="./frontend/dist", static_url_path="")
PATH = "./test.csv"
CORS(app)

#RestApi
class objectCsv(object):
    def __init__(self):
        fw = open(PATH, "a",encoding="ms932",errors="",newline='') # ms932にエンコードしないと使えない。
        write_file = csv.writer(fw, delimiter=",",quotechar='"',skipinitialspace=True)
        self.write_file = write_file
        month=0
        money=0
        travel_cost=0
        difference=0
        
    def getCsv(self):
        fr = open(PATH, "r",encoding="ms932",errors="",newline='') # ms932にエンコードしないと使えない。
        read_file = csv.DictReader(fr, delimiter=",",quotechar='"',skipinitialspace=True)
        csv_list = []
        for row in read_file:
            csv_list.append(row)
        return csv_list

    def addCsv(self,month,money,travel_cost,difference):
        self.write_file.writerow([month, money,travel_cost,difference])
        return

    def putCsv(self):
        return "putCsv"

    def deleteCsv(self):
        return "deleteCsv"

@app.route('/users')
def list_user():
    object_csv =  objectCsv()
    return jsonify(object_csv.getCsv())

@app.route('/users', methods=['POST'])
def post_user():
    object_csv =  objectCsv()
    month=request.form["month"]
    money=request.form["money"]
    travel_cost=request.form["travel_cost"]
    difference=request.form["difference"]
    object_csv.addCsv(month,money,travel_cost,difference)
    return "OK"


@app.errorhandler(404)
def index(_):
    return send_file("./frontend/dist/index.html")

if __name__ == "__main__":
    app.run(host='localhost')
from flask import Flask,render_template,send_file,jsonify,request
import csv
# from flask_cors import CORS

app = Flask(__name__, static_folder="./frontend/dist", static_url_path="")
PATH = "./csv/test.csv"
# CORS(app)

#RestAPI
class objectCsv(object):
    def __init__(self):
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
        fr.close()
        return csv_list

    def addCsv(self,month,money,travel_cost,difference):
        fa = open(PATH, "a",encoding="ms932",errors="",newline='') # ms932にエンコードしないと使えない。
        write_file = csv.writer(fa, delimiter=",",quotechar='"',skipinitialspace=True)
        write_file.writerow([month, money,travel_cost,difference])
        fa.close()
        return

    def putCsv(self,rlist,id,month,money,travel_cost,difference):
        fw = open(PATH, "w",encoding="ms932",errors="",newline='') # ms932にエンコードしないと使えない。
        write_file = csv.writer(fw, delimiter=",",quotechar='"',skipinitialspace=True)
        write_file.writerow(["month","money","travel_cost","difference"])
        count = 0
        for row in rlist:
            if id == count:
                write_file.writerow([month, money,travel_cost,difference])
            else:
                write_file.writerow([row["month"],row["money"],row["travel_cost"],row["difference"]])
            count+=1
        fw.close()
        return

    def deleteCsv(self,rlist,id):
        fw = open(PATH, "w",encoding="ms932",errors="",newline='') # ms932にエンコードしないと使えない。
        write_file = csv.writer(fw, delimiter=",",quotechar='"',skipinitialspace=True)
        write_file.writerow(["month","money","travel_cost","difference"])
        count = 0
        for row in rlist:
            if not id == count:
                write_file.writerow([row["month"],row["money"],row["travel_cost"],row["difference"]])
            count+=1
        fw.close()
        return

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

@app.route('/users/<user_id>', methods=['PUT'])
def put_user(user_id):
    object_csv =  objectCsv()
    id = int(user_id)
    month=request.form["month"]
    money=request.form["money"]
    travel_cost=request.form["travel_cost"]
    difference=request.form["difference"]
    object_csv.putCsv(object_csv.getCsv(),id,month,money,travel_cost,difference)
    return "OK"

@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    object_csv =  objectCsv()
    id = int(user_id)
    object_csv.deleteCsv(object_csv.getCsv(),id)
    return "OK"

@app.errorhandler(404)
def index(_):
    return send_file("./frontend/dist/index.html")

if __name__ == "__main__":
    app.run(host='localhost')
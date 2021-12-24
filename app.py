from flask import Flask, jsonify, request

tasks = [
    {
        "Contact":"9872346523",
        "Name":"Raju",
        "done":False,
        "id":1
    },

    {
        "Contact":"9872342347",
        "Name":"Aarav",
        "done":False,
        "id":2
    }
]
app = Flask(__name__)
@app.route("/add-data", methods=['POST'])
def add_task(): 
    if not request.json: 
        return jsonify({ 
            "status":"error", 
            "message": "Please provide the data!" },400) 
    contact = {
         'ID': tasks[-1]['ID'] + 1, 
        'Name': request.json['Name'], 
        'Contact': request.json.get('Contact', ""), 
        'done': False } 
    tasks.append(contact) 
    return jsonify({
        "status":"success", "message": "Task added succesfully!" })

@app.route("/")
def hello():
    return "This is a product page!"

@app.route("/get-data") 
def get_task(): 
    return jsonify({ "data" : tasks })

if __name__=="__main__":
    app.run(debug=True)
from flask import Flask, request
from runs import RunsDB  # Updated import to RunsDB

app = Flask(__name__)

@app.route("/runs/<int:run_id>", methods=["OPTIONS"])
def handle_cors_options(run_id):
    return "", 204, {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "PUT, DELETE, GET",
        "Access-Control-Allow-Headers": "Content-Type"
    }

@app.route("/runs/<int:run_id>", methods=["GET"])
def get_run(run_id):
    db = RunsDB("runs_db.db")  # Updated database filename
    run = db.getRun(run_id)  # Assumes getRun method fetches a run by id
    if run:
        return run, 200, {"Access-Control-Allow-Origin": "*"}
    else:
        return f"Run {run_id} not found", 404, {"Access-Control-Allow-Origin": "*"}

@app.route("/runs", methods=["GET"])
def retrieve_runs():
    db = RunsDB("runs_db.db")  # Updated database filename
    RUNS = db.getRuns()
    return RUNS, 200, {"Access-Control-Allow-Origin": "*"}

@app.route("/runs", methods=["POST"])
def create_run():
    db = RunsDB("runs_db.db")  # Updated database filename
    print("The request data is: ", request.form)
    
    # Extracting the new fields based on the updated table structure
    distance = request.form["distance"]
    title = request.form["title"]
    intensity = request.form["intensity"]
    description = request.form["description"]
    with_person = request.form["with"]  # Note: 'with' is a reserved word
    ground = request.form["ground"]
    
    db.createRun(distance, title, intensity, description, with_person, ground)
    return "Created", 201, {"Access-Control-Allow-Origin": "*"}

@app.route("/runs/<int:run_id>", methods=["PUT"])
def update_run(run_id):
    print("The update request data is: ", request.form)
    db = RunsDB("runs_db.db")  # Updated database filename
    
    run = db.getRun(run_id)
    if run:
        # Extracting the new fields
        distance = request.form["distance"]
        title = request.form["title"]
        intensity = request.form["intensity"]
        description = request.form["description"]
        with_person = request.form["with"]
        ground = request.form["ground"]
        
        db.updateRun(run_id, distance, title, intensity, description, with_person, ground)
        return "Updated", 200, {"Access-Control-Allow-Origin": "*"}
    else:
        return f"Run {run_id} not found", 404, {"Access-Control-Allow-Origin": "*"}

@app.route("/runs/<int:run_id>", methods=["DELETE"])
def delete_run(run_id):
    db = RunsDB("runs_db.db")  # Updated database filename
    if db.getRun(run_id) is None:
        return f"Run {run_id} not found", 404, {"Access-Control-Allow-Origin": "*"}
    else: 
        db.deleteRun(run_id)  # Updated method name to deleteRun
        return "Deleted", 200, {"Access-Control-Allow-Origin": "*"}

def run():
    app.run(port=8080, host='0.0.0.0')

if __name__ == "__main__":
    run()

import sqlite3

def dict_factory(cursor, row):
    # Converts each row to a dictionary
    fields = [column[0] for column in cursor.description]
    return {fields[i]: row[i] for i in range(len(fields))}

class RunsDB:

    def __init__(self, filename):
        self.connection = sqlite3.connect(filename)
        self.connection.row_factory = dict_factory  # Uses dict_factory to convert rows to dicts
        self.cursor = self.connection.cursor()

    def getRuns(self):
        # Retrieves all runs
        self.cursor.execute("SELECT * FROM runs")
        return self.cursor.fetchall()

    def getRun(self, id):
        self.cursor.execute("SELECT * FROM runs WHERE id = ?", [id])
        return self.cursor.fetchone() 
    
    def createRun(self, distance, title, intensity, description, with_person, ground):
        data = [distance, title, intensity, description, with_person, ground]
        self.cursor.execute(
            "INSERT INTO runs (distance, title, intensity, description, with, ground) VALUES (?, ?, ?, ?, ?, ?)", data
        )
        self.connection.commit()

    def updateRun(self, id, distance, title, intensity, description, with_person, ground):
        data = [distance, title, intensity, description, with_person, ground, id]
        self.cursor.execute(
            "UPDATE runs SET distance = ?, title = ?, intensity = ?, description = ?, with = ?, ground = ? WHERE id = ?", data
        )
        self.connection.commit()

    def deleteRun(self, id):
        # Deletes a run by ID
        self.cursor.execute("DELETE FROM runs WHERE id = ?", [id])
        self.connection.commit()

    def close(self):
        # Closes the database connection
        self.connection.close()

import sqlite3

def dict_factory(cursor, row):
    fields = []

    for column in cursor.description:
        fields.append(column[0])
    
    result_dict = {}
    for i in range(len(fields)):
        result_dict[fields[i]] = row[i]

    return result_dict

class RunsDB:

    def __init__(self, filename):
        self.connection = sqlite3.connect(filename)
        self.connection.row_factory = dict_factory
        self.cursor = self.connection.cursor()

    def getRuns(self):
        self.cursor.execute("SELECT * FROM runs")
        return self.cursor.fetchall()
        
    def getRun(self, id):
        data = [id]
        self.cursor.execute("SELECT * FROM runs WHERE id = ?", data)
        return self.cursor.fetchone()
    
    def createRun(self, distance, title, intensity, description, with_person, ground):
        data = [distance, title, intensity, description, with_person, ground]
        self.cursor.execute("INSERT INTO runs (distance, title, intensity, description, with, ground) VALUES (?, ?, ?, ?, ?, ?)", data)
        self.connection.commit()

    def updateRun(self, id, distance, title, intensity, description, with_person, ground):
        data = [distance, title, intensity, description, with_person, ground, id]
        self.cursor.execute("UPDATE runs SET distance = ?, title = ?, intensity = ?, description = ?, with = ?, ground = ? WHERE id = ?", data)
        self.connection.commit()
    
    def deleteRun(self, id):
        data = [id]
        self.cursor.execute("DELETE FROM runs WHERE id = ?", data)
        self.connection.commit()

    def close(self):
        self.connection.close()

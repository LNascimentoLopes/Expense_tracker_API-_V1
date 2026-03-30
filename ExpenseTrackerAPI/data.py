import json

dataJson = "Database.json"

def getData():
    try:
        with open(dataJson, "r") as f:
            data = json.load(f)


    except FileNotFoundError:
        data = []

    return data

def insert_Data(store):
    data = getData()
    data.append(store)
    saveData(data)

def saveData(data):
    with open(dataJson, "w") as f:
        json.dump(data, f, indent=4)
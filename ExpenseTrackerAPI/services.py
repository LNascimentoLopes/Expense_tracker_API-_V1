from datetime import datetime

from data import *

def add_expense_db(input):
    expense_dict = input.model_dump()
    expense_dict["ID"] = add_ids()
    expense_dict["date"] = datetime.today().strftime("%Y-%m-%d")
    insert_Data(expense_dict)
    return expense_dict

def add_ids():
    info = getData()
    max_id = max((i["ID"] for i in info), default=0) + 1
    print(max_id)
    return max_id

def remove_expense_db(id):
    info = getData()
    for i in info:
        if i["ID"] == id:
            info.remove(i)
    saveData(info)

def update_expense(id, data):
    t_data = data.model_dump()
    info = getData()
    for i in info:
        if i["ID"] == id:
            info[info.index(i)]["description"] = t_data["description"]
            info[info.index(i)]["value"] = t_data["value"]
    saveData(info)

def sum_all_expenses():
    expenses = getData()
    value = 0
    for i in expenses:
        value += i["value"]
    return value

def get_expense_by_month(month):
    expenses = getData()
    f_expenses = []
    for i in expenses:
        if datetime.fromisoformat(i["date"]).month <= month:
            f_expenses.append(i)
    return f_expenses
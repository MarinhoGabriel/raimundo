from xmlrpc.server import SimpleXMLRPCServer
import os
import pandas as pd

def persist_data(data):
    data.to_csv("notas.csv", sep=";", encoding="utf-8", index=False)

def read_data():
    return pd.read_csv("notas.csv", sep=";", encoding="utf-8")

def maybe_create_file():
    files = os.listdir('.')
    
    if(not("notas.csv" in files)):
        data = pd.DataFrame(columns=["registration", "subject", "grade"])
        persist_data(data)

if (__name__ == "__main__"):
    maybe_create_file()

    global data
    data = read_data()
    print(data)
    server = SimpleXMLRPCServer(('localhost', 9001), logRequests=True, allow_none=True)

    def register_grade(registration, subject, grade):
        global data
        
        if(get_grade(registration, subject)):
            data.loc[(data['subject'] == subject) & (data['registration'] == int(registration)), "grade"] = float(grade)
            print("Grade", grade, "updated for student", registration, "on subject", subject)
        
        else:
            record = {
                'registration': int(registration),
                'subject':subject,
                'grade': float(grade)
            }

            data = data.append(record, ignore_index=True)
            print("Grade", grade, "registered for student", registration, "on subject", subject)
        
        persist_data(data)
        
    def get_grade(registration, subject):
        print("Grade X for student", registration, "on subject", subject)
        indexes = (data['subject'] == subject) & (data['registration'] == int(registration))
        return list(data.loc[indexes, "grade"])

    def get_all_grades(registration):
        indexes = data['registration'] == int(registration)
        rtn = list(data.loc[indexes, "grade"])
        return rtn

    def get_ac(registration):
        indexes = data['registration'] == int(registration)
        rtn = list(data.loc[indexes, "grade"])
        ac = sum(rtn)/len(rtn)
        print("The average coeficient for student", registration, "is", ac)
        
        return ac

    def start_server():
        try:
            print ('To shutdown the server, press CTRL + C')
            server.serve_forever()
        except KeyboardInterrupt:
            server.server_close()
            print ('Shutting down server...')

    server.register_function(register_grade)
    server.register_function(get_grade)
    server.register_function(get_all_grades)
    server.register_function(get_ac)

    start_server()

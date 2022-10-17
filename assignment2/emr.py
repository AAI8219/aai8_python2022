import uuid
import pymysql
import json



class Config:
    def __init__(self):
        self.db_conn = pymysql.connect(host="67.205.163.33",
                             user="aai8",
                             password="InfSci1500_4263658",
                             db="aai8",
                             charset="utf8mb4",
                             cursorclass=pymysql.cursors.DictCursor)
    
class doctor:
    def __init__(self, doctor_id="", first_name = "", last_name = "", title = "", speciality = ""):
        self.__f_name = first_name
        self.__l_name = last_name
        self.__title = title
        self.__speciality = speciality
        
        if doctor_id == "":
            self.__doctor_id = str(uuid.uuid4())
            try: 
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    checkVal = 'INSERT INTO doctor (doctor_id, first_name, last_name, title, speciality)'
                    checkVal = checkVal + ' VALUES(%s, %s, %s, %s, %s)'
                    print(checkVal)
                    cur.execute(checkVal, (self.__doctor_id, self.__f_name, self.__l_name, self.__title, self.__speciality)) 
                    con.commit()
            finally:
                con.close()
        else:
            self.__doctor_id = doctor_id
            try:
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = "SELECT * FROM doctor WHERE doctor_id = '" + doctor_id + "'"
                    print(qry)
                    cur.execute(qry)
                    rows = cur.fetchall()
                    for row in rows:
                        self.__doctor_id = row["doctor_id"]
                        self.__f_name = row["first_name"]
                        self.__l_name = row["last_name"]
                        self.__title  = row["title"]
                        self.__speciality  = row["speciality"]

            finally:
                con.close()
    def editDoctor(self, first_name = "", last_name = "", title = "", speciality = ""):
        self.__f_name = first_name
        self.__l_name = last_name
        self.__title = title
        self.__speciality = speciality
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE doctor SET first_name = %s, last_name = %s, title = %s, speciality = %s WHERE doctor_id = %s;'
                print(qry)
                cur.execute(qry, (self.__f_name, self.__l_name, self.__title, self.__speciality, self.__doctor_id)) 
                con.commit()
        finally:
            con.close()
    
    def set_first_name(self, first_name=""):
        self.__f_name = first_name
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE doctor SET first_name = %s WHERE doctor_id = %s;'
                print(qry)
                cur.execute(qry, (self.__f_name, self.__doctor_id)) 
                con.commit()
        finally:
            con.close()
    def set_last_name(self, last_name=""):
        self.__l_name = last_name
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE doctor SET last_name = %s WHERE doctor_id = %s;'
                print(qry)
                cur.execute(qry, (self.__l_name, self.__doctor_id)) 
                con.commit()
        finally:
            con.close()
    def set_title(self, title=""):
        self.__title = title
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE doctor SET title = %s WHERE doctor_id = %s;'
                print(qry)
                cur.execute(qry, (self.__title, self.__doctor_id)) 
                con.commit()
        finally:
            con.close()
    def set_speciality(self, speciality=""):
        self.__speciality = speciality
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE doctor SET speciality = %s WHERE doctor_id = %s;'
                print(qry)
                cur.execute(qry, (self.__speciality, self.__doctor_id)) 
                con.commit()
        finally:
            con.close()

    def get_doctor_id(self):
        return self.__doctor_id

    def deleteDoctor(self):
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'DELETE FROM doctor WHERE doctor_id = %s;'
                print("deleting....")
                cur.execute(qry, ( self.__doctor_id)) 
                con.commit()
        finally:
            con.close()


    def to_json(self):
        fields_data = {
            "id" : self.__doctor_id,
            "f_name" : self.__f_name,
            "l_name" : self.__l_name,
            "title" : self.__title,
            "speciality" : self.__speciality

        }
        return json.dumps(fields_data)
    


class patient:
    def __init__(self, patient_id="", first_name = "", last_name = "", age = 0, birth_date = "", health_condition = ""):
        self.__f_name = first_name
        self.__l_name = last_name
        self.__age = age
        self.__birth_date = birth_date
        self.__health_condition = health_condition
        if patient_id == "":
            self.__patient_id = str(uuid.uuid4())
            try: 
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    checkVal = 'INSERT INTO patient (patient_id, first_name, last_name, age, birth_date, health_condition)'
                    checkVal = checkVal + ' VALUES(%s, %s, %s, %s, %s, %s)'
                    print(checkVal)
                    cur.execute(checkVal, (self.__patient_id, self.__f_name, self.__l_name, self.__age, self.__birth_date, self.__health_condition)) 
                    con.commit()
            finally:
                con.close()
        else:
            self.__patient_id = patient_id
            try:
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = "SELECT * FROM patient WHERE patient_id = '" + patient_id + "'"
                    print(qry)
                    cur.execute(qry)
                    rows = cur.fetchall()
                    for row in rows:
                        self.__patient_id = row["patient_id"]
                        self.__f_name = row["first_name"]
                        self.__l_name = row["last_name"]
                        self.__age  = row["age"]
                        self.__birth_date  = row["birth_date"]
                        self.__health_condition = row["health_condition"]
            finally:
                con.close()
    
    def editPatient(self, first_name = "", last_name = "", age = 0, birth_date = "", health_condition = ""):
        self.__f_name = first_name
        self.__l_name = last_name
        self.__age = age
        self.__birth_date = birth_date
        self.__health_condition = health_condition
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE patient SET first_name = %s, last_name = %s, age = %s, birth_date = %s, health_condition = %s WHERE patient_id = %s;'
                print(qry)
                cur.execute(qry, (self.__f_name, self.__l_name, self.__age, self.__birth_date, self.__health_condition, self.__patient_id)) 
                con.commit()
        finally:
            con.close()
    
    def set_first_name(self, first_name=""):
        self.__f_name = first_name
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE patient SET first_name = %s WHERE patient_id = %s;'
                print(qry)
                cur.execute(qry, (self.__f_name, self.__patient_id)) 
                con.commit()
        finally:
            con.close()
    def set_last_name(self, last_name=""):
        self.__l_name = last_name
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE patient SET last_name = %s WHERE patient_id = %s;'
                print(qry)
                cur.execute(qry, (self.__l_name, self.__patient_id)) 
                con.commit()
        finally:
            con.close()
    def set_age(self, age=0):
        self.__age = age
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE patient SET age = %s WHERE patient_id = %s;'
                print(qry)
                cur.execute(qry, (self.__age, self.__patient_id)) 
                con.commit()
        finally:
            con.close()
    def set_birth_date(self, birth_date=""):
        self.__birth_date = birth_date
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE patient SET birth_date = %s WHERE patient_id = %s;'
                print(qry)
                cur.execute(qry, (self.__birth_date, self.__patient_id)) 
                con.commit()
        finally:
            con.close()
    def set_health_condition(self, health_condition=""):
        self.__health_condition = health_condition
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE patient SET health_condition = %s WHERE patient_id = %s;'
                print(qry)
                cur.execute(qry, (self.__health_condition, self.__patient_id)) 
                con.commit()
        finally:
            con.close()

    def get_patient_id(self):
        return self.__patient_id

    def deletePatient(self):
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'DELETE FROM patient WHERE patient_id = %s;'
                print("deleting....")
                cur.execute(qry, ( self.__patient_id)) 
                con.commit()
        finally:
            con.close()
    def to_json(self):
        fields_data = {
            "id" : self.__patient_id,
            "f_name" : self.__f_name,
            "l_name" : self.__l_name,
            "age" : self.__age,
            "birth_date" : self.__birth_date,
            "health_condition" : self.__health_condition
        }
        return json.dumps(fields_data)



class visit():
    def __init__(self, visit_id="", doctor_id="", patient_id = "", date_of_visit = "", visit_location_street_address = "", visit_location_city = "", visit_location_state = "", visit_location_zip = ""):
        self.__doctor_id = doctor_id
        self.__patient_id = patient_id
        self.__date_of_visit = date_of_visit
        self.__visit_location_street_address = visit_location_street_address
        self.__visit_location_city = visit_location_city
        self.__visit_location_state = visit_location_state
        self.__visit_location_zip = visit_location_zip
        if visit_id == "":
            self.__visit_id = str(uuid.uuid4())
            
            try: 
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    checkVal = 'INSERT INTO visit (visit_id, doctor_id, patient_id, date_of_visit, visit_location_street_address, visit_location_city, visit_location_state, visit_location_zip)'
                    checkVal = checkVal + ' VALUES(%s, %s, %s, %s, %s, %s, %s, %s)'
                    print(checkVal)
                    cur.execute(checkVal, (self.__visit_id, self.__doctor_id, self.__patient_id, self.__date_of_visit, self.__visit_location_street_address, self.__visit_location_city, self.__visit_location_state, self.__visit_location_zip)) 
                    con.commit()
            finally:
                con.close()
        else:
            self.__visit_id = visit_id
            try:
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = "SELECT * FROM visit WHERE visit_id = '" + visit_id + "'"
                    print(qry)
                    cur.execute(qry)
                    rows = cur.fetchall()
                    for row in rows:
                        self.__visit_id = row["visit_id"]
                        self.__doctor_id = row["doctor_id"]
                        self.__patient_id = row["patient_id"]
                        self.__date_of_visit = row["date_of_visit"]
                        self.__visit_location_street_address  = row["visit_location_street_address"]
                        self.__visit_location_city  = row["visit_location_city"]
                        self.__visit_location_state = row["visit_location_state"]
                        self.__visit_location_zip = row["visit_location_zip"]
            finally:
                con.close()

    def editVisit(self, date_of_visit = "", visit_location_street_address = "", visit_location_city = "", visit_location_state = "", visit_location_zip = ""):
        
        self.__date_of_visit = date_of_visit
        self.__visit_location_street_address = visit_location_street_address
        self.__visit_location_city = visit_location_city
        self.__visit_location_state = visit_location_state
        self.__visit_location_zip = visit_location_zip
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE visit SET date_of_visit = %s, visit_location_street_address = %s, visit_location_city = %s, visit_location_state = %s, visit_location_zip = %s WHERE visit_id = %s;'
                print(qry)
                cur.execute(qry, (self.__date_of_visit, self.__visit_location_street_address, self.__visit_location_city, self.__visit_location_state, self.__visit_location_zip, self.__visit_id)) 
                con.commit()
        finally:
            con.close()
    
    def set_date_of_visit(self, date_of_visit=""):
        self.__date_of_visit = date_of_visit
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE visit SET date_of_visit = %s WHERE visit_id = %s;'
                print(qry)
                cur.execute(qry, (self.__date_of_visit, self.__visit_id)) 
                con.commit()
        finally:
            con.close()
    
    def set_visit_location_street_address(self, visit_location_street_address=""):
        self.__visit_location_street_address = visit_location_street_address
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE visit SET visit_location_street_address = %s WHERE visit_id = %s;'
                print(qry)
                cur.execute(qry, (self.__visit_location_street_address, self.__visit_id)) 
                con.commit()
        finally:
            con.close()
    def set_visit_location_city(self, visit_location_city=""):
        self.__visit_location_city = visit_location_city
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE visit SET visit_location_city = %s WHERE visit_id = %s;'
                print(qry)
                cur.execute(qry, (self.__visit_location_city, self.__visit_id)) 
                con.commit()
        finally:
            con.close()
    def set_visit_location_state(self, visit_location_state=""):
        self.__visit_location_state = visit_location_state
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE visit SET visit_location_state = %s WHERE visit_id = %s;'
                print(qry)
                cur.execute(qry, (self.__visit_location_state, self.__visit_id)) 
                con.commit()
        finally:
            con.close()
    def set_visit_location_zip(self, visit_location_zip=""):
        self.__visit_location_zip = visit_location_zip
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE visit SET visit_location_zip = %s WHERE visit_id = %s;'
                print(qry)
                cur.execute(qry, (self.__visit_location_zip, self.__visit_id)) 
                con.commit()
        finally:
            con.close()
    def deleteVisit(self):
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'DELETE FROM visit WHERE visit_id = %s;'
                print("deleting....")
                cur.execute(qry, ( self.__visit_id)) 
                con.commit()
        finally:
            con.close()

    def to_json(self):
        fields_data = {
            "id" : self.__visit_id,
            "doctor_id" : self.__doctor_id,
            "patient_id" : self.__patient_id,
            "date_of_visit" : self.__date_of_visit,
            "visit_location_street_address" : self.__visit_location_street_address,
            "visit_location_city" : self.__visit_location_city,
            "visit_location_state" : self.__visit_location_state,
            "visit_location_zip" : self.__visit_location_zip,
        }
        return json.dumps(fields_data)
    

class diagnosis:
    def __init__(self, diagnosis_id="", diagnosis_name = "", date_of_diagnosis = ""):
        self.__diagnosis_name = diagnosis_name
        self.__date_of_diagnosis = date_of_diagnosis
        if diagnosis_id == "":
            self.__diagnosis_id = str(uuid.uuid4())
            try: 
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    checkVal = 'INSERT INTO diagnosis (diagnosis_id, diagnosis_name, date_of_diagnosis)'
                    checkVal = checkVal + ' VALUES(%s, %s, %s)'
                    print(checkVal)
                    cur.execute(checkVal, (self.__diagnosis_id, self.__diagnosis_name, self.__date_of_diagnosis)) 
                    con.commit()
            finally:
                con.close()
        else:
            self.__diagnosis_id = diagnosis_id
            print( self.__diagnosis_id)
            try:
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = "SELECT * FROM diagnosis WHERE diagnosis_id = '" + diagnosis_id + "'"
                    print(qry)
                    cur.execute(qry)
                    rows = cur.fetchall()
                    for row in rows:
                        self.__diagnosis_id = row["diagnosis_id"]
                        self.__diagnosis_name = row["diagnosis_name"]
                        self.__date_of_diagnosis = row["date_of_diagnosis"]
            finally:
                con.close()


    def editDiagnosis(self, diagnosis_name = "", date_of_diagnosis = ""):
        self.__diagnosis_name = diagnosis_name
        self.__date_of_diagnosis = date_of_diagnosis
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE diagnosis SET diagnosis_name = %s, date_of_diagnosis = %s WHERE diagnosis_id = %s;'
                print(qry)
                cur.execute(qry, (self.__diagnosis_name, self.__date_of_diagnosis, self.__diagnosis_id))  
                con.commit()
        finally:
            con.close()

    def set_diagnosis_name(self, diagnosis_name=""):
        self.__diagnosis_name = diagnosis_name
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE diagnosis SET diagnosis_name = %s WHERE diagnosis_id = %s;'
                print(qry)
                cur.execute(qry, (self.__diagnosis_name, self.__diagnosis_id)) 
                con.commit()
        finally:
            con.close()
    def set_date_of_diagnosis(self, date_of_diagnosis=""):
        self.__date_of_diagnosis = date_of_diagnosis
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE diagnosis SET date_of_diagnosis = %s WHERE diagnosis_id = %s;'
                print(qry)
                cur.execute(qry, (self.__date_of_diagnosis, self.__diagnosis_id)) 
                con.commit()
        finally:
            con.close()
    def deleteDiagnosis(self):
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'DELETE FROM diagnosis WHERE diagnosis_id = %s;'
                print("deleting....")
                cur.execute(qry, ( self.__diagnosis_id)) 
                con.commit()
        finally:
            con.close()
    
    def to_json(self):
        fields_data = {
            "id" : self.__diagnosis_id,
            "diagnosis_name" : self.__diagnosis_name,
            "date_of_diagnosis" : self.__date_of_diagnosis
        }
        return json.dumps(fields_data)

class procedure_1:
    def __init__(self, procedure_1_id="", procedure_1_name = "", date_of_procedure_1 = ""):
        self.__procedure_1_name = procedure_1_name
        self.__date_of_procedure_1 = date_of_procedure_1
        if procedure_1_id == "":
            self.__procedure_1_id = str(uuid.uuid4())
            try: 
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    checkVal = 'INSERT INTO procedure_1 (procedure_1_id, procedure_1_name, date_of_procedure_1)'
                    checkVal = checkVal + ' VALUES(%s, %s, %s)'
                    print(checkVal)
                    cur.execute(checkVal, (self.__procedure_1_id, self.__procedure_1_name, self.__date_of_procedure_1)) 
                    con.commit()
            finally:
                con.close()
        else:
            self.__procedure_1_id = procedure_1_id
            try:
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = "SELECT * FROM procedure_1 WHERE procedure_1_id = '" + procedure_1_id + "'"
                    print(qry)
                    cur.execute(qry)
                    rows = cur.fetchall()
                    for row in rows:
                        self.__procedure_1_id = row["procedure_1_id"]
                        self.__procedure_1_name = row["procedure_1_name"]
                        self.__date_of_procedure_1 = row["date_of_procedure_1"]
            finally:
                con.close()
    def editProcedure_1(self, procedure_1_name = "", date_of_procedure_1 = ""):
        self.__procedure_1_name = procedure_1_name
        self.__date_of_procedure_1 = date_of_procedure_1
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE procedure_1 SET procedure_1_name = %s, date_of_procedure_1 = %s WHERE procedure_1_id = %s;'
                print(qry)
                cur.execute(qry, (self.__procedure_1_name, self.__date_of_procedure_1, self.__procedure_1_id))  
                con.commit()
        finally:
            con.close()
    def set_procedure_1_name(self, procedure_1_name=""):
        self.__procedure_1_name = procedure_1_name
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE procedure_1 SET procedure_1_name = %s WHERE procedure_1_id = %s;'
                print(qry)
                cur.execute(qry, (self.__procedure_1_name, self.__procedure_1_id)) 
                con.commit()
        finally:
            con.close()
    def set_date_of_procedure_1(self, date_of_procedure_1=""):
        self.__date_of_procedure_1 = date_of_procedure_1
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE procedure_1 SET date_of_procedure_1 = %s WHERE procedure_1_id = %s;'
                print(qry)
                cur.execute(qry, (self.__date_of_procedure_1, self.__procedure_1_id)) 
                con.commit()
        finally:
            con.close()
    def deleteProcedure_1(self):
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'DELETE FROM procedure_1 WHERE procedure_1_id = %s;'
                print("deleting....")
                cur.execute(qry, ( self.__procedure_1_id)) 
                con.commit()
        finally:
            con.close()
    
    def to_json(self):
        fields_data = {
            "id" : self.__procedure_1_id,
            "procedure_1_name" : self.__procedure_1_name,
            "date_of_procedure_1" : self.__date_of_procedure_1
        }
        return json.dumps(fields_data)





"""

Testing Area :

doc = doctor(doctor_id="", first_name = "Aasri", last_name = "Inu", title = "Dentist", speciality = "Pod")
#docJ = doctor(doctor_id="", first_name = "Jon", last_name = "Snow", title = "Intern", speciality = "Pediatric")
#doc.editDoctor("Leela", "Inu", "Surgeon", "Cardio")
#print(doc.to_json())
#doc.deleteDoctor()
#docJ.deleteDoctor()
doc.set_speciality("Test")

pat = patient(patient_id="", first_name="Jane", last_name="Smith", age=32, birth_date="2022-07-19", health_condition="headache")
pat.editPatient("John", "Smith", 22, "2022-07-12", "heart attack")
pat.set_first_name("Jim")
pat.set_last_name("Morty")
pat.set_age(45)
pat.set_birth_date("1947-08-15")
pat.set_health_condition("internal bleeding")
pat.deletePatient()

doc = doctor(doctor_id="", first_name = "Aasri", last_name = "Inu", title = "Dentist", speciality = "Pod")
pat = patient(patient_id="", first_name="Jane", last_name="Smith", age=32, birth_date="2022-07-19", health_condition="Test headache")

print("Hello")
doc_id = doc.get_doctor_id()
pat_id = pat.get_patient_id()
vis = visit(visit_id="", doctor_id= doc_id, patient_id= pat_id, date_of_visit="2022-08-15", visit_location_street_address="1234 Franklin Drive", visit_location_city="Pittsburgh", visit_location_state="PA", visit_location_zip="12345")
vis.editVisit("2024-09-23", "1888 Franklin Dr.", "NYC", "NY", "12121")
vis.set_date_of_visit("2026-02-22")
vis.set_visit_location_street_address("2222 test street")
vis.set_visit_location_city("Atlanta")
vis.set_visit_location_state("GA")
vis.set_visit_location_zip("55555")

vis.deleteVisit()

dig = diagnosis(diagnosis_id="", diagnosis_name="headache", date_of_diagnosis="2022-12-12")
dig2 = diagnosis(diagnosis_id="", diagnosis_name="stomachache", date_of_diagnosis="2022-07-12")
dig.editDiagnosis("testing", "2022-10-17")
dig.set_diagnosis_name("tst")
dig.set_date_of_diagnosis("2022-12-13")
dig.deleteDiagnosis()
dig2.deleteDiagnosis()
print(dig.to_json())

prod = procedure_1(procedure_1_id="", procedure_1_name="x-ray", date_of_procedure_1="1999-08-15")
prod.editProcedure_1("heart surgery", "2012-08-15")
prod.set_procedure_1_name("brain surgery")
prod.set_date_of_procedure_1("2025-08-15")
prod.deleteProcedure_1()
print(prod.to_json())


"""

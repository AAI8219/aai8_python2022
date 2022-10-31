"""
imports
"""
import uuid
import json
import pymysql
import unittest
from flask import Flask
app = Flask(__name__)

class Config:
    """this is config class"""
    def __init__(self):
        self.db_conn = pymysql.connect(host="67.205.163.33",
                             user="aai8",
                             password="InfSci1500_4263658",
                             db="aai8",
                             charset="utf8mb4",
                             cursorclass=pymysql.cursors.DictCursor)
class Doctor:
    """this is doctor class"""
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
                    check_val = 'INSERT INTO doctor' \
                               '(doctor_id, first_name,' \
                               'last_name, title, speciality)'
                    check_val = check_val + ' VALUES(%s, %s, %s, %s, %s)'
                    print(check_val)
                    cur.execute(check_val, (self.__doctor_id,
                    self.__f_name,
                    self.__l_name,
                    self.__title,
                    self.__speciality))
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
    def edit_doctor(self, first_name = "", last_name = "", title = "", speciality = ""):
        """this is edit_doctor"""
        self.__f_name = first_name
        self.__l_name = last_name
        self.__title = title
        self.__speciality = speciality
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE doctor SET first_name = %s,' \
                       'last_name = %s,' \
                       'title = %s,' \
                       'speciality = %s' \
                       'WHERE doctor_id = %s;'
                print(qry)
                cur.execute(qry, (self.__f_name,
                            self.__l_name,
                            self.__title,
                            self.__speciality,
                            self.__doctor_id))
                con.commit()
        finally:
            con.close()
    def set_first_name(self, first_name=""):
        """this is set_first_name"""
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
        """this is set_last_name"""
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
        """this is set_title"""
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
        """this is set_speciality"""
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
        """this is get_doctor_id"""
        return self.__doctor_id

    def delete_doctor(self):
        """this is delete_doctor"""
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
        """this is to_json"""
        fields_data = {
            "id" : self.__doctor_id,
            "f_name" : self.__f_name,
            "l_name" : self.__l_name,
            "title" : self.__title,
            "speciality" : self.__speciality
        }
        return json.dumps(fields_data)



class Patient:
    """this is class patient"""
    def __init__(self, patient_id="",
                first_name = "",
                last_name = "",
                age = 0,
                birth_date = "",
                health_condition = ""):
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
                    check_val =  'INSERT INTO patient' \
                                '(patient_id, first_name,'\
                                'last_name, age,'\
                                'birth_date, health_condition)'
                    check_val = check_val + ' VALUES(%s, %s, %s, %s, %s, %s)'
                    print(check_val)
                    cur.execute(check_val, (self.__patient_id,
                                self.__f_name,
                                self.__l_name,
                                self.__age,
                                self.__birth_date,
                                self.__health_condition))
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
    def edit_patient(self, first_name = "", last_name = "",
                    age = 0,
                    birth_date = "",
                    health_condition = ""):
        """this is edit_patient"""
        self.__f_name = first_name
        self.__l_name = last_name
        self.__age = age
        self.__birth_date = birth_date
        self.__health_condition = health_condition
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE patient SET first_name = %s,' \
                        'last_name = %s,' \
                        'age = %s,' \
                        'birth_date = %s,' \
                        'health_condition = %s' \
                        'WHERE patient_id = %s;'
                print(qry)
                cur.execute(qry, (self.__f_name,
                            self.__l_name,
                            self.__age,
                            self.__birth_date,
                            self.__health_condition,
                            self.__patient_id))
                con.commit()
        finally:
            con.close()
    def set_first_name(self, first_name=""):
        """this is set_first_name"""
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
        """this is set_last_name"""
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
        """this is set_age"""
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
        """this is set_birth_date"""
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
        """this is set_health_condition"""
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
        """this is get_patient_id"""
        return self.__patient_id

    def delete_patient(self):
        """this is delete_patient"""
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
        """this is to_json(self)"""
        fields_data = {
            "id" : self.__patient_id,
            "f_name" : self.__f_name,
            "l_name" : self.__l_name,
            "age" : self.__age,
            "birth_date" : self.__birth_date,
            "health_condition" : self.__health_condition
        }
        return json.dumps(fields_data)



class Visit():
    """this is visit class"""
    def __init__(self, visit_id="",
                doctor_id="",
                patient_id = "",
                date_of_visit = "",
                visit_location_street_address = "",
                visit_location_city = "",
                visit_location_state = "",
                visit_location_zip = ""):
        self.__doctor_id = doctor_id
        self.__patient_id = patient_id
        self.__date_of_visit = date_of_visit
        self.__visit_location_street_address = visit_location_street_address
        self.__visit_location_city = visit_location_city
        self.__visit_location_state = visit_location_state
        self.__visit_location_zip = visit_location_zip
        if visit_id == "":
            self.__visit_id = str(uuid.uuid4())
            """this is self visit id"""
            try:
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    check_val = 'INSERT INTO visit' \
                                '(visit_id,' \
                                'doctor_id,' \
                                'patient_id,' \
                                'date_of_visit,' \
                                'visit_location_street_address,' \
                                'visit_location_city,' \
                                'visit_location_state,' \
                                'visit_location_zip)'
                    check_val = check_val + ' VALUES(%s, %s, %s, %s, %s, %s, %s, %s)'
                    print(check_val)
                    cur.execute(check_val, (self.__visit_id,
                                self.__doctor_id,
                                self.__patient_id,
                                self.__date_of_visit,
                                self.__visit_location_street_address,
                                self.__visit_location_city,
                                self.__visit_location_state,
                                self.__visit_location_zip))
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

    def edit_visit(self, date_of_visit = "",
                 visit_location_street_address = "",
                 visit_location_city = "",
                 visit_location_state = "",
                 visit_location_zip = ""):
        """this is edit_visit"""
        self.__date_of_visit = date_of_visit
        self.__visit_location_street_address = visit_location_street_address
        self.__visit_location_city = visit_location_city
        self.__visit_location_state = visit_location_state
        self.__visit_location_zip = visit_location_zip
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE visit SET date_of_visit = %s,'\
                    'visit_location_street_address = %s,' \
                    'visit_location_city = %s,' \
                    'visit_location_state = %s,' \
                    'visit_location_zip = %s' \
                    'WHERE visit_id = %s;'
                print(qry)
                cur.execute(qry, (self.__date_of_visit,
                            self.__visit_location_street_address,
                            self.__visit_location_city,
                            self.__visit_location_state,
                            self.__visit_location_zip,
                            self.__visit_id))
                con.commit()
        finally:
            con.close()

    def set_date_of_visit(self, date_of_visit=""):
        """this is set_date_of_visit"""
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
        """this is set_visit_location_street_address"""
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
        """this is set_visit_location_city"""
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
        """this is set_visit_location_state"""
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
        """this is set_visit_location_zip"""
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
    def delete_visit(self):
        """this is def delete_visit(self)"""
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
        """this is to_json(self)"""
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


class Diagnosis:
    """this is diagnosis class"""
    def __init__(self, diagnosis_id="", diagnosis_name = "", date_of_diagnosis = ""):
        self.__diagnosis_name = diagnosis_name
        self.__date_of_diagnosis = date_of_diagnosis
        if diagnosis_id == "":
            self.__diagnosis_id = str(uuid.uuid4())
            try:
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    check_val = 'INSERT INTO diagnosis' \
                                '(diagnosis_id, diagnosis_name, date_of_diagnosis)'
                    check_val = check_val + ' VALUES(%s, %s, %s)'
                    print(check_val)
                    cur.execute(check_val, (self.__diagnosis_id,
                                self.__diagnosis_name,
                                self.__date_of_diagnosis))
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


    def edit_diagnosis(self, diagnosis_name = "", date_of_diagnosis = ""):
        """this is def edit_diagnosis"""
        self.__diagnosis_name = diagnosis_name
        self.__date_of_diagnosis = date_of_diagnosis
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE diagnosis SET diagnosis_name = %s,' \
                        'date_of_diagnosis = %s' \
                        'WHERE diagnosis_id = %s;'
                print(qry)
                cur.execute(qry, (self.__diagnosis_name,
                            self.__date_of_diagnosis,
                            self.__diagnosis_id))
                con.commit()
        finally:
            con.close()

    def set_diagnosis_name(self, diagnosis_name=""):
        """this is def set_diagnosis_name"""
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
        """this is def set_date_of_diagnosis"""
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
    def delete_diagnosis(self):
        """this is def delete_diagnosis(self)"""
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
        """this is def to_json(self)"""
        fields_data = {
            "id" : self.__diagnosis_id,
            "diagnosis_name" : self.__diagnosis_name,
            "date_of_diagnosis" : self.__date_of_diagnosis
        }
        return json.dumps(fields_data)

class ProcedureOne:
    """this is procedure class"""
    def __init__(self, procedure_1_id="", procedure_1_name = "", date_of_procedure_1 = ""):
        self.__procedure_1_name = procedure_1_name
        self.__date_of_procedure_1 = date_of_procedure_1
        if procedure_1_id == "":
            self.__procedure_1_id = str(uuid.uuid4())
            try:
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    check_val = 'INSERT INTO procedure_1' \
                            '(procedure_1_id, procedure_1_name,' \
                            'date_of_procedure_1)'
                    check_val = check_val + ' VALUES(%s, %s, %s)'
                    print(check_val)
                    cur.execute(check_val, (self.__procedure_1_id,
                                self.__procedure_1_name,
                                self.__date_of_procedure_1))
                    con.commit()
            finally:
                con.close()
        else:
            self.__procedure_1_id = procedure_1_id
            try:
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry ="SELECT * FROM procedure_1 WHERE procedure_1_id = '" + procedure_1_id + "'"
                    print(qry)
                    cur.execute(qry)
                    rows = cur.fetchall()
                    for row in rows:
                        self.__procedure_1_id = row["procedure_1_id"]
                        self.__procedure_1_name = row["procedure_1_name"]
                        self.__date_of_procedure_1 = row["date_of_procedure_1"]
            finally:
                con.close()
    def edit_procedure_one(self, procedure_1_name = "", date_of_procedure_1 = ""):
        """this is edit_procedure_one"""
        self.__procedure_1_name = procedure_1_name
        self.__date_of_procedure_1 = date_of_procedure_1
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE procedure_1 SET procedure_1_name = %s,' \
                        'date_of_procedure_1 = %s,' \
                        'WHERE procedure_1_id = %s;'
                print(qry)
                cur.execute(qry, (self.__procedure_1_name,
                self.__date_of_procedure_1,
                self.__procedure_1_id))
                con.commit()
        finally:
            con.close()
    def set_procedure_1_name(self, procedure_1_name=""):
        """this is set_procedure_1_name"""
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
        """this is set_date_of_procedure_1"""
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
    def delete_procedure_one(self):
        """this is delete_procedure_one(self)"""
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
        """this is to_json(self)"""
        fields_data = {
            "id" : self.__procedure_1_id,
            "procedure_1_name" : self.__procedure_1_name,
            "date_of_procedure_1" : self.__date_of_procedure_1
        }
        return json.dumps(fields_data)

class TestCreateNewDoctorEntry(unittest.TestCase):
    # Testing if we can add a new doctor entry
    def runTest(self):
        doc = Doctor(doctor_id="",
                    first_name = "Aasri",
                    last_name = "Inu",
                    title = "Dentist",
                    speciality = "Pod")
        test_check = doc.to_json()
        self.assertIsNone(test_check, "Value is not None. Therefore it exists.")

class TestDeleteDoctorEntry(unittest.TestCase):
    # Testing if we can delete a doctor entry
    def runTest(self):
        doc = Doctor(doctor_id="",
                    first_name = "Aasritha",
                    last_name = "Inug",
                    title = "Surgeon",
                    speciality = "Brain")
        doc.delete_doctor()
        doc_json = doc.to_json()
        dict_doctor = json.loads(doc_json)
        self.assertIsNotNone(dict_doctor["f_name"], "Is None because no longer exists.")

class TestEditDoctorEntry(unittest.TestCase):
    # Testing if we can edit a doctor entry
    def runTest(self):
        doc = Doctor(doctor_id="",
                    first_name = "Aasritha",
                    last_name = "Inug",
                    title = "Surgeon",
                    speciality = "Heart")
        doc.edit_doctor("Leela", "Inu", "Surgeon", "Cardio")
        doc_json = doc.to_json()
        dict_doctor = json.loads(doc_json)
        self.assertEqual(dict_doctor["f_name"], "Leela") #equals.

class TestUpdateDoctorEntry(unittest.TestCase):
    # Testing if we can update a single doctor's instance variable like the title for example.
    def runTest(self):
        doc = Doctor(doctor_id="",
                    first_name = "Aasritha",
                    last_name = "Inug",
                    title = "Surgeon",
                    speciality = "Lung")
        doc.set_title("Psychologist")
        doc_json = doc.to_json()
        dict_doctor = json.loads(doc_json)
        self.assertEqual(dict_doctor["title"], "Psychologist") #equals.

# run the test
if __name__ == '__main__':
    unittest.main()

@app.route('/')
def index():
    pat = Patient(patient_id="", first_name="Jane", last_name="Smith", age=32, birth_date="2022-07-19", health_condition="headache")
    doc = Doctor(doctor_id="", first_name = "Jon", last_name = "Snow", title = "Doctor", speciality = "Pediatric")
    doc_id = doc.get_doctor_id()
    pat_id = pat.get_patient_id()
    vis = Visit(visit_id="",
                doctor_id= doc_id,
                patient_id= pat_id,
                date_of_visit="2022-08-15",
                visit_location_street_address="1234 Franklin Drive",
                visit_location_city="Pittsburgh",
                visit_location_state="PA",
                visit_location_zip="12345")
    
    vis_two = Visit(visit_id="",
                doctor_id= doc_id,
                patient_id= pat_id,
                date_of_visit="2022-08-30",
                visit_location_street_address="1234 Jefferson Drive",
                visit_location_city="Pittsburgh",
                visit_location_state="PA",
                visit_location_zip="54321")
    
    return vis.to_json() + "" + vis_two.to_json()
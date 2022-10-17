use aai8;

SET foreign_key_checks=0;
DROP TABLE IF EXISTS doctor CASCADE;
DROP TABLE IF EXISTS patient;
DROP TABLE IF EXISTS visit;
DROP TABLE IF EXISTS diagnosis;
DROP TABLE IF EXISTS procedure_1;
DROP TABLE IF EXISTS visit_procedure CASCADE; 
DROP TABLE IF EXISTS visit_diagnosis CASCADE; 
SET foreign_key_checks=1;

CREATE TABLE doctor(
doctor_id VARCHAR(36) NOT NULL,
PRIMARY KEY (doctor_id),
first_name VARCHAR(100) NOT NULL,
last_name VARCHAR(100) NOT NULL,
title VARCHAR(100) NOT NULL,
speciality VARCHAR(100) NOT NULL
);

CREATE TABLE patient(
patient_id VARCHAR(36) NOT NULL,
PRIMARY KEY (patient_id),
first_name VARCHAR(100) NOT NULL,
last_name VARCHAR(100) NOT NULL,
age INT NOT NULL,
birth_date DATETIME NOT NULL,
health_condition VARCHAR(1000) NOT NULL
);

CREATE TABLE visit(
visit_id VARCHAR(36) NOT NULL,
doctor_id VARCHAR(36) NOT NULL,
patient_id VARCHAR(36) NOT NULL,
PRIMARY KEY (visit_id),
FOREIGN KEY (doctor_id) REFERENCES doctor(doctor_id),
FOREIGN KEY (patient_id) REFERENCES patient(patient_id),
date_of_visit DATE NOT NULL,
visit_location_street_address VARCHAR(150) NOT NULL, 
visit_location_city VARCHAR(100) NOT NULL,
visit_location_state CHAR(2) NOT NULL,
visit_location_zip VARCHAR(5) NOT NULL
);


CREATE TABLE diagnosis(
diagnosis_id VARCHAR(36) NOT NULL,
PRIMARY KEY (diagnosis_id),
diagnosis_name VARCHAR(200) NOT NULL,
date_of_diagnosis DATE NOT NULL
);

CREATE TABLE procedure_1(
procedure_1_id VARCHAR(36) NOT NULL,
PRIMARY KEY (procedure_1_id),
procedure_1_name VARCHAR(100) NOT NULL,
date_of_procedure_1 DATE NOT NULL
);

CREATE TABLE visit_procedure(
visit_procedure_id VARCHAR(36) NOT NULL,
visit_id VARCHAR(36) NOT NULL,
FOREIGN KEY (visit_id) REFERENCES visit(visit_id),
procedure_1_id VARCHAR(36) NOT NULL,
FOREIGN KEY (procedure_1_id) REFERENCES procedure_1(procedure_1_id)
);

CREATE TABLE visit_diagnosis(
visit_diagnosis_id VARCHAR(36) NOT NULL,
visit_id VARCHAR(36) NOT NULL,
FOREIGN KEY (visit_id) REFERENCES visit(visit_id),
diagnosis_id VARCHAR(36) NOT NULL,
FOREIGN KEY (diagnosis_id) REFERENCES diagnosis(diagnosis_id)
);



select * from doctor;
select * from patient;
select * from visit;
select * from diagnosis;
select * from procedure_1;
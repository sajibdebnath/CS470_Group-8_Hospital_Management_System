-- ============================
-- CREATE HOSPITAL SYSTEM TABLES
-- ============================

-- PATIENT TABLE
CREATE TABLE Patient (
    pno NUMBER PRIMARY KEY,
    pname VARCHAR2(50) NOT NULL,
    pgender VARCHAR2(10) NOT NULL,
    page NUMBER NOT NULL,
    pward VARCHAR2(20) NOT NULL,
    pstatus VARCHAR2(20),
    room_no NUMBER, -- FK to Room
    dept_id NUMBER,       -- FK to Department
    CONSTRAINT fk_patient_room FOREIGN KEY (room_no) REFERENCES Room(room_no),
    CONSTRAINT fk_patient_dept FOREIGN KEY (dept_id) REFERENCES Department(dept_id)
);

-- DOCTOR TABLE
CREATE TABLE Doctor (
    dno NUMBER PRIMARY KEY,
    dname VARCHAR2(50) NOT NULL,
    specialization VARCHAR2(50) NOT NULL,
    contact VARCHAR2(20),
    dept_id NUMBER, -- FK to Department
    CONSTRAINT fk_doctor_dept FOREIGN KEY (dept_id) REFERENCES Department(dept_id)
);

-- DEPARTMENT TABLE
CREATE TABLE Department (
    dept_id NUMBER PRIMARY KEY,
    dept_name VARCHAR2(50) NOT NULL,
    floor VARCHAR2(20),
    head VARCHAR2(50)
);

-- ROOM TABLE
CREATE TABLE Room (
    room_no NUMBER PRIMARY KEY,
    room_type VARCHAR2(20) NOT NULL,
    is_occupied VARCHAR2(5)
);

-- BILLING TABLE
CREATE TABLE Billing (
    bill_id NUMBER PRIMARY KEY,
    pno NUMBER NOT NULL,
    amount NUMBER(10, 2) NOT NULL,
    payment_method VARCHAR2(20),
    paid_status VARCHAR2(10),
    CONSTRAINT fk_billing_patient FOREIGN KEY (pno) REFERENCES Patient(pno)
);

-- APPOINTMENT TABLE
CREATE TABLE Appointment (
    appt_id NUMBER PRIMARY KEY,
    pno NUMBER NOT NULL,
    dno NUMBER NOT NULL,
    appt_date DATE NOT NULL,
    appt_time VARCHAR2(20) NOT NULL,
    CONSTRAINT fk_appt_patient FOREIGN KEY (pno) REFERENCES Patient(pno),
    CONSTRAINT fk_appt_doctor FOREIGN KEY (dno) REFERENCES Doctor(dno)
);

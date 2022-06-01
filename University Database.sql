-- ****************************
-- Created a relational database designed to hold information relating to Students, Student Courses and Instructors who tutor students



-- ****************************
-- Part A
-- ****************************
-- Create new database, schooldb; drop database if schooldb already exists before new database is created


USE Master;
GO
DROP DATABASE IF EXISTS schooldb;
GO
CREATE DATABASE schooldb;
GO
USE schooldb;
PRINT 'Part A Completed'



-- ****************************
-- Part B
-- ****************************
-- Create procedure, usp_dropTables, that clears database if tables already exist; drops procedure if exists


DROP PROCEDURE IF EXISTS usp_dropTables;


GO


CREATE PROCEDURE usp_dropTables
AS
BEGIN
  DROP TABLE IF EXISTS dbo.StudentContacts;
  DROP TABLE IF EXISTS dbo.ContactType;
  DROP TABLE IF EXISTS dbo.Employees;
  DROP TABLE IF EXISTS dbo.EmpJobPosition;
  DROP TABLE IF EXISTS dbo.Student_Courses;
  DROP TABLE IF EXISTS dbo.CourseList;
  DROP TABLE IF EXISTS dbo.StudentInformation;
        
PRINT 'Part B Completed'
END;
GO


EXEC usp_dropTables;


GO



-- ****************************
-- Part C
-- ****************************
-- Create tables for schooldb ERD


CREATE TABLE StudentInformation
	(
	StudentID         INTEGER         NOT NULL        IDENTITY(100,1)       PRIMARY KEY,
	Title             CHAR(50)        NULL,
  FirstName         CHAR(50)        NOT NULL,
  LastName          CHAR(50)        NOT NULL,
  Address1          CHAR(50)        NULL,
  Address2          CHAR(50)        NULL,
  City              CHAR(50)        NULL,
  County            CHAR(100)       NULL,
  Zip               CHAR(5)         NULL,
  Country           CHAR(75)        NULL,        
  Telephone         CHAR(30)        NULL,
  Email             VARCHAR(75)     NULL,
  Enrolled          CHAR(50)        NULL,
  AltTelephone      CHAR(30)        NULL
  );
GO
CREATE TABLE CourseList
  (
  CourseID              INTEGER       NOT NULL      IDENTITY(10,1)      PRIMARY KEY,
  CourseDescription     CHAR(50)      NOT NULL,
  CourseCost            Money         NULL,
  CourseDurrationYears  TINYINT       NULL,
  Notes                 CHAR(255)     NULL
  );
GO
CREATE TABLE Student_Courses
  (
  StudentCourseID     INTEGER     NOT NULL      IDENTITY(1,1)         PRIMARY KEY,
	StudentID           INTEGER     NOT NULL                            FOREIGN KEY REFERENCES StudentInformation(StudentID),
	CourseID            INTEGER     NOT NULL                            FOREIGN KEY REFERENCES CourseList(CourseID),
	CourseStartDate     DATE        NOT NULL,
	CourseComplete      CHAR(50)    NULL
  );
GO
CREATE TABLE EmpJobPosition
  (
  EmpJobPositionID    INTEGER			NOT NULL      IDENTITY(1,1)         PRIMARY KEY,
  EmployeePosition    CHAR(50)		NOT NULL
  );
GO
CREATE TABLE Employees
  (
  EmployeeID          INTEGER			NOT NULL      IDENTITY(1000,1)	    PRIMARY KEY,
  EmployeeName        CHAR(100)		NOT NULL,
  EmployeePositionID  INTEGER			NOT NULL                            FOREIGN KEY REFERENCES EmpJobPosition(EmpJobPositionID),
  EmployeePassword    CHAR(255)   NULL,
  Access              CHAR(255)		NULL
  );
GO
CREATE TABLE ContactType
  (
  ContactTypeID       INTEGER     NOT NULL      IDENTITY(1,1)         PRIMARY KEY,
  ContactType         CHAR(50)		NULL
  );
GO
CREATE TABLE StudentContacts
  (
  ContactID           INTEGER     NOT NULL      IDENTITY(10000,1)     PRIMARY KEY,
  StudentID           INTEGER     NOT NULL                            FOREIGN KEY REFERENCES StudentInformation(StudentID),
  ContactTypeID       INTEGER     NOT NULL                            FOREIGN KEY REFERENCES ContactType(ContactTypeID),
  ContactDate		      DATE        NOT NULL,
  EmployeeID		      INTEGER     NOT NULL                            FOREIGN KEY REFERENCES Employees(EmployeeID),
  ContactDetails		  CHAR(50)    NOT NULL
  );
GO


PRINT 'Part C Completed';


GO



-- ****************************
-- Part D
-- ****************************
-- Columns, constraintings and indexes for schooldb


-- Constraint prevents duplicate reccords in Student_Courses table

ALTER TABLE Student_Courses ADD CONSTRAINT Student_Course_ID UNIQUE (StudentID, CourseID);
GO


-- Timestamp records in StudentInformation table

ALTER TABLE StudentInformation
ADD CreatedDateTime DATETIME DEFAULT CURRENT_TIMESTAMP;
GO


-- Remove AltTelephone column from StudentInformation table

ALTER TABLE StudentInformation
DROP COLUMN AltTelephone;
GO

-- Create index based on last names in StudentInformation table

CREATE INDEX IX_LastName
ON StudentInformation(LastName);
GO


PRINT 'Part D Completed';


GO



-- ****************************
-- Part E
-- ****************************
-- Create trigger, trg_assignEmail, which generates a new student email if an email is not specified; drop trigger if exists
-- Auto-generated Email Format: firstName.lastName@disney.com


DROP TRIGGER IF EXISTS trg_assignEmail;


GO


CREATE TRIGGER trg_assignEmail ON StudentInformation
INSTEAD OF INSERT
AS
	INSERT INTO StudentInformation(FirstName, LastName, Email)
	SELECT TRIM(FirstName), TRIM(LastName), COALESCE(Email, FirstName + '.' + LastName + '@disney.com')
	FROM INSERTED;
GO


PRINT 'Part E Completed';



-- ****************************
-- Part F
-- ****************************
-- DATA Population


INSERT INTO StudentInformation
	(FirstName,LastName)
VALUES
	('Mickey', 'Mouse');


INSERT INTO StudentInformation
	(FirstName,LastName)
VALUES
	('Minnie', 'Mouse');


INSERT INTO StudentInformation
	(FirstName,LastName)
VALUES
	('Donald', 'Duck');


SELECT * FROM StudentInformation;


INSERT INTO CourseList
	(CourseDescription)
VALUES
	('Advanced Math');


INSERT INTO CourseList
	(CourseDescription)
VALUES
	('Intermediate Math');


INSERT INTO CourseList
	(CourseDescription)
VALUES
	('Beginning Computer Science');


INSERT INTO CourseList
	(CourseDescription)
VALUES
	('Advanced Computer Science');


SELECT * from CourseList;


INSERT INTO Student_Courses
	(StudentID,CourseID,CourseStartDate)
VALUES
	(100, 10, '01/05/2018');


INSERT INTO Student_Courses
	(StudentID,CourseID,CourseStartDate)
VALUES
	(101, 11, '01/05/2018');


INSERT INTO Student_Courses
	(StudentID,CourseID,CourseStartDate)
VALUES
	(102, 11, '01/05/2018');
INSERT INTO Student_Courses
	(StudentID,CourseID,CourseStartDate)
VALUES
	(100, 11, '01/05/2018');


INSERT INTO Student_Courses
	(StudentID,CourseID,CourseStartDate)
VALUES
	(102, 13, '01/05/2018');


SELECT * from Student_Courses;


INSERT INTO EmpJobPosition
	(EmployeePosition)
VALUES
	('Math Instructor');


INSERT INTO EmpJobPosition
	(EmployeePosition)
VALUES
	('Computer Science');


SELECT * from EmpJobPosition


INSERT INTO Employees
	(EmployeeName,EmployeePositionID)
VALUES
	('Walt Disney', 1);


INSERT INTO Employees
	(EmployeeName,EmployeePositionID)
VALUES
	('John Lasseter', 2);


INSERT INTO Employees
	(EmployeeName,EmployeePositionID)
VALUES
	('Danny Hillis', 2);


SELECT * from Employees;


INSERT INTO ContactType
	(ContactType)
VALUES
	('Tutor');


INSERT INTO ContactType
	(ContactType)
VALUES
	('Homework Support');


INSERT INTO ContactType
	(ContactType)
VALUES
	('Conference');


SELECT * from ContactType;


INSERT INTO StudentContacts
	(StudentID,ContactTypeID,EmployeeID,ContactDate,ContactDetails)
VALUES
	(100, 1, 1000, '11/15/2017', 'Micky and Walt Math Tutoring');


INSERT INTO StudentContacts
	(StudentID,ContactTypeID,EmployeeID,ContactDate,ContactDetails)
VALUES
	(101, 2, 1001, '11/18/2017', 'Minnie and John Homework support');


INSERT INTO StudentContacts
	(StudentID,ContactTypeID,EmployeeID,ContactDate,ContactDetails)
VALUES
	(100, 3, 1001, '11/18/2017', 'Micky and Walt Conference');


INSERT INTO StudentContacts
	(StudentID,ContactTypeID,EmployeeID,ContactDate,ContactDetails)
VALUES
	(102, 2, 1002, '11/20/2017', 'Donald and Danny Homework support');


SELECT * from StudentContacts;


INSERT INTO StudentInformation
	(FirstName,LastName,Email)
VALUES
	('Porky', 'Pig', 'porky.pig@warnerbros.com');


INSERT INTO StudentInformation
	(FirstName,LastName)
VALUES
	('Snow', 'White');


PRINT 'Part F Completed';



-- ****************************
-- Part G
-- ****************************
-- Create stored procedure, usp_addQuickContacts, which records activity log for meetings between students and instructors


GO


DROP PROCEDURE IF EXISTS usp_addQuickContacts;


GO
CREATE PROCEDURE usp_addQuickContacts
	(
	@StudentEmail VARCHAR(75),
	@EmployeeName VARCHAR(50),
	@contactDetails VARCHAR(50),
	@contactType VARCHAR(30)
	)
AS
BEGIN
	BEGIN
		IF NOT EXISTS (SELECT 1 FROM ContactType WHERE ContactType = @contactType)
		INSERT INTO ContactType(ContactType) VALUES(@contactType)
	END;
	BEGIN
		INSERT INTO StudentContacts(StudentID,EmployeeID, ContactDetails, ContactTypeID)
		VALUES
		(		
		(SELECT studentID from StudentInformation where Email = @StudentEmail),
		(SELECT EmployeeID FROM Employees WHERE EmployeeName = @EmployeeName), 
		(SELECT ContactDetails FROM StudentContacts WHERE ContactDetails = @contactDetails), 
		(SELECT ContactTypeID FROM ContactType WHERE ContactType = @contactType)
		)
	END;
END;


PRINT 'Part G Completed';


GO



-- ****************************
-- PART H
-- ****************************
-- Create stored procedure, usp_getCourseRosterByName, which returns names of all student's enrolled in the course specified


DROP PROCEDURE IF EXISTS usp_getCourseRosterByName;


GO


CREATE PROCEDURE usp_getCourseRosterByName(@courseDesc CHAR(50))
AS
BEGIN
	SELECT C.CourseDescription, S.FirstName, S.LastName
	FROM StudentInformation S INNER JOIN Student_Courses SC on S.StudentID = SC.StudentID
		INNER JOIN CourseList C on SC.CourseID = C.CourseID
	WHERE C.CourseDescription = @courseDesc
END;


PRINT 'Part H Completed';


GO



-- ****************************
-- Part I
-- ****************************
/*Create view, vtutorContacts, which returns results from StudentContacts and displays EmployeeName, StudentName, ContactDetails, and ContactDate fields
for all tutor contacts*/ 


DROP VIEW IF EXISTS vtutorContacts;


GO


CREATE VIEW vtutorContacts
AS
	SELECT E.EmployeeName, (TRIM(S.FirstName) + ' ' + TRIM(S.LastName))
		AS StudentName, SC.ContactDetails, SC.ContactDate
	FROM Employees E INNER JOIN StudentContacts SC on E.EmployeeID = SC.EmployeeID
		INNER JOIN StudentInformation S on S.StudentID = SC.StudentID
		INNER JOIN ContactType CT ON SC.ContactTypeID = CT.ContactTypeID
	WHERE CT.ContactType = 'Tutor';
GO


SELECT * FROM vtutorContacts;


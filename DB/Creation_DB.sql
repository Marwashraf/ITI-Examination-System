+-------------Address
CREATE TABLE Address (
    Address_ID int IDENTITY(1,1) NOT NULL PRIMARY KEY,
    City varchar(50) NOT NULL
);

-----------------Branch
CREATE TABLE Branch(
	B_ID int IDENTITY(1,1) NOT NULL Primary Key,
	B_Name varchar(100) NULL,
	Address_ID int NULL,
)


-----------------Certificate
CREATE TABLE Certificate (
    Credintial_URL varchar(200) NOT NULL PRIMARY KEY,
    Ct_Name varchar(50) NULL,
    Description varchar(200) NULL,
    Hours int NULL,
	St_ID int NULL,
    Ct_ID int IDENTITY(1,1) NOT NULL,
    FOREIGN KEY (St_ID) REFERENCES Student (St_ID)
);

-------------------Company
CREATE TABLE Company(
	Company_ID int IDENTITY(1,1) NOT NULL primary key,
	Company_Name varchar(100) NOT NULL,
	Launch_Date date NOT NULL,
	Company_Filed varchar(100) NOT NULL,
	Address_ID int NOT NULL,
	FOREIGN KEY(Address_ID)REFERENCES Address (Address_ID)
)

----------------------Courses
CREATE TABLE Courses(
	Cr_ID  int IDENTITY(1,1) NOT NULL Primary key ,
	Cr_Name varchar (100) NULL,
	Topic_ID int NOT NULL,
FOREIGN KEY(Topic_ID)REFERENCES Topic (Topic_ID)
)

-------------------------------Deal
CREATE TABLE Deal(
	Branch_ID int NOT NULL,
	Company_ID int NOT NULL,
	D_SDate date NULL,
	D_EDate date NULL,
	PRIMARY KEY (Branch_ID, Company_ID),
	FOREIGN KEY(Branch_ID)REFERENCES Branch (B_ID),
	FOREIGN KEY(Company_ID)REFERENCES Company (Company_ID)
 )

-------------------------------------------Department
CREATE TABLE Department(
	Dept_ID int IDENTITY(1,1) NOT NULL Primary Key,
	Dept_Name varchar(100) NULL,
	Manger int NOT NULL,
 FOREIGN KEY(Manger)REFERENCES Instructor (Ins_ID)
)

------------------------------Evaluation_P_Student

CREATE TABLE Evaluation_P_Student (
    St_ID int NOT NULL,
    Evaluation_P_ID int NOT NULL,
    Score int NULL,
    Grade varchar(50) NULL,
	PRIMARY KEY (St_ID, Evaluation_P_ID),
    FOREIGN KEY (St_ID) REFERENCES Student (St_ID),
    FOREIGN KEY (Evaluation_P_ID) REFERENCES Evaluation_Projects (Proj_ID)
);


-----------------------------------------Evaluation Projects
CREATE TABLE Evaluation_Projects(
	Proj_ID int IDENTITY(1,1) NOT NULL primary key,
	Pro_Name varchar(100) NULL,
	Min_Mark int NULL,
	Full_Mark int NULL,
	Cr_ID int NOT NULL,
 FOREIGN KEY(Cr_ID) REFERENCES Courses (Cr_ID)
)

-------------------------------------------------------Exam
CREATE TABLE Exam (
    Exam_ID int IDENTITY(1,1) NOT NULL PRIMARY KEY,
    Duration int NULL,
    No_Q int NULL,
    [Date] date NULL,
    Min_Mark int NULL,
    Full_Mark int NULL,
    Crs_ID int NOT NULL,
    St_ID int NOT NULL,
    FOREIGN KEY (Crs_ID) REFERENCES Course (Cr_ID),
    FOREIGN KEY (St_ID) REFERENCES Student (St_ID)
);

---------------------------------------Freelance
CREATE TABLE Freelance (
    Fr_ID int IDENTITY(1,1) NOT NULL PRIMARY KEY,
    Description varchar(200) NULL,
    Cost int NULL,
    Duration int NULL,
    St_Account varchar(200) NULL,
    Client_Name varchar(200) NULL,
    Client_Number varchar(50) NULL,
    St_ID int NULL,
    FOREIGN KEY (St_ID) REFERENCES Student (St_ID)
);

---------------------------------------------Graduation_Project

CREATE TABLE Graduation_Project(
	Project_ID int IDENTITY(1,1) NOT NULL Primary key,
	Pro_Name varchar(100) NULL,
	MinMarktoPass int NULL,
	FullMark int NULL,
	Track_ID int NULL,
	FOREIGN KEY(Track_ID)REFERENCES Track (T_ID)
 )

 -----------------------------------------------Graduation Team
 CREATE TABLE Graduation_Team(
	Team_ID int IDENTITY(1,1) NOT NULL Primary Key,
	Score int NULL,
	Grade varchar(100) NULL,
	P_SDate date NULL,
	P_EDate date NULL,
	Proj_ID int NOT NULL,
	FOREIGN KEY(Proj_ID) REFERENCES Graduation_Project (Project_ID)
	)


-----------------------------------------Instructor
CREATE TABLE Instructor(
	Ins_ID int IDENTITY(1,1) NOT NULL Primary Key,
	Ins_SSN varchar(50) NULL,
	First_Name varchar(500) NOT NULL,
	Last_Name varchar(500) NOT NULL,
	Salary int NOT NULL,
	Ins_Email varchar(50) NOT NULL,
	Password varchar(50) NULL,
	Phone varchar(50) NOT NULL,
	Dept_ID int NOT NULL,
	Address_ID int NOT NULL,
	Job_Type varchar(100) NOT NULL,
	FOREIGN KEY(Address_ID)REFERENCES Address (Address_ID)
	)

-------------------------------------Instructor Assign
CREATE TABLE Instructor_Assign(
	Program_ID int NOT NULL,
	Branch_ID int NOT NULL,
	Dept_ID int NOT NULL,
	[Track_ID] int NOT NULL,
	Course_ID int NOT NULL,
	Ins_ID int NOT NULL,
	Intake int NOT NULL,
	Course_SData date NOT NULL,
	Course_EDate date NOT NULL,
	PRIMARY KEY(Program_ID,Branch_ID,Dept_ID,Track_ID,Course_ID,Ins_ID,Intake),
	FOREIGN KEY(Branch_ID)REFERENCES Branch (B_ID),
	FOREIGN KEY(Course_ID)REFERENCES Courses (Cr_ID),
	FOREIGN KEY(Dept_ID)REFERENCES Department (Dept_ID),
	FOREIGN KEY(Ins_ID)REFERENCES Instructor (Ins_ID),
	FOREIGN KEY(Program_ID)REFERENCES Program (P_ID),
	FOREIGN KEY(Track_ID)REFERENCES Track (T_ID)
 )

------------------------------------Intakes
CREATE TABLE Intakes(
	Intake int NOT NULL Primary Key,
	Start_Date date NULL,
	End_Date date NULL,
)

---------------------------------------Job
CREATE TABLE Job(
	Job_ID int IDENTITY(1,1) NOT NULL Primary Key,
	Job_Title varchar(50) NULL,
	Salary int NULL,
	Hiring_Date date NULL,
	Company_Name varchar(100) NULL,
	Job_Type varchar(50) NULL,
	St_ID int NOT NULL,
 FOREIGN KEY(St_ID)REFERENCES Student (St_ID)
 )

 ----------------------------------------------Program
 CREATE TABLE Program(
	P_ID int IDENTITY(1,1) NOT NULL Primary key,
	P_Name varchar(100) NULL,
	P_Duration int NULL,
 )

 -----------------------------------------------Questions
 
CREATE TABLE Questions(
	Q_ID int IDENTITY(1,1) NOT NULL primary Key,
	Question_Type varchar(50) NULL,
	Question varchar(1000) NULL,
	Choice_1 varchar(500) NULL,
	Choice_2 varchar(500) NULL,
	Choice_3 varchar(500) NULL,
	Choice_4 varchar(500) NULL,
	Correct_Choice varchar(500) NULL,
	Crs_ID int NOT NULL,
	FOREIGN KEY(Crs_ID)REFERENCES Courses (Cr_ID)
)

-------------------------------------------------St_Enrollment
CREATE TABLE St_Enrollment(
	Program_ID int NOT NULL,
	Branch_ID int NOT NULL,
	Dept_ID int NOT NULL,
	Track_ID int NOT NULL,
	St_ID int NOT NULL,
	Intake int NOT NULL,
	Primary Key(Program_ID,Branch_ID,Dept_ID,Track_ID,St_ID,Intake),
	FOREIGN KEY(Branch_ID)REFERENCES Branch (B_ID),
	FOREIGN KEY(Dept_ID)REFERENCES Department (Dept_ID),
	FOREIGN KEY(Intake)REFERENCES Intakes (Intake),
	FOREIGN KEY(Program_ID)REFERENCES Program (P_ID),
	FOREIGN KEY(St_ID)REFERENCES Student (St_ID),
	FOREIGN KEY([Track_ID])REFERENCES [dbo].[Track] ([T_ID])

 )


 ------------------------------------Student
 
CREATE TABLE Student(
	St_ID int IDENTITY(1,1) NOT NULL Primary Key,
	St_SSN varchar(14) NOT NULL,
	First_Name varchar(100) NOT NULL,
	Last_Name varchar(100) NOT NULL,
	Graduation_Year int NOT NULL,
	Gender varchar(1) NOT NULL,
	Date_of_Birth date NOT NULL,
	St_Email varchar(50) NOT NULL,
	Password varchar(50) NULL,
	Phone varchar(20) NOT NULL,
	Address_ID int NOT NULL,
	Team_ID int NOT NULL,
	FOREIGN KEY(Address_ID)REFERENCES Address (Address_ID),
	FOREIGN KEY(Team_ID)REFERENCES Graduation_Team (Team_ID)
 )


 -----------------------------------------------Student To Exam
 CREATE TABLE Student_To_Exam(
	Exam_ID int NOT NULL,
	Q_ID int NOT NULL,
	St_Answer varchar(500) NULL,
	St_Degree int NULL,
	Exam_Date datetime NULL  DEFAULT (getdate()),
	Primary Key(Exam_ID,Q_ID),
 )

 -----------------------------------------------------Track
 CREATE TABLE Track(
	T_ID int IDENTITY(1,1) NOT NULL,
	T_Name varchar(100) NULL,
	Duration int NULL,
	Capacity int NULL,
	No_Courses int NULL,
 )


 --------------------------------------------------Topic
 CREATE TABLE Topic (
    Topic_ID int IDENTITY(1,1) NOT NULL PRIMARY KEY,
    Topic_Name varchar(100) NULL
);


---------------------------------------------------Track_Courses
CREATE TABLE Track_Courses(
	Cr_ID int NOT NULL,
	Track_ID int NOT NULL,
	Hours int NULL,
	Primary Key(Cr_ID,Track_ID),
	FOREIGN KEY(Cr_ID)REFERENCES Courses (Cr_ID),
	FOREIGN KEY(Track_ID)REFERENCES Track (T_ID)
)
----------------------------------------------------------------------------------------------------------------

CREATE TABLE Graduation_Project_Team_DIM(
	Team_ID int IDENTITY(1,1) NOT NULL Primary Key,
	Team_BK int NOT NULL,
	Project_BK int NOT NULL,
	Project varchar(100) NULL,
	Grade varchar(100) NULL,
	Graduation_Project_SDate date NULL,
	Graduation_Project_EDate date NULL,
	Min_Marks_ToPass int NULL,
	FullMark int NULL,
	Source_sys_code tinyint NULL,
	Last_modified_date date NULL DEFAULT (getdate()) 
)


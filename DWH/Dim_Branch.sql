

CREATE TABLE Branches_DIM(
	Branch_ID int IDENTITY(1,1) NOT NULL Primary key,
	Branch_BK int NOT NULL,
	B_City varchar(50) NULL,
	Department_BK int NOT NULL,
	Track_BK int NOT NULL,
	Program_BK int NOT NULL,
	Branch_Name varchar(100) NULL,
	Department_Name varchar(100) NULL,
	Track_Name varchar(100) NULL,
	Track_Capacity int NULL,
	Program_Name varchar(200) NULL,
	Intake int NULL,
	intake_SDate date NULL,
	Intake_EDate date NULL,
	Source_SYS_Code tinyint NULL,
	Last_Modified_Date date NULL DEFAULT (getdate()) 
)


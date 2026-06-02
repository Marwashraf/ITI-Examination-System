
CREATE TABLE Graduation_Fact(
	Graduation_Fact_ID int IDENTITY(1,1) NOT NULL Primary Key,
	Team_FK int NOT NULL,
	Branch_FK int NOT NULL,
	Graduation_Project_Score int NULL,
	Source_sys_code tinyint NULL,
	Created_AT date NULL DEFAULT (getdate()),
	FOREIGN KEY(Branch_FK)REFERENCES Branches_DIM (Branch_ID),
	FOREIGN KEY(Team_FK)REFERENCES Graduation_Project_Team_DIM (Team_ID)
 )

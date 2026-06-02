
CREATE TABLE Evaluation_Project_Fact(
	[Evaluation_Fact_ID] [int] IDENTITY(1,1) NOT NULL Primary Key,
	[Student_FK] [int] NOT NULL,
	[Branch_FK] [int] NOT NULL,
	[Course_FK] [int] NOT NULL,
	[Project_Score] [int] NULL,
	[Source_Sys_code] [tinyint] NULL,
	[Created_AT] [date] NULL DEFAULT (getdate()),
	FOREIGN KEY(Branch_FK)REFERENCES Branches_DIM (Branch_ID),
	FOREIGN KEY(Course_FK)REFERENCES Course_Dim (Course_ID),
	FOREIGN KEY(Student_FK)REFERENCES Student_DIM (Student_ID)
)

CREATE TABLE Examination_Fact(
	Examination_Fact_ID int IDENTITY(1,1) NOT NULL Primary Key,
	Student_FK int NOT NULL,
	Course_FK int NOT NULL,
	Instructor_FK int NOT NULL,
	Branch_FK int NOT NULL,
	Exam_FK int NOT NULL,
	Date_FK int NOT NULL,
	Exam_Degree int NULL,
	Source_sys_code int NULL,
	Created_AT date NULL DEFAULT (getdate()),
	FOREIGN KEY(Branch_FK)REFERENCES Branches_DIM (Branch_ID),
	FOREIGN KEY(Course_FK)REFERENCES Course_Dim (Course_ID),
	FOREIGN KEY(Date_FK)REFERENCES DimDate (DateSK),
	FOREIGN KEY(Exam_FK)REFERENCES Exam_DIM (Exam_id),
	FOREIGN KEY(Instructor_FK)REFERENCES Instractor_DIM (Instractor_ID),
	FOREIGN KEY(Student_FK)REFERENCES [Student_DIM] (Student_ID)
	)



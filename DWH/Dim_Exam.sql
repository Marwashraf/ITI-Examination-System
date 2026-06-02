
CREATE TABLE Exam_DIM(
	Exam_id int IDENTITY(1,1) NOT NULL Primary Key,
	Exam_BK int NOT NULL,
	Question_BK int NOT NULL,
	Duration int NULL,
	No_Questions int NULL,
	Date date NULL DEFAULT (getdate()),
	Min_Mark_To_Pass int NULL,
	Full_Mark int NULL,
	Question_Type varchar(50) NULL,
	Questions varchar(1000) NULL,
	Correct_Choice varchar(500) NULL,
	ST_Answers varchar(500) NULL,
	St_Degree int NULL,
	Source_sys_code tinyint NULL,
	Last_Modified_Date date NULL  DEFAULT (getdate()),
)
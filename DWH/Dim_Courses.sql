
CREATE TABLE Course_Dim(
	Course_ID int IDENTITY(1,1) NOT NULL Primary Key,
	Course_BK int NULL,
	Topic_BK int NULL,
	Evaluation_Project_BK int NULL,
	Course_Name varchar(200) NULL,
	Track_BK int NULL,
	Hours int NULL,
	Toipc_Name varchar(200) NULL,
	Evaluation_project_name varchar(200) NULL,
	Evalp_Min_Mark_ToPass int NULL,
	Evap_FullMark int NULL,
	Source_sys_code tinyint NULL,
	Last_Modified_Date date NULL DEFAULT (getdate())
 )

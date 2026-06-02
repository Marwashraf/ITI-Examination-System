
CREATE TABLE Instractor_DIM(
	Instractor_ID int IDENTITY(1,1) NOT NULL Primary Key,
	Instractor_BK int NOT NULL,
	first_name varchar(500) NULL,
	Last_name varchar(500) NULL,
	I_City varchar(50) NULL,
	Salary int NULL,
	Job_Type varchar(100) NULL,
	source_sys_code tinyint NULL,
	start_date datetime NULL,
	end_date datetime NULL,
	Last_Modified_date date NULL DEFAULT (getdate()),
	is_current int NULL,
)




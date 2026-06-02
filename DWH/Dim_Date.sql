

CREATE TABLE DimDate(
	DateSK int NOT NULL Primary Key,
	Date date NOT NULL,
	Day char(2) NOT NULL,
	DaySuffix varchar(4) NOT NULL,
	DayOfWeek varchar(9) NOT NULL,
	DOWInMonth tinyint NOT NULL,
	DayOfYear int NOT NULL,
	WeekOfYear tinyint NOT NULL,
	WeekOfMonth tinyint NOT NULL,
	Month char(2) NOT NULL,
	MonthName varchar(9) NOT NULL,
	Quarter tinyint NOT NULL,
	QuarterName varchar(6) NOT NULL,
	Year char(4) NOT NULL,
	StandardDate varchar(10) NULL,
	HolidayText varchar(50) NULL,
	FiscalDay char(2) NULL,
	FiscalMonth char(2) NULL,
	FiscalMonthName varchar(9) NULL,
	FiscalQuarter tinyint NULL,
	FiscalQuarterName varchar(6) NULL,
	FiscalYear char(4) NULL,
 )


Alter Procedure AddJob
	@Job_Title Varchar(50),@Salary INT,
	@Hiring_Date Date ,@Comapny_Name Varchar(100),
	@Job_Type Varchar(50),@St_ID INT
AS
Begin
	If Exists (Select 8 From Student Where St_ID=@St_ID)
	BeGIN
	Insert INTO Job
	Values(@Job_Title,@Salary,@Hiring_Date,@Comapny_Name,@Job_Type,@St_ID)
	Select 'Added Successfully' AS Message;
	ENd
	ELSE
		Select 'Enter Valid Student ID' As Message
END;

Execute AddJob 'gyuerilsig',20000,'2020-03-03','rtyguhijolsgoi','Full Time',3000;


Create PROCEDURE UpdateJob
    @Job_ID INT,
    @Job_Title VARCHAR(50) = NULL,
    @Salary INT = NULL,
    @Hiring_Date DATE = NULL,
    @Company_Name VARCHAR(100) = NULL,
    @Job_Type VARCHAR(50) = NULL,
    @St_ID INT = NULL
AS
BEGIN
    BEGIN TRY
        IF EXISTS (SELECT * FROM Job WHERE Job_ID = @Job_ID)
        BEGIN
            IF @St_ID IS NULL OR EXISTS (SELECT * FROM Student WHERE St_ID = @St_ID)
            BEGIN
                DECLARE @Old_Job_Title VARCHAR(50),
                        @Old_Salary INT,
                        @Old_Hiring_Date DATE,
                        @Old_Company_Name VARCHAR(100),
                        @Old_Job_Type VARCHAR(50);

                SELECT @Old_Job_Title = Job_Title,
                       @Old_Salary = Salary,
                       @Old_Hiring_Date = Hiring_Date,
                       @Old_Company_Name = Company_Name,
                       @Old_Job_Type = Job_Type
                FROM Job
                WHERE Job_ID = @Job_ID;
                
                UPDATE Job
                SET Job_Title = COALESCE(@Job_Title, @Old_Job_Title),
                    Salary = COALESCE(@Salary, @Old_Salary),
                    Hiring_Date = COALESCE(@Hiring_Date, @Old_Hiring_Date),
                    Company_Name = COALESCE(@Company_Name, @Old_Company_Name),
                    Job_Type = COALESCE(@Job_Type, @Old_Job_Type),
                    St_ID = COALESCE(@St_ID, St_ID)
                WHERE Job_ID = @Job_ID;
                
                SELECT 'Job updated successfully' AS Message;
            END
            ELSE
            BEGIN
                SELECT 'Enter Valid Student ID' AS Message;
            END
        END
        ELSE
        BEGIN
            SELECT 'Job ID does not exist' AS Message;
        END
    END TRY
    BEGIN CATCH
        SELECT 'An error occurred. Please try again later.' AS Message;
    END CATCH
END;


Execute UpdateJob 1001,@St_ID=12000;


CREATE PROCEDURE DeleteJob
    @Job_ID INT
AS
BEGIN
    BEGIN TRY
        IF EXISTS (SELECT * FROM Job WHERE Job_ID = @Job_ID)
        BEGIN
            DELETE FROM Job WHERE Job_ID = @Job_ID;
            SELECT 'Job deleted successfully' AS Message;
        END
        ELSE
        BEGIN
            SELECT 'Job ID does not exist' AS Message;
        END
    END TRY
    BEGIN CATCH
        SELECT 'An error occurred. Please try again later.' AS Message;
    END CATCH
END;

Execute DeleteJob 10010;
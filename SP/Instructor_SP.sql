CREATE PROCEDURE AddInstructor
    @Ins_SSN varchar(50),
    @First_Name varchar(500),
    @Last_Name varchar(500),
    @Salary int,
    @Ins_Email varchar(50),
    @Password varchar(50),
    @Phone varchar(50),
    @Job_Type varchar(100),
    @Address_ID INT
AS
BEGIN
 
    INSERT INTO Instructor
    VALUES (@Ins_SSN, @First_Name, @Last_Name, @Salary, @Ins_Email, @Password, @Phone, @Job_Type, @Address_ID);
    
END;

CREATE PROCEDURE UpdateInstructor
    @Ins_ID INT,
    @Ins_SSN varchar(50),
    @First_Name varchar(500)=Null,
    @Last_Name varchar(500)=Null,
    @Salary int=Null,
    @Ins_Email varchar(50)=Null,
    @Password varchar(50)=Null,
    @Phone varchar(50)=Null,
    @Job_Type varchar(100)=Null,
    @Address_ID INT
AS
BEGIN
    -- Check if the provided Ins_ID exists in the Instructor table
    IF NOT EXISTS (SELECT * FROM Instructor WHERE Ins_ID = @Ins_ID)
    BEGIN
        Print('The provided Ins_ID does not exist in the Instructor table.');
    END;

    -- Check if the provided Address_ID exists in the Address table

	DECLARE @Old_First_Name varchar(500),
            @Old_Last_Name varchar(500),
            @Old_Salary int,
            @Old_Ins_Email varchar(50),
            @Old_Password varchar(50),
            @Old_Phone varchar(50),
            @Old_Job_Type varchar(100),
            @Old_Address_ID INT;


     SELECT @Old_First_Name = First_Name,
           @Old_Last_Name = Last_Name,
           @Old_Salary = Salary,
           @Old_Ins_Email = Ins_Email,
           @Old_Password = Password,
           @Old_Phone = Phone,
           @Old_Job_Type = Job_Type,
           @Old_Address_ID = Address_ID
    FROM Instructor
    WHERE Ins_SSN = @Ins_SSN;
	IF NOT EXISTS (SELECT * FROM Address WHERE Address_ID = @Address_ID)
    BEGIN
        Print('The provided Address_ID does not exist in the Address table.');
    END;
    -- Update the values with the new ones if provided, otherwise keep the old values
    UPDATE Instructor
    SET First_Name = COALESCE(@First_Name, @Old_First_Name),
        Last_Name = COALESCE(@Last_Name, @Old_Last_Name),
        Salary = COALESCE(@Salary, @Old_Salary),
        Ins_Email = COALESCE(@Ins_Email, @Old_Ins_Email),
        Password = COALESCE(@Password, @Old_Password),
        Phone = COALESCE(@Phone, @Old_Phone),
        Job_Type = COALESCE(@Job_Type, @Old_Job_Type),
        Address_ID = COALESCE(@Address_ID, @Old_Address_ID)
    WHERE Ins_ID = @Ins_ID;
END;



CREATE PROCEDURE DeleteInstructor
    @Ins_SSN varchar(50)
AS
BEGIN
    -- Check if the provided Ins_SSN exists in the Instructor table
    IF NOT EXISTS (SELECT 1 FROM Instructor WHERE Ins_SSN = @Ins_SSN)
    BEGIN
        Print('The provided Ins_SSN does not exist in the Instructor table.');
    END;

    -- Delete the instructor based on the provided Ins_SSN
    DELETE FROM Instructor WHERE Ins_SSN = @Ins_SSN;
END;


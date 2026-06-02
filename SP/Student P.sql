Alter PROCEDURE AddStudent
    @St_SSN VARCHAR(14),
    @First_Name VARCHAR(100),
    @Last_Name VARCHAR(100),
    @Graduation_Year INT,
    @Gender VARCHAR(1),
    @Date_of_Birth DATE,
    @St_Email VARCHAR(50),
    @Password VARCHAR(50),
    @Phone VARCHAR(20),
    @Address_ID INT,
    @Team_ID INT
AS
BEGIN
    BEGIN TRY
        IF EXISTS (SELECT * FROM Address WHERE Address_ID = @Address_ID) AND 
           EXISTS (SELECT * FROM Graduation_Team WHERE Team_ID = @Team_ID)
        BEGIN
            IF NOT EXISTS (SELECT * FROM Student WHERE St_SSN = @St_SSN)
            BEGIN
                INSERT INTO Student (St_SSN, First_Name, Last_Name, Graduation_Year, Gender, Date_of_Birth, St_Email, Password, Phone, Address_ID, Team_ID)
                VALUES (@St_SSN, @First_Name, @Last_Name, @Graduation_Year, @Gender, @Date_of_Birth, @St_Email, @Password, @Phone, @Address_ID, @Team_ID);
                
                SELECT 'Student added successfully' AS Message;
            END
            ELSE
            BEGIN
                SELECT 'Student with the provided SSN already exists' AS Message;
            END
        END
        ELSE
        BEGIN
            SELECT 'Please provide valid Zip Code and Team IDs' AS Message;
        END
    END TRY
    BEGIN CATCH
        SELECT 'An error occurred. Please try again later.' AS Message;
    END CATCH
END;


Execute AddStudent 12365478965478,'Nnnnn','Gggggggg',2015,'M','2002-01-01','marwaashraf5814@gmail.com','budfcfhuiswh0','+201025357234',5,100;


Alter PROCEDURE UpdateStudent
    @St_SSN VARCHAR(14),
    @First_Name VARCHAR(100) = NULL,
    @Last_Name VARCHAR(100) = NULL,
    @Graduation_Year INT = NULL,
    @Gender VARCHAR(1) = NULL,
    @Date_of_Birth DATE = NULL,
    @St_Email VARCHAR(50) = NULL,
    @Password VARCHAR(50) = NULL,
    @Phone VARCHAR(20) = NULL,
    @Address_ID INT = NULL,
    @Team_ID INT = NULL
AS
BEGIN
    BEGIN TRY
        IF EXISTS (SELECT * FROM Student WHERE St_SSN = @St_SSN)
        BEGIN
            DECLARE @Old_First_Name VARCHAR(100),
                    @Old_Last_Name VARCHAR(100),
                    @Old_Graduation_Year INT,
                    @Old_Gender VARCHAR(1),
                    @Old_Date_of_Birth DATE,
                    @Old_St_Email VARCHAR(50),
                    @Old_Password VARCHAR(50),
                    @Old_Phone VARCHAR(20),
                    @Old_Address_ID INT,
                    @Old_Team_ID INT;

            SELECT @Old_First_Name = First_Name,
                   @Old_Last_Name = Last_Name,
                   @Old_Graduation_Year = Graduation_Year,
                   @Old_Gender = Gender,
                   @Old_Date_of_Birth = Date_of_Birth,
                   @Old_St_Email = St_Email,
                   @Old_Password = Password,
                   @Old_Phone = Phone,
                   @Old_Address_ID = Address_ID,
                   @Old_Team_ID = Team_ID
            FROM Student
            WHERE St_SSN = @St_SSN;

            -- Check if provided Zip Code ID exists
            IF (@Address_ID IS NULL OR EXISTS (SELECT * FROM Address WHERE Address_ID = @Address_ID))
            BEGIN
                -- Check if provided Team ID exists
                IF (@Team_ID IS NULL OR EXISTS (SELECT * FROM Graduation_Team WHERE Team_ID = @Team_ID))
                BEGIN
                    UPDATE Student
                    SET First_Name = COALESCE(@First_Name, @Old_First_Name),
                        Last_Name = COALESCE(@Last_Name, @Old_Last_Name),
                        Graduation_Year = COALESCE(@Graduation_Year, @Old_Graduation_Year),
                        Gender = COALESCE(@Gender, @Old_Gender),
                        Date_of_Birth = COALESCE(@Date_of_Birth, @Old_Date_of_Birth),
                        St_Email = COALESCE(@St_Email, @Old_St_Email),
                        Password = COALESCE(@Password, @Old_Password),
                        Phone = COALESCE(@Phone, @Old_Phone),
                        Address_ID = COALESCE(@Address_ID, @Old_Address_ID),
                        Team_ID = COALESCE(@Team_ID, @Old_Team_ID)
                    WHERE St_SSN = @St_SSN;
                    
                    SELECT 'Student information updated successfully' AS Message;
                END
                ELSE
                BEGIN
                    SELECT 'Team with the provided ID does not exist' AS Message;
                END
            END
            ELSE
            BEGIN
                SELECT 'Zip Code with the provided ID does not exist' AS Message;
            END
        END
        ELSE
        BEGIN
            SELECT 'Student with the provided SSN does not exist' AS Message;
        END
    END TRY
    BEGIN CATCH
        SELECT 'An error occurred. Please try again later.' AS Message;
    END CATCH
END;

Execute UpdateStudent 12365478965478,@Address_ID=50;


CREATE PROCEDURE DeleteStudent
    @St_SSN VARCHAR(14)
AS
BEGIN
    BEGIN TRY
        IF EXISTS (SELECT * FROM Student WHERE St_SSN = @St_SSN)
        BEGIN
            DELETE FROM Student WHERE St_SSN = @St_SSN;
            SELECT 'Student deleted successfully' AS Message;
        END
        ELSE
        BEGIN
            SELECT 'Student with the provided SSN does not exist' AS Message;
        END
    END TRY
    BEGIN CATCH
        SELECT 'An error occurred. Please try again later.' AS Message;
    END CATCH
END;


Execute DeleteStudent 12365478965478;
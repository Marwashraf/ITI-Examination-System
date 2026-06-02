Create PROCEDURE AddCompany
    @Company_Name VARCHAR(100),
    @Launch_Date DATE,
    @Company_Filed VARCHAR(100),
    @Zip_Code INT
AS
BEGIN
    IF EXISTS (SELECT * FROM Address WHERE Zip_Code = @Zip_Code)
    BEGIN 
        INSERT INTO Company
        VALUES (@Company_Name, @Launch_Date, @Company_Filed, @Zip_Code);
        
        SELECT 'Added Successfully' AS Message;
    END
    ELSE
        SELECT 'Enter Valid Zip Code' AS Message;
END


Execute AddCompany 'ftsygiudiu','2020-03-03','fcghvjv',1000;


Create PROCEDURE UpdateCompany
    @Company_ID INT,
    @Company_Name VARCHAR(100) = NULL,
    @Launch_Date DATE = NULL,
    @Company_Field VARCHAR(100) = NULL,
    @Zip_Code INT = NULL
AS
BEGIN
    BEGIN TRY
        DECLARE @Old_Company_Name VARCHAR(100),
                @Old_Launch_Date DATE,
                @Old_Company_Field VARCHAR(100),
                @Old_Zip_Code INT;

        SELECT @Old_Company_Name = Company_Name,
               @Old_Launch_Date = Launch_Date,
               @Old_Company_Field = Company_Filed,
               @Old_Zip_Code = Zip_Code
        FROM Company
        WHERE Company_ID = @Company_ID;

        IF NOT EXISTS (SELECT 1 FROM Company WHERE Company_ID = @Company_ID)
        BEGIN
            SELECT 'Company ID does not exist' AS Message;
            RETURN;
        END

        IF @Zip_Code IS NOT NULL AND NOT EXISTS (SELECT 1 FROM Address WHERE Zip_Code = @Zip_Code)
        BEGIN
            SELECT 'Enter Valid Zip Code' AS Message;
            RETURN;
        END

        UPDATE Company
        SET Company_Name = COALESCE(@Company_Name, @Old_Company_Name),
            Launch_Date = COALESCE(@Launch_Date, @Old_Launch_Date),
            Company_Filed = COALESCE(@Company_Field, @Old_Company_Field),
            Zip_Code = COALESCE(@Zip_Code, @Old_Zip_Code)
        WHERE Company_ID = @Company_ID;

        SELECT 'Company information updated successfully' AS Message;
    END TRY
    BEGIN CATCH
        SELECT 'An error occurred. Please try again later.' AS Message;
    END CATCH
END;



Execute UpdateCompany 70,@Zip_Code=30;

Create PROCEDURE DeleteCompany
    @Company_ID INT
AS
BEGIN
    BEGIN TRY
        IF EXISTS (SELECT * FROM Company WHERE Company_ID = @Company_ID)
        BEGIN
			DELETE FROM Company
			WHERE Company_ID = @Company_ID;

        SELECT 'Company deleted successfully' AS Message;
            
        END
		Else
		SELECT 'Company ID does not exist' AS Message;
    END TRY
    BEGIN CATCH
        SELECT 'An error occurred. Please try again later.' AS Message;
    END CATCH
END;

Execute DeleteCompany 90;
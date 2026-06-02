Alter PROCEDURE AddFreelance
    @Description VARCHAR(200),
    @Cost INT,
    @Duration INT,
    @St_Account VARCHAR(200),
    @Client_Name VARCHAR(200),
    @Client_Number VARCHAR(20),
    @St_ID INT
AS
BEGIN
    IF EXISTS (SELECT * FROM Student WHERE St_ID = @St_ID)
    BEGIN
        INSERT INTO Freelance (Description, Cost, Duration, St_Account, Client_Name, Client_Number,St_ID)
        VALUES (@Description, @Cost, @Duration, @St_Account, @Client_Name, @Client_Number,@St_ID);

        SELECT 'Added Successfully' AS Message;
    END
    ELSE
    BEGIN
        SELECT 'Enter Valid Student ID' AS Message;
    END
END;



Execute AddFreelance 'udsfvkugvfj',456,1000,159,'brfgbyuj','487465312346',1000;


Create PROCEDURE UpdateFreelance
    @Freelance_ID INT,
    @Description VARCHAR(200) = NULL,
    @Cost INT = NULL,
    @Duration INT = NULL,
    @St_Account VARCHAR(200) = NULL,
    @Client_Name VARCHAR(200) = NULL,
    @Client_Number VARCHAR(20) = NULL,
    @St_ID INT = NULL
AS
BEGIN
    BEGIN TRY
        IF EXISTS (SELECT * FROM Freelance WHERE Fr_ID = @Freelance_ID)
        BEGIN
            IF @St_ID IS NULL OR EXISTS (SELECT * FROM Student WHERE St_ID = @St_ID)
            BEGIN
                DECLARE @Old_Description VARCHAR(200),
                        @Old_Cost INT,
                        @Old_Duration INT,
                        @Old_St_Account VARCHAR(200),
                        @Old_Client_Name VARCHAR(200),
                        @Old_Client_Number VARCHAR(20);

                SELECT @Old_Description = Description,
                       @Old_Cost = Cost,
                       @Old_Duration = Duration,
                       @Old_St_Account = St_Account,
                       @Old_Client_Name = Client_Name,
                       @Old_Client_Number = Client_Number
                FROM Freelance
                WHERE Fr_ID = @Freelance_ID;

                -- Update the Freelance only if the Student ID exists
                UPDATE Freelance
                SET Description = COALESCE(@Description, @Old_Description),
                    Cost = COALESCE(@Cost, @Old_Cost),
                    Duration = COALESCE(@Duration, @Old_Duration),
                    St_Account = COALESCE(@St_Account, @Old_St_Account),
                    Client_Name = COALESCE(@Client_Name, @Old_Client_Name),
                    Client_Number = COALESCE(@Client_Number, @Old_Client_Number),
                    St_ID = @St_ID
                WHERE Fr_ID = @Freelance_ID;
                
                SELECT 'Freelance information updated successfully' AS Message;
            END
            ELSE
            BEGIN
                SELECT 'Enter Valid Student ID' AS Message;
            END
        END
        ELSE
        BEGIN
            SELECT 'Freelance with the provided ID does not exist' AS Message;
        END
    END TRY
    BEGIN CATCH
        SELECT 'An error occurred. Please try again later.' AS Message;
    END CATCH
END;



Execute UpdateFreelance @Freelance_ID=1003,@Description='yuhfiuhudof', @St_ID=50 ;


CREATE PROCEDURE DeleteFreelance
    @Freelance_ID INT
AS
BEGIN
    BEGIN TRY
        IF EXISTS (SELECT * FROM Freelance WHERE Fr_ID = @Freelance_ID)
        BEGIN
            -- Delete the Freelance
            DELETE FROM Freelance
            WHERE Fr_ID = @Freelance_ID;
            
            SELECT 'Freelance deleted successfully' AS Message;
        END
        ELSE
        BEGIN
            SELECT 'Freelance with the provided ID does not exist' AS Message;
        END
    END TRY
    BEGIN CATCH
        SELECT 'An error occurred. Please try again later.' AS Message;
    END CATCH
END;


Execute DeleteFreelance 1002;
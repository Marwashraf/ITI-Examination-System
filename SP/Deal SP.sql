Alter PROCEDURE AddDeal
    @Branch_ID INT,
    @Company_ID INT
AS
BEGIN
    IF EXISTS (SELECT * FROM Branch WHERE B_ID = @Branch_ID) AND EXISTS (SELECT * FROM Company WHERE Company_ID = @Company_ID)
    BEGIN
        IF NOT EXISTS (SELECT * FROM Deal WHERE Branch_ID = @Branch_ID AND Company_ID = @Company_ID)
        BEGIN
            INSERT INTO Deal (Branch_ID, Company_ID)
            VALUES (@Branch_ID, @Company_ID);

            SELECT 'Deal added successfully' AS Message;
        END
        ELSE
        BEGIN
            SELECT 'Deal already exists for the provided Branch ID and Company ID' AS Message;
        END
    END
    ELSE
    BEGIN
        SELECT 'Invalid Branch ID or Company ID' AS Message;
    END
END;

Execute AddDeal 1,1;


Create PROCEDURE DeleteDeal
    @Branch_ID INT,
    @Company_ID INT
AS
BEGIN
    BEGIN TRY
        IF EXISTS (
            SELECT * 
            FROM Deal 
            WHERE Branch_ID = @Branch_ID 
            AND Company_ID = @Company_ID
        )
        BEGIN
            DELETE FROM Deal
            WHERE Branch_ID = @Branch_ID 
            AND Company_ID = @Company_ID;

            SELECT 'Deal deleted successfully' AS Message;
        END
        ELSE
        BEGIN
            SELECT 'Deal with the provided Branch ID and Company ID does not exist' AS Message;
        END
    END TRY
    BEGIN CATCH
        SELECT 'An error occurred. Please try again later.' AS Message;
    END CATCH
END;


Execute DeleteDeal 50,1;

CREATE PROCEDURE AddCertificate 
    @Credintial_URL VARCHAR(200),
    @Ct_Name VARCHAR(50),
    @Description VARCHAR(200),
    @Hours INT,
    @St_ID INT
AS
BEGIN
    IF NOT EXISTS (SELECT * FROM Certificate WHERE Credintial_URL = @Credintial_URL)
    BEGIN
        IF EXISTS (SELECT * FROM Student WHERE St_ID = @St_ID)
        BEGIN
            INSERT INTO Certificate (Credintial_URL, Ct_Name, Description, Hours, St_ID)
            VALUES (@Credintial_URL, @Ct_Name, @Description, @Hours, @St_ID);

            SELECT 'Added Successfully' AS Message;
        END
        ELSE
        BEGIN
            SELECT 'Enter Valid Student ID' AS Message;
        END
    END
    ELSE
    BEGIN
        SELECT 'Enter Valid Credential URL' AS Message;
    END
END;


Execute AddCertificate 'asdfghjkl;','poiuyt','sdrtfgyhuji',458,1003;


Alter PROCEDURE DeleteCertificate
    @Ct_ID VARCHAR(200)
AS
BEGIN
    IF EXISTS (SELECT * FROM Certificate WHERE Ct_ID = @Ct_ID)
    BEGIN
        DELETE FROM Certificate WHERE Ct_ID = @Ct_ID;
        SELECT 'Certificate deleted successfully' AS Message;
    END
    ELSE
    BEGIN
        SELECT 'Certificate with the provided ID does not exist' AS Message;
    END
END;


Execute DeleteCertificate 1000;
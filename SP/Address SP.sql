CREATE PROCEDURE AddAddress 
    @City VARCHAR(100)
AS
BEGIN
    INSERT INTO Address (City) 
    VALUES (@City);
END;

Execute AddAddress Elmaadi;

ALTER PROCEDURE UpdateAddress
    @Address_ID INT,
    @City VARCHAR(100) = NULL
AS
BEGIN
    IF EXISTS (SELECT * FROM Address WHERE Address_ID = @Address_ID)
    BEGIN
        DECLARE @Old_City VARCHAR(100)
        SELECT @Old_City = City
        FROM Address
        WHERE Address_ID = @Address_ID;

        UPDATE Address
        SET City = COALESCE(@City, @Old_City) 
        WHERE Address_ID = @Address_ID;
        
        SELECT 'Address updated successfully' AS Message;
    END
    ELSE
    BEGIN
        SELECT 'Address ID Does Not Exist' AS Message;
    END
END;


Execute UpdateAddress 24,'Adel';


Alter Procedure DeleteAddress(@Address_ID int)
AS
BEGIN
    IF  EXISTS (SELECT * FROM Address WHERE Address_ID = @Address_ID)
    BEGIN
        Delete  Address
        Where Address_ID=@Address_ID
    END
    ELSE
    BEGIN
		Select'Address Zip Code Does Not Exist'
	END
End;


Execute DeleteAddress 24;
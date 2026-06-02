
-------------------------------AddProgram
Create Procedure AddProgram(@P_Name varchar(100),@P_SMonth INT,@P_EMonth INT,@P_Quarter Int,@P_Duration Int)
AS
Begin
	Insert Into Program
	Values(@P_Name,@P_SMonth,@P_EMonth,@P_Quarter,@P_Duration)
End;



---------------------Delete Program
Create PROCEDURE DeleteProgram @P_ID INT
AS
BEGIN
    IF  EXISTS (SELECT * FROM Program WHERE P_ID = @P_ID )
    BEGIN
        Delete Program
		Where P_ID=@P_ID
    END
    ELSE
    BEGIN
       Select'Program Does Not Exist'
    END
END;

Execute AddProgram





Alter Procedure AddBranch (@B_Name varchar(100),@Address_ID Int)
AS
Begin
	insert into Branch 
	Values (@B_Name,@Address_ID)
ENd;

Execute AddBranch Elmaadi,11;

Create Procedure DeleteBranch (@B_ID Int)
AS
BEGIN
IF  EXISTS (SELECT * FROM Branch WHERE B_ID = @B_ID)
    BEGIN
        Delete  Branch
        Where B_ID=@B_ID
    END
    ELSE
    BEGIN
		Select'Branch ID Does Not Exist'
	END
End;
Execute DeleteBranch  17;


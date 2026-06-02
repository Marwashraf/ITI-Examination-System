Create Procedure AddDepartment(@D_Name varchar(100),@Ins_ID int)
AS
Begin
	Insert Into Department
	Values(@D_Name,@Ins_ID)
End;

Execute AddDepartment Elmaadi,987;

ALTER PROCEDURE UpdateDepartment 
    @Dept_Id INT,
    @Dept_Name VARCHAR(100) = NULL,
	@Ins_ID INT=Null
AS
BEGIN
    BEGIN TRY
        IF EXISTS (SELECT * FROM Department WHERE Dept_ID = @Dept_Id)
        BEGIN
            IF @Ins_ID IS NULL OR EXISTS (SELECT * FROM Instructor WHERE Ins_ID = @Ins_ID)
            BEGIN
                DECLARE @Old_Dept_Name VARCHAR(100),
                        @Old_Ins_ID INT;

                SELECT @Old_Dept_Name = Dept_Name,
                       @Old_Ins_ID = Ins_ID
                FROM Department
                WHERE Dept_ID = @Dept_Id;

                UPDATE Department
                SET Dept_Name = COALESCE(@Dept_Name, @Old_Dept_Name),
                    Ins_ID = COALESCE(@Ins_ID, @Old_Ins_ID)
                WHERE Dept_ID = @Dept_Id;
                
                SELECT 'Department updated successfully' AS Message;
            END
            ELSE
            BEGIN
                SELECT 'Enter Valid Instractor ID' AS Message;
            END
        END
        ELSE
        BEGIN
            SELECT 'Enter Valid Department ID' AS Message;
        END
    END TRY
    BEGIN CATCH
        SELECT 'An error occurred. Please try again later.' AS Message;
    END CATCH
END;



Execute UpdateDepartment 17, @Dept_Name='Adel';


Alter Procedure DeleteDepartment(@Dept_ID int)
AS
Begin
	If Exists (Select * From Department Where Dept_ID=@Dept_ID)
	Begin
	Delete Department
	Where Dept_ID=@Dept_ID
	Select 'Deleted Successfully'
	END
	Else
	Select'Enter Valid Department ID'
End;

Execute DeleteDepartment 16;

Alter Procedure AddGraduationProject(@Pro_Name Varchar(100),@MinMarktoPass INT,@FullMark INT,@Track_ID INT)
AS
Begin
	if Exists(Select * From Track where T_ID=@Track_ID)
		Begin
			Insert Into Graduation_Project
			Values (@Pro_Name,@MinMarktoPass,@FullMark,@Track_ID)
			Select 'Added Successfully' As Message 
		End
		Else
		select'Enter Valid Track Id'
END;

Execute AddGraduationProject 'yjgfvdujgv',25,100,29;

CREATE PROCEDURE DeleteGraduationProject
    @Project_ID INT
AS
BEGIN
    IF EXISTS (SELECT * FROM Graduation_Project WHERE Project_ID = @Project_ID)
    BEGIN
        Delete Graduation_Project
		Where Project_ID=@Project_ID
    END
    ELSE
    BEGIN
        Select 'Graduation Project Does not Exist'
    END
END;

Execute DeleteGraduationProject 31;



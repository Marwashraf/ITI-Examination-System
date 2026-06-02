Create Procedure AddTopic(@T_Name Varchar(100))
AS
Begin
	Insert Into Topic 
	Values (@T_Name)
END

Execute AddTopic 'gyujgfyudsgyls';

Create Procedure DeleteTopic(@T_ID int)
AS
Begin
	IF EXISTS (Select * From Topic Where Topic_ID=@T_ID)
	Begin
	Delete Topic 
	Where Topic_ID=@T_ID
	Select 'Deleted Successfully' AS Message;
	END
	ELSE
	Select 'Enter Valid Topic ID Successfully' AS Message;
END;

Execute DeleteTopic 17;

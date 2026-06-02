Update Student
Set Team_ID=1
Where St_ID<=5 


DECLARE @St_ID INT,@T_ID INT
SET @St_ID = 5
SET @T_ID=2
WHILE @St_ID <= 1000
BEGIN
    UPDATE Student
    SET Team_ID = @T_ID
    WHERE St_ID > @St_ID and St_ID<=@St_ID+5
    
    SET @St_ID = @St_ID + 5
	SET @T_ID=@T_ID+1
END

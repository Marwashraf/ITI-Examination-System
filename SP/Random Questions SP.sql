
Alter PROCEDURE GetRandomQuestions @cr_name Varchar(500)
AS
BEGIN
    SET NOCOUNT ON;
    SELECT  Top(10) q.*
    FROM Questions as q
	inner join Courses as c
	on c.Cr_ID = q.Crs_ID
	Where c.Cr_Name=@cr_name
    ORDER BY NEWID(); -- Use NEWID() to randomize the selection
END;
GO

GetRandomQuestions 'Data Science'





Create Procedure AddCourses (@Cr_Name varchar(100),@Hours INT,@Topic_ID INT)
AS
BEGIN
	IF EXISTS (Select * From Topic where Topic_ID=@Topic_ID)
	Begin
	INSERT INTO Courses
	Values(@Cr_Name,@Hours,@Topic_ID)
	Select 'Added Successfully' AS Message
	END
	ElSE
	Select 'Enter Valid Topic ID' AS Message
ENd

Execute AddCourses 'tfdhvugilahgfiughiu',123,16;

ALTER PROCEDURE UpdateCourses 
    @Cr_ID INT,
    @Cr_Name VARCHAR(100) = NULL,
    @Hours INT = NULL,
    @Topic_ID INT = NULL
AS
BEGIN
    BEGIN TRY
        -- Check if the course ID exists
        IF EXISTS (SELECT * FROM Courses WHERE Cr_ID = @Cr_ID)
        BEGIN
            -- Check if the provided Topic_ID exists in the Topic table
            IF @Topic_ID IS NULL OR EXISTS (SELECT * FROM Topic WHERE Topic_ID = @Topic_ID)
            BEGIN
                DECLARE @Old_Cr_Name VARCHAR(100),
                        @Old_Hours INT,
                        @Old_Topic_ID INT;

                SELECT @Old_Cr_Name = Cr_Name,
                       @Old_Hours = Hours,
                       @Old_Topic_ID = Topic_ID
                FROM Courses
                WHERE Cr_ID = @Cr_ID;

                -- Update the course only if the Topic_ID exists
                UPDATE Courses
                SET Cr_Name = COALESCE(@Cr_Name, @Old_Cr_Name),
                    Hours = COALESCE(@Hours, @Old_Hours),
                    Topic_ID = COALESCE(@Topic_ID, @Old_Topic_ID)
                WHERE Cr_ID = @Cr_ID;
                
                SELECT 'Courses updated successfully' AS Message;
            END
            ELSE
            BEGIN
                SELECT 'Enter Valid Topic ID' AS Message;
            END
        END
        ELSE
        BEGIN
            SELECT 'Enter Valid Course ID' AS Message;
        END
    END TRY
    BEGIN CATCH
        SELECT 'An error occurred. Please try again later.' AS Message;
    END CATCH
END;


Execute UpdateCourses @Cr_ID=32,@Cr_Name='Adel' ,@Topic_ID=40;



Create Procedure DeleteCourses (@Cr_ID INT)
AS
Begin
	If Exists (Select * From Courses where Cr_ID=@Cr_ID )
	BEGIN	
		Delete Courses
		Where Cr_ID=@Cr_ID 
		Select 'Deleted Successfully'
	END
	Else
		Select 'Enter Valid Course ID'
END

Execute DeleteCourses @Cr_ID=31;
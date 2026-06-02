ALTER PROCEDURE AddTrackCourses
    @Cr_ID INT,
    @Track_ID INT
AS
BEGIN
    BEGIN TRY
        IF EXISTS (SELECT * FROM Courses WHERE Cr_ID = @Cr_ID) AND 
           EXISTS (SELECT * FROM Track WHERE T_ID = @Track_ID) 
        BEGIN
            IF NOT EXISTS (SELECT * FROM Track_Courses WHERE Cr_ID = @Cr_ID AND Track_ID = @Track_ID)
            BEGIN
                INSERT INTO Track_Courses (Cr_ID, Track_ID)
                VALUES (@Cr_ID, @Track_ID);
                
                SELECT 'Track and Course added successfully' AS Message;
            END
            ELSE
            BEGIN
                SELECT 'Track and Course combination already exists' AS Message;
            END
        END
        ELSE
        BEGIN
            SELECT 'Enter Valid Track and Course IDs' AS Message;
        END
    END TRY
    BEGIN CATCH
        SELECT 'An error occurred. Please try again later.' AS Message;
    END CATCH
END;



Execute AddTrackCourses 1,5;


Alter PROCEDURE DeleteTrackCourses
     @Cr_ID INT,
     @Track_ID INT
AS
BEGIN
    IF EXISTS (SELECT * FROM Track_Courses WHERE Track_ID = @Track_ID AND Cr_ID = @Cr_ID)
    BEGIN
        Delete Track_Courses
		Where Track_ID = @Track_ID AND Cr_ID = @Cr_ID
		Select 'Deleted Successfully ' As Message
    END
    ELSE
    BEGIN
		Select 'Enter Valid ID ' As Message
    END
END;



Execute DeleteTrackCourses 1,5;
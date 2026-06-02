Alter Procedure AddTrack(@T_Name Varchar(100),@Duration INT,@Capacity INT,@No_Courses INT,@Dept_ID INT)
AS
BEGIN
    IF  EXISTS (SELECT * FROM Department WHERE Dept_ID = @Dept_ID)
    BEGIN
        INSERT INTO Track
        VALUES (@T_Name, @Duration,@Capacity,@No_Courses,@Dept_ID);
    END
    ELSE
    BEGIN
		Select'Department ID Does Not Exist' As Message
	END
EnD;

Execute AddTrack 'rdytfgulihojk',20,12,85,1;

Execute AddTrack 'rdytfgulihojk',20,12,85,6;

Alter PROCEDURE UpdateTrack
    @T_ID INT,
    @T_Name VARCHAR(100) = NULL,
    @Duration INT = NULL,
    @Capacity INT = NULL,
    @No_Courses INT = NULL,
    @Dept_ID INT = NULL
AS
BEGIN
    BEGIN TRY
        IF EXISTS (SELECT * FROM Track WHERE T_ID = @T_ID)
        BEGIN
            IF @Dept_ID IS NULL OR EXISTS (SELECT * FROM Department WHERE Dept_ID = @Dept_ID)
            BEGIN
                DECLARE @Old_T_Name VARCHAR(100), 
                        @Old_Duration INT, 
                        @Old_Capacity INT, 
                        @Old_No_Courses INT, 
                        @Old_Dept_ID INT;

                SELECT @Old_T_Name = T_Name,
                       @Old_Duration = Duration,
                       @Old_Capacity = Capacity,
                       @Old_No_Courses = No_Courses,
                       @Old_Dept_ID = Dept_ID
                FROM Track
                WHERE T_ID = @T_ID;

                UPDATE Track
                SET T_Name = COALESCE(@T_Name, @Old_T_Name),
                    Duration = COALESCE(@Duration, @Old_Duration),
                    Capacity = COALESCE(@Capacity, @Old_Capacity),
                    No_Courses = COALESCE(@No_Courses, @Old_No_Courses),
                    Dept_ID = COALESCE(@Dept_ID, @Old_Dept_ID)
                WHERE T_ID = @T_ID;
                
                SELECT 'Track updated successfully' AS Message;
            END
            ELSE
            BEGIN
                SELECT 'Enter Valid Department ID' AS Message;
            END
        END
        ELSE
        BEGIN
            SELECT 'Track ID Does Not Exist' AS Message;
        END
    END TRY
    BEGIN CATCH
        SELECT 'An error occurred. Please try again later.' AS Message;
    END CATCH
END;


Execute UpdateTrack 34,@Dept_ID=30;


Alter Procedure DeleteTrack(@T_ID INT)
AS
BEGIN
    IF  EXISTS (SELECT * FROM Track WHERE T_ID = @T_ID)
    BEGIN
        Delete  Track
        Where T_ID=@T_ID
		Select'Deleted Successfully' As Message
    END
    ELSE
    BEGIN
		Select'Track ID Does Not Exist' As Message
	END
EnD;

Execute DeleteTrack 34;
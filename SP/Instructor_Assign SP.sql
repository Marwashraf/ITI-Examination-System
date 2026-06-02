-------------Ins_Assign
Create PROCEDURE AddInstructorAssign
    @Program_ID INT,
    @Branch_ID INT,
    @Dept_ID INT,
    @Track_ID INT,
	@Course_ID INT,
	@Ins_ID INT,
    @Intake INT,
	@Course_SDate Date,
	@Course_EDate Date
AS
BEGIN
	IF NOT EXISTS (SELECT * FROM Program WHERE P_ID = @Program_ID)
    BEGIN
        SELECT 'Enter Valid Program ID' AS Message;
        RETURN;
    END

	IF NOT EXISTS (SELECT * FROM Branch WHERE B_ID = @Branch_ID)
    BEGIN
        SELECT 'Enter Valid Branch ID' AS Message;
        RETURN;
    END

	IF NOT EXISTS (SELECT *  FROM Department WHERE Dept_ID = @Dept_ID)
    BEGIN
        SELECT 'Enter Valid Department ID' AS Message;
        RETURN;
    END

    IF NOT EXISTS (SELECT * FROM Track WHERE T_ID = @Track_ID)
    BEGIN
        SELECT 'Enter Valid Track ID' AS Message;
        RETURN;
    END

	IF NOT EXISTS (SELECT * FROM Courses WHERE Cr_ID = @Course_ID)
    BEGIN
        SELECT 'Enter Valid Track ID' AS Message;
        RETURN;
    END

    IF NOT EXISTS (SELECT * FROM Instructor WHERE Ins_ID = @Ins_ID)
    BEGIN
        SELECT 'Enter Valid Instructor ID' AS Message;
        RETURN;
    END

    IF NOT EXISTS (SELECT * FROM Intakes WHERE Intake = @Intake)
    BEGIN
        SELECT 'Enter Valid Intake' AS Message;
        RETURN;
    END

   
    INSERT INTO Instructor_Assign
    VALUES ( @Program_ID,@Branch_ID,@Dept_ID, @Track_ID,@Course_ID,@Ins_ID, @Intake,@Course_SDate,@Course_EDate);

    SELECT 'Instructor Assign added successfully' AS Message;
END;


Execute AddInstructorAssign 9,14,9,15,20,3,35,'2020-03-03','2020-05-05';



--------------------------Update Assign
Create PROCEDURE UpdateInstractorAssign
    @Program_ID INT,
    @Branch_ID INT,
    @Dept_ID INT,
    @Track_ID INT,
    @Course_ID INT,
    @Ins_ID INT,
    @Intake INT,
    @Course_SDate DATE = NULL,
    @Course_EDate DATE = NULL
AS
BEGIN
    BEGIN TRY
        DECLARE 
            @Old_Program_ID INT,
            @Old_Branch_ID INT,
            @Old_Dept_ID INT,
            @Old_Track_ID INT,
            @Old_Course_ID INT,
            @Old_Ins_ID INT,
            @Old_Intake INT,
            @Old_C_SDate DATE,
            @Old_C_EDate DATE;

        SELECT 
            @Old_Program_ID = Program_ID,
            @Old_Branch_ID = Branch_ID,
            @Old_Dept_ID = Dept_ID,
            @Old_Track_ID = Track_ID,
            @Old_Course_ID = Course_ID,
            @Old_Ins_ID = Ins_ID,
            @Old_Intake = Intake,
            @Old_C_SDate = Course_SData,
            @Old_C_EDate = Course_EDate
        FROM Instructor_Assign
        WHERE Ins_ID = @Ins_ID 
            AND Program_ID = @Program_ID 
            AND Branch_ID = @Branch_ID 
            AND Dept_ID = @Dept_ID 
			AND Track_ID=@Track_ID
			AND Course_ID=@Course_ID
			AND Ins_ID=@Ins_ID
            AND Intake = @Intake;

        IF @Program_ID IS NOT NULL AND NOT EXISTS (SELECT * FROM Program WHERE P_ID = @Program_ID)
        BEGIN
            SELECT 'Enter Valid Program ID' AS Message;
            RETURN;
        END

        IF @Branch_ID IS NOT NULL AND NOT EXISTS (SELECT * FROM Branch WHERE B_ID = @Branch_ID)
        BEGIN
            SELECT 'Enter Valid Branch ID' AS Message;
            RETURN;
        END

        IF @Dept_ID IS NOT NULL AND NOT EXISTS (SELECT * FROM Department WHERE Dept_ID = @Dept_ID)
        BEGIN
            SELECT 'Enter Valid Department ID' AS Message;
            RETURN;
        END

        IF @Track_ID IS NOT NULL AND NOT EXISTS (SELECT * FROM Track WHERE T_ID = @Track_ID)
        BEGIN
            SELECT 'Enter Valid Track ID' AS Message;
            RETURN;
        END

        IF @Course_ID IS NOT NULL AND NOT EXISTS (SELECT * FROM Courses WHERE Cr_ID = @Course_ID)
        BEGIN
            SELECT 'Enter Valid Course ID' AS Message;
            RETURN;
        END

        IF @Ins_ID IS NOT NULL AND NOT EXISTS (SELECT * FROM Instructor WHERE Ins_ID = @Ins_ID)
        BEGIN
            SELECT 'Enter Valid Instructor ID' AS Message;
            RETURN;
        END

        IF @Intake IS NOT NULL AND NOT EXISTS (SELECT * FROM Intakes WHERE Intake = @Intake)
        BEGIN
            SELECT 'Intake does not exist' AS Message;
            RETURN;
        END

        UPDATE Instructor_Assign
        SET 
            Program_ID = COALESCE(@Program_ID, @Old_Program_ID),
            Branch_ID = COALESCE(@Branch_ID, @Old_Branch_ID),
            Dept_ID = COALESCE(@Dept_ID, @Old_Dept_ID),
            Track_ID = COALESCE(@Track_ID, @Old_Track_ID),
            Course_ID = COALESCE(@Course_ID, @Old_Course_ID),
            Ins_ID = COALESCE(@Ins_ID, @Old_Ins_ID),
            Intake = COALESCE(@Intake, @Old_Intake),
            Course_SData = COALESCE(@Course_SDate, @Old_C_SDate),
            Course_EDate = COALESCE(@Course_EDate, @Old_C_EDate)
        WHERE Ins_ID = @Ins_ID 
            AND Program_ID = @Program_ID 
            AND Branch_ID = @Branch_ID 
            AND Dept_ID = @Dept_ID 
            AND Course_ID = @Course_ID 
            AND Ins_ID = @Ins_ID 
            AND Intake = @Intake;

        SELECT 'Instructor Assign updated successfully' AS Message;
    END TRY
    BEGIN CATCH
        SELECT 'An error occurred. Please try again later.' AS Message;
    END CATCH
END;



Execute UpdateInstractorAssign 9,14,9,15,20,3,35,'2023-05-05' ;	



-----------------------------Delete Assign
Create PROCEDURE DeleteInstructorassign
    @Program_ID INT,
    @Branch_ID INT,
    @Dept_ID INT,
    @Track_ID INT,
    @Course_ID INT,
    @Ins_ID INT,
    @Intake INT
AS
BEGIN
    BEGIN TRY
        IF @Program_ID IS NOT NULL AND NOT EXISTS (SELECT * FROM Program WHERE P_ID = @Program_ID)
        BEGIN
            SELECT 'Enter Valid Program ID' AS Message;
            RETURN;
        END

        IF @Branch_ID IS NOT NULL AND NOT EXISTS (SELECT * FROM Branch WHERE B_ID = @Branch_ID)
        BEGIN
            SELECT 'Enter Valid Branch ID' AS Message;
            RETURN;
        END

        IF @Dept_ID IS NOT NULL AND NOT EXISTS (SELECT * FROM Department WHERE Dept_ID = @Dept_ID)
        BEGIN
            SELECT 'Enter Valid Department ID' AS Message;
            RETURN;
        END

        IF @Track_ID IS NOT NULL AND NOT EXISTS (SELECT * FROM Track WHERE T_ID = @Track_ID)
        BEGIN
            SELECT 'Enter Valid Track ID' AS Message;
            RETURN;
        END

        IF @Course_ID IS NOT NULL AND NOT EXISTS (SELECT * FROM Courses WHERE Cr_ID = @Course_ID)
        BEGIN
            SELECT 'Enter Valid Course ID' AS Message;
            RETURN;
        END

        IF @Ins_ID IS NOT NULL AND NOT EXISTS (SELECT * FROM Instructor WHERE Ins_ID = @Ins_ID)
        BEGIN
            SELECT 'Enter Valid Instructor ID' AS Message;
            RETURN;
        END

        IF @Intake IS NOT NULL AND NOT EXISTS (SELECT * FROM Intakes WHERE Intake = @Intake)
        BEGIN
            SELECT 'Intake does not exist' AS Message;
            RETURN;
        END

        DELETE FROM Instructor_Assign
        WHERE Ins_ID = @Ins_ID 
            AND Program_ID = @Program_ID 
            AND Branch_ID = @Branch_ID 
            AND Dept_ID = @Dept_ID 
            AND Track_ID = @Track_ID 
            AND Course_ID = @Course_ID 
            AND Ins_ID = @Ins_ID 
            AND Intake = @Intake;

        SELECT 'Instructor Assign deleted successfully' AS Message;
    END TRY
    BEGIN CATCH
        SELECT 'An error occurred. Please try again later.' AS Message;
    END CATCH
END;


Execute DeleteInstructorassign 9,14,9,15,20,3,35;
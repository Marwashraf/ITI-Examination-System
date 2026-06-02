Create PROCEDURE AddStudentEnrollment
    @Program_ID INT,
    @Branch_ID INT,
    @Dept_ID INT,
    @Track_ID INT,
	@St_ID INT,
    @Intake INT
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

    IF NOT EXISTS (SELECT 1 FROM Track WHERE T_ID = @Track_ID)
    BEGIN
        SELECT 'Enter Valid Track ID' AS Message;
        RETURN;
    END

    IF NOT EXISTS (SELECT * FROM Student WHERE St_ID = @St_ID)
    BEGIN
        SELECT 'Enter Valid Student ID' AS Message;
        RETURN;
    END

    IF NOT EXISTS (SELECT * FROM Intakes WHERE Intake = @Intake)
    BEGIN
        SELECT 'Enter Valid Intake' AS Message;
        RETURN;
    END

   
    INSERT INTO St_Enrollment
    VALUES ( @Program_ID,@Branch_ID,@Dept_ID, @Track_ID,@St_ID, @Intake);

    SELECT 'Student enrollment added successfully' AS Message;
END;


Execute AddStudentEnrollment 4,2,7,14,30,60;


Alter PROCEDURE UpdateStudentEnrollment
   @Program_ID INT,
    @Branch_ID INT,
    @Dept_ID INT,
    @Track_ID INT,
	@St_ID INT,
    @Intake INT
AS
BEGIN
    BEGIN TRY
        DECLARE 
				@Old_Program_ID INT,
                @Old_Branch_ID INT,
                @Old_Dept_ID INT,
                @Old_Track_ID INT,
				@Old_St_ID INT,
                @Old_Intake INT;

        SELECT 
				@Old_Program_ID = Program_ID,
               @Old_Branch_ID = Branch_ID,
               @Old_Dept_ID=Dept_ID,
               @Old_Track_ID = Track_ID,
			   @Old_St_ID = St_ID,
               @Old_Intake = Intake
        FROM St_Enrollment
        WHERE St_ID = @St_ID and Program_ID=@Program_ID and Branch_ID=@Branch_ID and Dept_ID=@Dept_ID and Intake=@Intake;

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

        IF @Intake IS NOT NULL AND NOT EXISTS (SELECT * FROM Track WHERE T_ID = @Track_ID)
        BEGIN
            SELECT 'Enter Valid Track ID' AS Message;
            RETURN;
        END

		IF  @St_ID IS NOT NULL AND NOT EXISTS (SELECT * FROM Student WHERE St_ID = @St_ID)
        BEGIN
            SELECT 'Student ID does not exist' AS Message;
            RETURN;
        END

		IF  @Intake IS NOT NULL AND NOT EXISTS (SELECT * FROM Intakes WHERE Intake = @Intake)
        BEGIN
            SELECT 'Intake does not exist' AS Message;
            RETURN;
        END

        UPDATE St_Enrollment
        SET 
			Program_ID = COALESCE(@Program_ID, @Old_Program_ID),
			Branch_ID = COALESCE(@Branch_ID, @Old_Branch_ID),
            Dept_ID = COALESCE(@Dept_ID, @Old_Dept_ID),
            Track_ID = COALESCE(@Track_ID, @Old_Track_ID),
			St_ID = COALESCE(@St_ID, @Old_St_ID),
            Intake = COALESCE(@Intake, @Old_Intake)
        WHERE St_ID = @St_ID and  Branch_ID = @Branch_ID and Program_ID = @Program_ID and St_ID=@St_ID and Dept_ID=@Dept_ID and Intake=@Intake;

        SELECT 'Student enrollment updated successfully' AS Message;
    END TRY
    BEGIN CATCH
        SELECT 'An error occurred. Please try again later.' AS Message;
    END CATCH
END;



Execute UpdateStudentEnrollment 4,2,7,14,30,35 ;	




Alter PROCEDURE DeleteStudentEnrollment
      @Program_ID INT,
    @Branch_ID INT,
    @Dept_ID INT,
    @Track_ID INT,
	@St_ID INT,
    @Intake INT
AS
BEGIN
    BEGIN TRY
        IF EXISTS (SELECT * FROM St_Enrollment WHERE St_ID = @St_ID AND Branch_ID = @Branch_ID AND Program_ID = @Program_ID AND Track_ID = @Track_ID and 
		Dept_ID=@Dept_ID  and Intake=@Intake)
        BEGIN
            DELETE FROM St_Enrollment
            WHERE St_ID = @St_ID AND Branch_ID = @Branch_ID AND Program_ID = @Program_ID AND Track_ID = @Track_ID and 
			Dept_ID=@Dept_ID  and Intake=@Intake;

            SELECT 'Student enrollment deleted successfully' AS Message;
        END
        ELSE
        BEGIN
            SELECT 'No matching record found to delete' AS Message;
        END
    END TRY
    BEGIN CATCH
        SELECT 'An error occurred. Please try again later.' AS Message;
    END CATCH
END;

Execute DeleteStudentEnrollment 4,2,7,14,30,35;
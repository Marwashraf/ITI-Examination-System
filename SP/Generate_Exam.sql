ALTER PROCEDURE GenerateExam 
    @Intake_ID int,
    @Track_ID int,
    @Crs_ID int,
    @Date date
AS
BEGIN
    -- Check if Intake_ID exists
    IF EXISTS (SELECT * FROM Intakes WHERE Intake = @Intake_ID)
    BEGIN
        -- Check if Track_ID exists
        IF EXISTS (SELECT * FROM Track WHERE T_ID = @Track_ID)
        BEGIN
            -- Check if Crs_ID exists
            IF EXISTS (SELECT * FROM Courses WHERE Cr_ID = @Crs_ID)
            BEGIN
                -- Check if there are enrollments for the specified Intake, Track, and Course
                IF EXISTS (SELECT se.Intake, se.Track_ID, tc.Cr_ID FROM St_Enrollment se
				            JOIN Track_Courses tc ON tc.Track_ID = se.Track_ID
				            WHERE se.Intake = @Intake_ID AND se.Track_ID = @Track_ID AND tc.Cr_ID = @Crs_ID)
				BEGIN
					-- Check if there are no existing exams for the specified date, course, and students
					IF NOT EXISTS (SELECT * FROM Exam WHERE Date = @Date AND Crs_ID = @Crs_ID AND St_ID IN (SELECT St_ID FROM St_Enrollment WHERE Intake = @Intake_ID AND Track_ID = @Track_ID))
					BEGIN
						-- Insert exams for each student enrolled in the specified Intake, Track, and Course
						INSERT INTO Exam (Date, Crs_ID, St_ID)
						SELECT @Date, @Crs_ID, se.St_ID
						FROM St_Enrollment se
						JOIN Track_Courses tc ON tc.Track_ID = se.Track_ID
						WHERE se.Intake = @Intake_ID AND se.Track_ID = @Track_ID AND tc.Cr_ID = @Crs_ID;
                    
						PRINT 'Exams generated successfully.';
					END
					ELSE
					BEGIN
						PRINT 'Exams already exist for the specified date, course, and students.';
					END
				END
				ELSE
				BEGIN
					PRINT 'No enrollments found for the specified Intake, Track, and Course.';
				END
			END
			ELSE
			BEGIN
				PRINT 'Course with ID ' + CAST(@Crs_ID AS varchar(10)) + ' does not exist.';
			END
		END
		ELSE
		BEGIN
			PRINT 'Track with ID ' + CAST(@Track_ID AS varchar(10)) + ' does not exist.';
		END
	END
	ELSE
	BEGIN
		PRINT 'Intake with ID ' + CAST(@Intake_ID AS varchar(10)) + ' does not exist.';
	END
END


GenerateExam @Intake_ID=1,@Track_ID=1,@Crs_ID=10,@Date='2017-03-06';
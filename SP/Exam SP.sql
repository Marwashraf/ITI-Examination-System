Alter PROCEDURE AddExam
    @Duration INT,
    @No_Q INT,
    @Date DATETime,
    @Min_Mark INT,
    @Full_Mark INT,
    @Crs_ID INT,
    @St_Id INT
AS
BEGIN
    BEGIN TRY
        IF NOT EXISTS (SELECT * FROM Student WHERE St_Id = @St_Id)
        BEGIN
            SELECT 'Student does not exist' AS Message;
            RETURN;
        END

        IF NOT EXISTS (SELECT * FROM Courses WHERE Cr_ID = @Crs_ID)
        BEGIN
            SELECT 'Course does not exist' AS Message;
            RETURN;
        END

        -- Insert the exam record
        INSERT INTO Exam
        VALUES ( @Duration, @No_Q, @Date, @Min_Mark, @Full_Mark, @Crs_ID, @St_Id);

        SELECT 'Exam added successfully' AS Message;
    END TRY
    BEGIN CATCH
        SELECT 'An error occurred. Please try again later.' AS Message;
    END CATCH
END;


Execute AddExam 160,20,'2020-02-02',20,40,40,2000;



Alter PROCEDURE UpdateExam
    @Exam_ID INT,
    @Duration INT = NULL,
    @No_Q INT = NULL,
    @Date DATE = NULL,
    @Min_Mark INT = NULL,
    @Full_Mark INT = NULL,
    @Crs_ID INT = NULL,
    @St_Id INT = NULL
AS
BEGIN
    BEGIN TRY
        DECLARE @Old_Duration INT,
                @Old_No_Q INT,
                @Old_Date DATE,
                @Old_Min_Mark INT,
                @Old_Full_Mark INT,
                @Old_Crs_ID INT,
                @Old_St_Id INT;

        IF NOT EXISTS (SELECT * FROM Exam WHERE Exam_ID = @Exam_ID AND St_Id = @St_Id AND Crs_ID = @Crs_ID)
        BEGIN
            SELECT 'Exam does not exist' AS Message;
            RETURN;
        END

        SELECT @Old_Duration = Duration,
               @Old_No_Q = No_Q,
               @Old_Date = Date,
               @Old_Min_Mark = Min_Mark,
               @Old_Full_Mark = Full_Mark,
               @Old_Crs_ID = Crs_ID,
               @Old_St_Id = St_Id
        FROM Exam
		WHERE Exam_ID = @Exam_ID;

        UPDATE Exam
        SET 
            Duration = COALESCE(@Duration, Duration),
            No_Q = COALESCE(@No_Q, No_Q),
            Date = COALESCE(@Date, Date),
            Min_Mark = COALESCE(@Min_Mark, Min_Mark),
            Full_Mark = COALESCE(@Full_Mark, Full_Mark),
            Crs_ID = COALESCE(@Crs_ID, Crs_ID),
            St_Id = COALESCE(@St_Id, St_Id)
        WHERE Exam_ID = @Exam_ID AND St_Id = @St_Id AND Crs_ID = @Crs_ID;

        SELECT 'Exam updated successfully' AS Message;
    END TRY
    BEGIN CATCH
        SELECT 'An error occurred. Please try again later.' AS Message;
    END CATCH
END;



Execute UpdateExam 20 ,@Date='2022-09-09';


CREATE PROCEDURE DeleteExam
    @Exam_ID INT,
    @Crs_ID INT,
    @St_ID INT
AS
BEGIN
    BEGIN TRY
        IF NOT EXISTS (SELECT * FROM Exam WHERE Exam_ID = @Exam_ID AND Crs_ID = @Crs_ID AND St_Id = @St_ID)
        BEGIN
            SELECT 'Exam does not exist' AS Message;
            RETURN;
        END

        DELETE FROM Exam
        WHERE Exam_ID = @Exam_ID AND Crs_ID = @Crs_ID AND St_Id = @St_ID;

        SELECT 'Exam deleted successfully' AS Message;
    END TRY
    BEGIN CATCH
        SELECT 'An error occurred. Please try again later.' AS Message;
    END CATCH
END;



Execute DeleteExam 1,30,1000;
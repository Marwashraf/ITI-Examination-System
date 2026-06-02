Alter PROCEDURE AddQuestion
    @QuestionType VARCHAR(50),
    @Question VARCHAR(1000),
    @Choice_1 VARCHAR(500) = NULL,
    @Choice_2 VARCHAR(500) = NULL,
	@Choice_3 VARCHAR(500) = NULL,
	@Choice_4 VARCHAR(500) = NULL,
    @Correct_Choice VARCHAR(50) = NULL,
    @Crs_Id INT
AS
BEGIN
    BEGIN TRY
        IF NOT EXISTS (SELECT * FROM Courses WHERE Cr_ID = @Crs_Id)
        BEGIN
            SELECT 'Course does not exist' AS Message;
            RETURN;
        END

        IF @QuestionType = 'True/False'
        BEGIN
            SET @Choice_3 = NULL;
            SET @Choice_4 = NULL;

            INSERT INTO Questions (Question_Type, Question, Choice_1, Choice_2, Correct_Choice, Crs_Id)
            VALUES (@QuestionType, @Question, @Choice_1, @Choice_2, @Correct_Choice, @Crs_Id);
        END
        ELSE IF @QuestionType = 'MCQ'
        BEGIN
            IF @Choice_1 IS NULL OR @Choice_2 IS NULL OR @Choice_3 IS NULL OR @Choice_4 IS NULL OR @Correct_Choice IS NULL
            BEGIN
                SELECT 'All choices and correct choice are required for MCQ questions' AS Message;
                RETURN;
            END

            INSERT INTO Questions (Question_Type, Question, Choice_1, Choice_2, Choice_3, Choice_4, Correct_Choice, Crs_Id)
            VALUES (@QuestionType, @Question, @Choice_1, @Choice_2, @Choice_3, @Choice_4, @Correct_Choice, @Crs_Id);
        END
        ELSE
        BEGIN
            SELECT 'Invalid QuestionType' AS Message;
            RETURN;
        END

        SELECT 'Question added successfully' AS Message;
    END TRY
    BEGIN CATCH
        SELECT 'An error occurred. Please try again later.' AS Message;
    END CATCH
END;


EXECUTE AddQuestion 
    @QuestionType = 'True/False',
    @Question = 'rtsdtyfugihj',
    @Choice_1 = 'True',
    @Choice_2 = 'False',
    @Correct_Choice = 'True',
    @Crs_Id = 5;

	

EXECUTE AddQuestion 
    @QuestionType = 'MCQ',
    @Question = 'rtsdtyfugihj',
    @Choice_1 = 'True',
    @Choice_2 = 'False',
	@Choice_3 = 'False',
	@Choice_4 = 'False',
    @Correct_Choice = 'True',
    @Crs_Id = 5;

EXECUTE AddQuestion 
    @QuestionType = 'True/False',
    @Question = 'rtsdtyfugihj',
    @Choice_1 = 'True',
    @Choice_2 = 'False',
	@Choice_3 = 'False',
	@Choice_4 = 'False',
    @Correct_Choice = 'True',
    @Crs_Id = 5;


Create PROCEDURE UpdateQuestion
    @Question_ID INT,
    @QuestionType VARCHAR(50) = NULL,
    @Question VARCHAR(1000) = NULL,
    @Choice_1 VARCHAR(500) = NULL,
    @Choice_2 VARCHAR(500) = NULL,
    @Choice_3 VARCHAR(500) = NULL,
    @Choice_4 VARCHAR(500) = NULL,
    @Correct_Choice VARCHAR(50) = NULL,
    @Crs_ID INT = NULL
AS
BEGIN
    BEGIN TRY
        DECLARE @Old_QuestionType VARCHAR(50),
                @Old_Question VARCHAR(1000),
                @Old_Choice_1 VARCHAR(500),
                @Old_Choice_2 VARCHAR(500),
                @Old_Choice_3 VARCHAR(500),
                @Old_Choice_4 VARCHAR(500),
                @Old_Correct_Choice VARCHAR(50),
                @Old_Crs_ID INT;

        IF NOT EXISTS (SELECT 1 FROM Questions WHERE Q_ID = @Question_ID AND Crs_ID = @Crs_ID)
        BEGIN
            SELECT 'Question does not exist' AS Message;
            RETURN;
        END
        SELECT @Old_QuestionType = Question_Type,
               @Old_Question = Question,
               @Old_Choice_1 = Choice_1,
               @Old_Choice_2 = Choice_2,
               @Old_Choice_3 = Choice_3,
               @Old_Choice_4 = Choice_4,
               @Old_Correct_Choice = Correct_Choice,
               @Old_Crs_ID = Crs_ID
        FROM Questions
        WHERE Q_ID = @Question_ID;

        UPDATE Questions
        SET 
            Question_Type = COALESCE(@QuestionType, @Old_QuestionType),
            Question = COALESCE(@Question, @Old_Question ),
            Choice_1 = COALESCE(@Choice_1, @Old_Choice_1),
            Choice_2 = COALESCE(@Choice_2, @Old_Choice_2),
            Choice_3 = COALESCE(@Choice_3, @Old_Choice_3),
            Choice_4 = COALESCE(@Choice_4, @Old_Choice_4),
            Correct_Choice = COALESCE(@Correct_Choice, Correct_Choice),
            Crs_ID = COALESCE(@Crs_ID, Crs_ID)
        WHERE Q_ID = @Question_ID AND Crs_ID = @Crs_ID;

        SELECT 'Question updated successfully' AS Message;
    END TRY
    BEGIN CATCH 
        SELECT 'An error occurred. Please try again later.' AS Message;
    END CATCH
END;


EXECUTE UpdateQuestion 699,@Crs_ID=5,@Question='llllllll';

CREATE PROCEDURE DeleteQuestion
    @Question_ID INT
AS
BEGIN
    BEGIN TRY
        -- Check if the question exists
        IF NOT EXISTS (SELECT * FROM Questions WHERE Q_ID = @Question_ID)
        BEGIN
            SELECT 'Question does not exist' AS Message;
            RETURN;
        END

        -- Delete the question record
        DELETE FROM Questions
        WHERE Q_ID = @Question_ID;

        SELECT 'Question deleted successfully' AS Message;
    END TRY
    BEGIN CATCH
        SELECT 'An error occurred. Please try again later.' AS Message;
    END CATCH
END;


Execute DeleteQuestion 697;

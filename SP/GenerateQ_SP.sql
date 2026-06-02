CREATE PROCEDURE CheckAndGenerateExamQuestions @Date date,@Cr_Name varchar(100)
AS
BEGIN
    DECLARE @CurrentDate DATETIME;
    SET @CurrentDate = GETDATE();

    DECLARE @ExamDate DATETIME;

    SELECT @ExamDate = MIN(Date)
    FROM Exam e
	join Courses c
	on c.Cr_ID=e.Crs_ID
    WHERE Date >= @Date and Cr_Name=@Cr_Name;

    IF @ExamDate IS NOT NULL
    BEGIN
        PRINT 'An exam is scheduled for ' + CONVERT(VARCHAR(20), @ExamDate) + '. Generating exam questions...'

        Execute GetRandomQuestions @cr_Name

        PRINT 'Exam questions generated successfully.';
    END
    ELSE
    BEGIN
        PRINT 'No exams scheduled after the current date.';
    END
END


CheckAndGenerateExamQuestions '2017-03-06','Operation system';
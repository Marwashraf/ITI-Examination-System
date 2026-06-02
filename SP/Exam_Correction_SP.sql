



Alter PROCEDURE ExamCorrection
    @Exam_ID INT
AS
BEGIN
    -- Check if the provided Exam_ID exists in the Exam table
    IF NOT EXISTS (SELECT 1 FROM Exam WHERE Exam_ID = @Exam_ID)
    BEGIN
        Select ('The provided Exam_ID does not exist in the Exam table.');
    END;

    -- Select data for exam correction
    SELECT e.Exam_ID, e.St_ID, ste.Q_ID, ste.St_Answer, q.Correct_Choice, ste.St_Degree
    FROM Exam e
    JOIN Student_To_Exam ste ON ste.Exam_ID = e.Exam_ID
    JOIN Questions q ON q.Q_ID = ste.Q_ID
    WHERE e.Exam_ID = @Exam_ID;
END;


ExamCorrection 1000;



Create PROCEDURE ExamDegree
    @Exam_ID INT,
    @St_ID INT,
    @Cr_ID INT
AS
BEGIN
    -- Check if the provided St_ID exists in the Student table
    IF NOT EXISTS (SELECT 1 FROM Student WHERE St_ID = @St_ID)
    BEGIN
        Print('The provided St_ID does not exist in the Student table.');
    END;

    -- Check if the provided Cr_ID exists in the Courses table
    IF NOT EXISTS (SELECT 1 FROM Courses WHERE Cr_ID = @Cr_ID)
    BEGIN
        Print('The provided Cr_ID does not exist in the Courses table.');
    END;

    -- Check if the provided Exam_ID exists in the Exam table
    IF NOT EXISTS (SELECT 1 FROM Exam WHERE Exam_ID = @Exam_ID)
    BEGIN
        Print('The provided Exam_ID does not exist in the Exam table.');
    END;

    -- Select data
    SELECT e.Exam_ID,
           s.St_ID,
           CONCAT_WS(' ', s.First_Name, s.Last_Name) AS 'Student Name',
           c.Cr_Name,
           SUM(ste.St_Degree) AS [student degree],
           MAX(ste.Exam_Date) AS [Submit Date]
    FROM Exam AS e
    INNER JOIN Student_To_Exam AS ste ON e.Exam_ID = ste.Exam_ID
    JOIN Student AS s ON s.St_ID = e.St_ID
    JOIN Courses AS c ON c.Cr_ID = e.Crs_ID
    WHERE e.Exam_ID = @Exam_ID AND e.Crs_ID = @Cr_ID
    GROUP BY s.St_ID, CONCAT_WS(' ', s.First_Name, s.Last_Name), c.Cr_Name, e.Exam_ID;
END;


CREATE PROCEDURE ExamAnswers
    @Exam_ID INT
AS
BEGIN
    -- Check if the provided Exam_ID exists in the Exam table
    IF NOT EXISTS (SELECT 1 FROM Exam WHERE Exam_ID = @Exam_ID)
    BEGIN
        Select('The provided Exam_ID does not exist in the Exam table.');
    END;

    -- Select data for the provided Exam_ID
    SELECT e.Exam_ID, e.St_ID, ste.Q_ID, ste.St_Answer
    FROM Exam e
    JOIN Student_To_Exam ste ON ste.Exam_ID = e.Exam_ID
    WHERE e.Exam_ID = @Exam_ID;
END;


ExamAnswers 1000
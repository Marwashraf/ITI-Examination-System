

Alter PROCEDURE Exams_model_SP
    @studentID INT, 
    @courseID INT
AS
BEGIN
    IF EXISTS (SELECT 1 FROM Exam AS e WHERE e.St_ID = @studentID AND e.Crs_ID = @courseID)
    BEGIN
        IF EXISTS (SELECT 1 FROM Student_To_Exam AS ste INNER JOIN Exam AS e ON ste.Exam_ID = e.Exam_ID
                   WHERE e.St_ID = @studentID AND e.Crs_ID = @courseID)
        BEGIN
            SELECT e.Exam_ID, q.Question, q.Correct_Choice, ste.St_Answer, ste.St_Degree
            FROM Questions AS q
            INNER JOIN Student_To_Exam AS ste ON q.Q_ID = ste.Q_ID
            INNER JOIN Exam AS e ON ste.Exam_ID = e.Exam_ID
            WHERE e.St_ID = @studentID AND e.Crs_ID = @courseID;
        END
        ELSE
        BEGIN
            SELECT 'this student has not taken the exam for this course yet!!' AS message;
        END
    END
    ELSE
    BEGIN
        SELECT 'Please enter valid IDs!!' AS message;
    END
END
GO



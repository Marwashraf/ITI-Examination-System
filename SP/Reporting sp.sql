
--------1
Alter Procedure GetDeptStd @Dept_ID VARCHAR(MAX) 
AS
BEGIN
    IF EXISTS (SELECT 1 FROM Department WHERE Dept_ID IN (SELECT value FROM STRING_SPLIT(@Dept_ID, ',')))
    BEGIN
        SELECT 
            s.St_ID,
            s.St_SSN,
            CONCAT_WS(' ', s.First_Name, s.Last_Name) AS 'Full Name',
            s.Gender,
            s.St_Email,
            s.Date_of_Birth,
            s.Graduation_Year,
            s.Phone,
            a.City,
            gt.Team_ID,
            gt.Score,
            gt.P_SDate,
            gt.P_EDate
        FROM 
            student s
        JOIN 
            St_Enrollment se ON se.St_ID = s.St_ID
        JOIN 
            Address a ON a.Address_ID = s.Address_ID
        JOIN 
            Graduation_Team gt ON gt.Team_ID = s.Team_ID
        WHERE 
            Dept_ID IN (SELECT value FROM STRING_SPLIT(@Dept_ID, ','))
    END
    ELSE
        SELECT 'Department ID Does not Exist' AS Message 
END

GetDeptStd '6';


--------2
Alter procedure GetStdDefgree @St_ID VARCHAR(MAX) 
AS
BEGIN
    IF EXISTS (SELECT 1 FROM Student WHERE St_ID IN (SELECT value FROM STRING_SPLIT(@St_ID, ',')))
    BEGIN
        IF EXISTS (SELECT 1 FROM St_Enrollment WHERE St_ID IN (SELECT value FROM STRING_SPLIT(@St_ID, ',')))
        BEGIN
            SELECT 
                se.St_ID,
                Crs_ID,
                c.Cr_Name,
                e.Full_Mark,
                ((SUM(ste.St_Degree)) * 100 / e.Full_Mark) AS ' % Degree'
            FROM 
                St_Enrollment se
            JOIN 
                Exam e ON e.St_ID = se.St_ID
            JOIN 
                Student_To_Exam ste ON ste.Exam_ID = e.Exam_ID
            JOIN 
                Courses c ON c.Cr_ID = e.Crs_ID
            WHERE 
                se.St_ID IN (SELECT value FROM STRING_SPLIT(@St_ID, ','))
            GROUP BY 
                se.St_ID,
                Crs_ID,
                c.Cr_Name,
                e.Full_Mark
        END
        ELSE
            SELECT 'Student ID Does not Exist in St_Enrollment' AS Message
    END
    ELSE
        SELECT 'Student ID Does not Exist' AS Message
END


GetStdDefgree '500,200';



------3
ALTER PROCEDURE TeachingIns 
    @Ins_ID VARCHAR(MAX)
AS
BEGIN
    IF EXISTS (SELECT 1 FROM Instructor WHERE Ins_ID IN (SELECT value FROM STRING_SPLIT(@Ins_ID, ',')))
    BEGIN
        IF EXISTS (SELECT 1 FROM Instructor_Assign WHERE Ins_ID IN (SELECT value FROM STRING_SPLIT(@Ins_ID, ',')))
        BEGIN
            SELECT 
                COUNT(s.St_ID) AS 'No_Student', 
                p.P_Name AS 'Program Name', 
                b.B_Name AS 'Branch Name',
                d.Dept_Name AS 'Department Name', 
                t.T_Name AS 'Track Name', 
                c.Cr_Name AS 'Course Name',
                ia.Ins_ID, 
                CONCAT(ins.First_Name, ' ', ins.Last_Name) AS 'Instructor Name',
                i.*
            FROM 
                St_Enrollment AS ste
            INNER JOIN 
                Track_Courses AS tc ON ste.Track_ID = tc.Track_ID
            INNER JOIN 
                Instructor_Assign AS ia ON ia.Program_ID = ste.Program_ID 
                                        AND ia.Branch_ID = ste.Branch_ID 
                                        AND ia.Track_ID = ste.Track_ID 
                                        AND ia.Course_ID = tc.Cr_ID 
                                        AND ia.Intake = ste.Intake
            JOIN 
                Program p ON p.P_ID = ste.Program_ID
            JOIN 
                Branch b ON b.B_ID = ste.Branch_ID
            JOIN 
                Department d ON d.Dept_ID = ste.Dept_ID
            JOIN 
                Track t ON t.T_ID = ste.Track_ID
            JOIN 
                Student s ON s.st_ID = ste.St_ID
            JOIN 
                Courses c ON c.Cr_ID = tc.Cr_ID
            JOIN 
                Intakes i ON i.Intake = ste.Intake
            INNER JOIN 
                Instructor AS ins ON ins.Ins_ID = ia.Ins_ID
            WHERE 
                ins.Ins_ID IN (SELECT value FROM STRING_SPLIT(@Ins_ID, ','))
            GROUP BY  
                p.P_Name, 
                b.B_Name,
                d.Dept_Name, 
                t.T_Name, 
                c.Cr_Name, 
                ia.Ins_ID, 
                CONCAT(ins.First_Name, ' ', ins.Last_Name),
                i.Intake, 
                i.Start_Date, 
                i.End_Date
        END
        ELSE
            SELECT 'Instructor ID Does not Assign to any Courses' AS Message
    END
    ELSE
        SELECT 'Instructor ID Does not Exist' AS Message
END


TeachingIns '50,100';


------4
ALTER PROCEDURE CoursesTopic 
    @Cr_ID VARCHAR(MAX) 
AS
BEGIN
    IF EXISTS (SELECT 1 FROM Courses WHERE Cr_ID IN (SELECT value FROM STRING_SPLIT(@Cr_ID, ',')))
    BEGIN
        SELECT 
            C.Cr_ID,
            t.*
        FROM 
            Courses c
        JOIN 
            Topic t ON t.Topic_ID = c.Topic_ID
        WHERE 
            c.Cr_ID IN (SELECT value FROM STRING_SPLIT(@Cr_ID, ','))
    END
    ELSE
        SELECT 'Course ID Does not Exist' AS Message
END


CoursesTopic '10,12' ;

----5
ALTER PROCEDURE GetExam 
    @Exam_ID VARCHAR(MAX)
AS
BEGIN
    IF EXISTS (SELECT 1 FROM Exam WHERE Exam_ID IN (SELECT value FROM STRING_SPLIT(@Exam_ID, ',')))
    BEGIN
        SELECT 
            e.Exam_ID,
            ste.Q_ID,
            q.Question,
            q.Choice_1,
            q.Choice_2,
            q.Choice_3,
            q.Choice_4
        FROM 
            Exam e
        JOIN 
            Student_To_Exam ste ON ste.Exam_ID = e.Exam_ID
        JOIN 
            Questions q ON q.Q_ID = ste.Q_ID
        WHERE 
            e.Exam_ID IN (SELECT value FROM STRING_SPLIT(@Exam_ID, ','))
    END
    ELSE
        SELECT 'Exam ID Does not Exist' AS Message
END

GetExam '5,9';



------6
Alter PROCEDURE GetStdExam 
    @Exam_ID INT,
    @St_ID INT
AS
BEGIN
    IF EXISTS (
        SELECT *
        FROM Exam e
        JOIN St_Enrollment se ON se.St_ID = e.St_ID
        WHERE e.Exam_ID = @Exam_ID AND se.St_ID = @St_ID
    )
    BEGIN
        SELECT 
            e.Exam_ID,e.St_ID,
            ste.Q_ID,
            q.Question,
            ste.St_Answer,Q.Correct_Choice,ste.St_Degree
        FROM 
            Exam e
        JOIN 
            Student_To_Exam ste ON ste.Exam_ID = e.Exam_ID
        JOIN 
            Questions q ON q.Q_ID = ste.Q_ID
        JOIN 
            St_Enrollment se ON se.St_ID = e.St_ID
        WHERE 
            e.Exam_ID = @Exam_ID AND se.St_ID = @St_ID;
    END
    ELSE
    BEGIN
        PRINT 'No such exam found for the given student.';
    END
END;

GetStdExam 2,1;


-------7
Alter Procedure GetStdExamReport @St_ID INT
As
Begin 
	if Exists(Select * From Exam Where St_ID=@St_ID)
		Begin
		select s.St_ID,e.Exam_ID,c.Cr_Name,Q.Q_ID,Q.Question,Q.Correct_Choice,ste.St_Answer,ste.St_Degree
		from Exam e
		join Student_To_Exam ste
		on ste.Exam_ID=e.Exam_ID
		join Questions Q
		on Q.Q_ID=ste.Q_ID
		join student s
		on s.St_ID=e.St_ID
		join Courses c
		on c.Cr_ID=e.Crs_ID
		Where e.St_ID=@St_ID
		END
	ELSE
	 Select 'Exam ID Does not Exists '
END

GetStdExamReport 100;


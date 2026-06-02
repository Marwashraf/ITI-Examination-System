Create Procedure  ValidateStudent
AS
Begin
	Select *
	From Student
END;


ValidateStudent;

Create Procedure  ValidateInstructor
AS
Begin
	Select *
	From Instractor
END;

ValidateInstructor


Execute ValidateInstructor 'wseally0@devhub.com','kR5,lbCZ<!W}Vde~';


Alter Procedure GetCourses(@St_ID INT)
AS
Begin
	Select c.Cr_Name,e.Exam_ID
	from St_Enrollment se
	Join Track_Courses tc
	on tc.Track_ID=se.Track_ID
	join Courses c
	on c.Cr_ID=tc.Cr_ID
	join Exam e
	on e.St_ID=se.St_ID and e.Crs_ID=tc.Cr_ID
	Where e.Exam_ID not in (Select Exam_ID From Student_To_Exam) and se.St_ID=@St_ID
END;

Execute GetCourses 865;




Alter Procedure AddStudentQ_D(@Exam_ID INT,@Q_ID INT,@St_Answer Varchar(500),@St_Degree INT)
AS
Begin
	If Exists (select * from Exam where Exam_ID=@Exam_ID )
	Begin 
		INSERT into Student_To_Exam(Exam_ID, Q_ID, St_Answer, St_Degree)
		VALUES (@Exam_ID,@Q_ID,@St_Answer,@St_Degree)
		Select 'Inserted  Successfully' As Message;
	End
	Else
		Select 'Invalid Exam ID' As Message 
END;

Execute AddStudentQ_D 2,1,'wsedrtfyguh',0;



ALTER Procedure InstructorView(@Ins_ID INT)
AS
Begin
  select se.St_ID,CONCAT_WS(' ', s.First_Name, s.Last_Name) AS 'Student Name',c.Cr_Name,p.P_Name,b.B_Name,
  t.T_Name,se.Intake,e.Min_Mark,e.Full_Mark,Sum(ste.St_Degree) as [student degree],max(ste.Exam_Date) as [Submit Date]
  from St_Enrollment as se
  inner join Student s
  on se.St_ID = s.St_ID
  inner join Program as p
  on se.Program_ID = p.P_ID
  inner join Branch as b
  on se.Branch_ID = b.B_ID
  inner join Track as t
  on se.Track_ID = t.T_ID
  inner join Track_Courses as tc 
  on se.Track_ID = tc.Track_ID
  inner join Courses as c
  on tc.Cr_ID = c.Cr_ID
  inner join Instructor_Assign as ia
  on ia.Program_ID = se.Program_ID and ia.Branch_ID = se.Branch_ID and ia.Track_ID = se.Track_ID and ia.Course_ID = tc.Cr_ID and ia.Intake = se.Intake
  inner join Exam as e
  on e.St_ID = se.St_ID and e.Crs_ID = tc.Cr_ID
  inner join Student_To_Exam as ste
  on e.Exam_ID = ste.Exam_ID
  where ia.Ins_ID = @Ins_ID
  group by se.St_ID,CONCAT_WS(' ', s.First_Name, s.Last_Name),c.Cr_Name,p.P_Name,b.B_Name,t.T_Name,se.Intake,ia.Ins_ID,
  e.Min_Mark,e.Full_Mark
END;


Create procedure CalculateStudentDegree @eid int
as
begin 
  if exists (select * from Student_To_Exam st where st.Exam_ID = @eid)
  begin
    select  SUM(ste.St_Degree) as [Your Degree]
    from Student_To_Exam as ste
    where ste.Exam_ID = @eid
    group by ste.Exam_ID
  end
  else
  select 'none has take this Exam' as message
end
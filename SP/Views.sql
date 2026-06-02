
create view std
as
with ques as (
	SELECT q.Q_ID,q.Crs_ID,
	Case when q.Question_Type = 'MCQ' then
	  CASE 
		WHEN RAND() <= 0.25 THEN q.Choice_1
		WHEN RAND() <= 0.5 THEN q.Choice_2
		WHEN RAND() <= 0.75 THEN q.Choice_3
		ELSE q.Choice_4 END
	  else CASE WHEN RAND() <= 0.5 THEN q.Choice_1 ELSE q.Choice_2 END
	  end as st_answer
FROM Questions AS q
WHERE q.Q_ID IN (SELECT TOP 10 q.Q_ID FROM Questions AS q WHERE q.Crs_ID = (
        SELECT TOP 1 e.Crs_ID FROM Exam AS e WHERE Exam_ID NOT IN (
            SELECT ste.Exam_ID FROM Student_To_Exam AS ste)
        ORDER BY NEWID())
		ORDER BY NEWID())
)

select top 10 e.Exam_ID,qs.Q_ID,qs.st_answer, 
case when qs.st_answer = qq.Correct_Choice then 2 else 0
end as st_degree from ques as qs
inner join	Questions qq
on qs.Q_ID = qq.Q_ID
inner join exam e 
on qs.Crs_ID = e.Crs_ID
where e.Exam_ID NOT IN (SELECT ste.Exam_ID FROM Student_To_Exam AS ste)
order by e.Exam_ID


insert into Student_To_Exam
select *, GETDATE()
from std




DECLARE @Counter INT = 0;

WHILE @Counter < 5800
BEGIN
    INSERT INTO Student_To_Exam
    SELECT *, GETDATE()
    FROM std;

    SET @Counter = @Counter + 1;
END;


create view yetExamed
as
select * 
from Exam
where Exam_ID NOT IN (SELECT ste.Exam_ID FROM Student_To_Exam AS ste)





  create view St_Crs_Ins
as
select s.St_ID,Concat(S.First_Name,' ',S.Last_Name) as 'Student Name' , p.P_Name as 'Program Name',b.B_Name as 'Branch Name',
  d.Dept_Name as 'Department Name',t.T_Name as 'Track Name',c.Cr_Name as'Course Name',ia.Ins_ID,Concat(ins.First_Name,' ',ins.Last_Name) as 'Instructor Name',i.*
  from St_Enrollment as ste
  inner join Track_Courses as tc 
  on ste.Track_ID = tc.Track_ID
  inner join Instructor_Assign as ia
  on ia.Program_ID = ste.Program_ID 
 and 
  ia.Branch_ID = ste.Branch_ID 
  and 
  ia.Track_ID = ste.Track_ID 
  and 
  ia.Course_ID = tc.Cr_ID 
  and 
  ia.Intake = ste.Intake
  join Program p
  on p.P_ID=ste.Program_ID
  join Branch b
  on b.B_ID=ste.Branch_ID
  join Department d
  on d.Dept_ID=ste.Dept_ID
  Join Track t
  on t.T_ID=ste.Track_ID
  join student s
 on s.st_ID=ste.St_ID
 join Courses c
 on c.Cr_ID=tc.Cr_ID
 join Intakes i
 on i.Intake=ste.Intake
 inner join Instructor as ins 
 on ins.Ins_ID = ia.Ins_ID




 Create view Exams_model
as
select e.Exam_ID,e.St_ID,e.Crs_ID,q.Question,q.Correct_Choice, ste.St_Answer,ste.St_Degree
from Questions as q
inner join Student_To_Exam as ste
on q.Q_ID = ste.Q_ID
inner join Exam as e
on ste.Exam_ID=e.Exam_ID




----------------------Graduation Fact

select distinct gt.Team_ID, se.Branch_ID, gt.Score
from Graduation_Project gp
join Graduation_Team gt
on gt.Proj_ID=gp.Project_ID
join Student s
on s.Team_ID=gt.Team_ID
join St_Enrollment se
on se.St_ID=s.St_ID
where gt.Team_ID > ?


------------------------Evaluation Fact
select distinct eps.St_ID,ste.Branch_ID,ep.Cr_ID,eps.Score,ste.Dept_ID,ste.Program_ID,ste.Track_ID,ste.Intake,ep.Proj_ID
from St_Enrollment as ste
  inner join Evaluation_P_Student eps
  on ste.St_ID = eps.St_ID
  inner join Evaluation_Projects ep 
  on ep.Proj_ID = eps.Evaluation_P_ID
  inner join Student s 
  on s.St_ID = eps.St_ID
  inner join Track_Courses tc
  on tc.Track_ID = ste.Track_ID and tc.Cr_ID = ep.Cr_ID
  where eps.St_ID > ?

  ---------------------------Examination Fact 
  select se.St_ID, c.Cr_ID, ia.Ins_ID,se.Branch_ID, ste.Exam_ID, s.Address_ID, cast(ste.Exam_Date as date) as datee,t.T_ID,p.P_ID,se.Intake ,sum(ste.St_Degree) as Student_Degree
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
  inner join Exam as e
  on e.St_ID = se.St_ID and e.Crs_ID = tc.Cr_ID
  inner join Student_To_Exam as ste
  on e.Exam_ID = ste.Exam_ID
  inner join Instructor_Assign ia
  on ia.Course_ID = tc.Cr_ID and ia.Branch_ID = se.Branch_ID and ia.Track_ID = se.Track_ID and ia.Program_ID = se.Program_ID and ia.Intake = se.Intake
 where ste.Exam_ID > ?
 group by ste.Exam_ID,se.St_ID,c.Cr_ID,se.Branch_ID, ia.Ins_ID, s.Address_ID, cast(ste.Exam_Date as date),t.T_ID,p.P_ID,se.Intake
ALTER procedure Get_branch_name @bid int
	as
	begin
	select b.B_Name
	from Branch as b
	where b.B_ID = @bid
	end

Get_branch_name 1; 


ALTER procedure Get_course_name @cid int
as
begin
select c.Cr_Name
from Courses as c
where c.Cr_ID = @cid
end


Get_course_name 5;


ALTER procedure Get_instructor_name @iid int
as
begin
	select CONCAT_WS(' ', i.First_Name, i.Last_Name) AS 'Instructor Name'
	from Instructor as i
	where i.Ins_ID = @iid
end

ALTER procedure [dbo].[Get_program_name] @pid int
as
begin
	select p.P_Name
	from Program as p
	where p.P_ID = @pid
end


ALTER procedure Get_student_name @sid int
as
begin
	select CONCAT_WS(' ', s.First_Name, s.Last_Name) AS 'Student Name'
	from Student as s
	where s.St_ID = @sid
end


ALTER procedure Get_track_name @tid int
as
begin
	select t.T_Name
	from Track as t
	where t.T_ID = @tid
end

ALTER Procedure GetCourses(@St_ID INT)
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
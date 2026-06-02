



CREATE Procedure AddStudentQ_D(@Exam_ID INT,@Q_ID INT,@St_Answer Varchar(500),@St_Degree INT)
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







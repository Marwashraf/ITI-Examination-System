select ste.Exam_ID, ste.Q_ID, e.Duration, e.No_Q, e.Date, e.Min_Mark, e.Full_Mark,
        q.Question_Type,q.Question, q.Correct_Choice, ste.St_Answer, ste.St_Degree
  from Student_To_Exam ste
  inner join Exam as e
  on e.Exam_ID = ste.Exam_ID
 inner join Questions q
 on ste.Q_ID = q.Q_ID
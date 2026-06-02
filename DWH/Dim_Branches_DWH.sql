select distinct se.Branch_ID, se.Dept_ID, se.Track_ID,
       se.Program_ID, b.B_Name,
     d.Dept_Name, t.T_Name, t.Capacity, p.P_Name,
     se.Intake, i.Start_Date, i.End_Date
from Branch b inner join  St_Enrollment se
on b.B_ID = se.Branch_ID
inner join Track t
on se.Track_ID = t.T_ID
inner join Department d
on se.Dept_ID = d.Dept_ID
inner join Program p
on se.Program_ID = p.P_ID
inner join Intakes i
on i.Intake = se.Intake

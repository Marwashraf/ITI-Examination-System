select s.St_ID, c.Ct_ID, j.Job_ID, f.Fr_ID,
       gt.Team_ID, s.First_Name, s.Last_Name, s.Graduation_Year,
     s.Gender, s.Date_of_Birth, c.Ct_Name, c.Hours, j.Job_Title,
     j.Hiring_Date, j.Company_Name, j.Salary, j.Job_Type, f.Cost,
     f.Duration, f.Client_Name
from Student s inner join Graduation_Team gt
on s.Team_ID = gt.Team_ID
left join Certificate c
on s.St_ID = c.St_ID
left join Job j
on s.St_ID = j.St_ID
left join Freelance f
on s.St_ID = f.St_ID
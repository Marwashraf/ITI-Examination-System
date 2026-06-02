select distinct gt.Team_ID, se.Branch_ID, gt.Score
from Graduation_Project gp
join Graduation_Team gt
on gt.Proj_ID=gp.Project_ID
join Student s
on s.Team_ID=gt.Team_ID
join St_Enrollment se
on se.St_ID=s.St_ID



select eps.St_ID,ste.Branch_ID,ep.Cr_ID,eps.Score
from St_Enrollment as ste
  inner join Evaluation_P_Student eps
  on ste.St_ID = eps.St_ID
  inner join Evaluation_Projects ep 
  on ep.Proj_ID = eps.Evaluation_P_ID







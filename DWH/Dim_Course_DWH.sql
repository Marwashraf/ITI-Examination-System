SELECT Courses.Cr_ID, Courses.Cr_Name, Topic.Topic_Name, Track_Courses.Hours, 
       Evaluation_Projects.Pro_Name, Evaluation_Projects.Min_Mark, 
     Evaluation_Projects.Full_Mark, Evaluation_Projects.Proj_ID, Topic.Topic_ID, Track_Courses.Track_ID
FROM     Courses  inner JOIN
                  Topic ON Courses.Topic_ID = Topic.Topic_ID left join
                  Track_Courses ON Courses.Cr_ID = Track_Courses.Cr_ID
          left JOIN 
                  Evaluation_Projects ON Courses.Cr_ID = Evaluation_Projects.Cr_ID
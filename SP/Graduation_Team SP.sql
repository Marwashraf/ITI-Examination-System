Alter Procedure AddGraduationTeam (@Score INT,@Grade Varchar(200),@P_SDate Date,@P_EDate Date,@Proj_ID INT)
AS
Begin
	If Exists (Select * From Graduation_Project Where Project_ID=@Proj_ID)
	Begin 
	Insert Into Graduation_Team 
	Values(@Score,@Grade,@P_SDate,@P_EDate,@Proj_ID)
	Select'Inserted Successfully' AS  Message
	END
	Else
	Begin
	Select'Enter Valid Graduation Project ID' AS  Message
	END
END

Execute AddGraduationTeam 100,'VGood','2024-02-13','2024-02-23',1;


ALTER PROCEDURE UpdateGraduationTeam
    @Team_ID INT,
    @Score INT = NULL,
    @Grade VARCHAR(200) = NULL,
    @P_SDate DATE = NULL,
    @P_EDate DATE = NULL,
    @Proj_ID INT = NULL
AS
BEGIN
    BEGIN TRY
        IF EXISTS (SELECT * FROM Graduation_Team WHERE Team_ID = @Team_ID)
        BEGIN
            IF @Proj_ID IS NULL OR EXISTS (SELECT * FROM Graduation_Project WHERE Project_ID = @Proj_ID)
            BEGIN
                DECLARE
                        @Old_Score INT,
                        @Old_Grade VARCHAR(200),
                        @Old_P_SDate DATE,
                        @Old_P_EDate DATE,
                        @Old_Proj_ID INT;

                SELECT 
                       @Old_Score = Score,
                       @Old_Grade = Grade,
                       @Old_P_SDate = P_SDate,
                       @Old_P_EDate = P_EDate,
                       @Old_Proj_ID = Proj_ID
                FROM Graduation_Team
                WHERE Team_ID = @Team_ID;

                UPDATE Graduation_Team
                SET 
                    Score = COALESCE(@Score, @Old_Score),
                    Grade = COALESCE(@Grade, @Old_Grade),
                    P_SDate = COALESCE(@P_SDate, @Old_P_SDate),
                    P_EDate = COALESCE(@P_EDate, @Old_P_EDate),
                    Proj_ID = COALESCE(@Proj_ID, @Old_Proj_ID)
                WHERE Team_ID = @Team_ID;

                SELECT 'Graduation Team updated successfully' AS Message;
            END
            ELSE
            BEGIN
                SELECT 'Enter Valid Project ID' AS Message;
            END
        END
        ELSE
        BEGIN
            SELECT 'Team ID Does Not Exist' AS Message;
        END
    END TRY
    BEGIN CATCH
        SELECT 'An error occurred. Please try again later.' AS Message;
    END CATCH
END;

EXEC UpdateGraduationTeam @Team_ID = 201,@Proj_ID=25;

CREATE PROCEDURE DeleteGraduationTeam
    @Team_ID INT
AS
BEGIN
    IF EXISTS (SELECT * FROM Graduation_Team WHERE Team_ID = @Team_ID)
    BEGIN
        DELETE FROM Graduation_Team
        WHERE Team_ID = @Team_ID;

        SELECT 'Graduation Team ID Deleted successfully' AS Message;
    END
    ELSE
    BEGIN
        SELECT 'Enter Valid Team ID' AS Message;
    END
END;

EXECute DeleteGraduationTeam @Team_ID =201;



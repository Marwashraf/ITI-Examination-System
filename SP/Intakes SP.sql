CREATE PROCEDURE AddIntakes
    @Intake INT,
    @Start_Date DATE,
    @End_Date DATE
AS
BEGIN
    BEGIN TRY
        IF EXISTS (SELECT 1 FROM Intakes WHERE Intake = @Intake)
        BEGIN
            SELECT 'Intake already exists' AS Message;
            RETURN;
        END
        INSERT INTO Intakes
        VALUES (@Intake, @Start_Date, @End_Date);

        SELECT 'Intake added successfully' AS Message;
    END TRY
    BEGIN CATCH
        SELECT 'An error occurred. Please try again later.' AS Message;
    END CATCH
END;


Execute AddIntakes 100,'2020-02-02','2020-04-04';

Alter PROCEDURE UpdateIntakes
    @Intake INT,
    @Start_Date DATE = NULL,
    @End_Date DATE = NULL
AS
BEGIN
    BEGIN TRY
        IF NOT EXISTS (SELECT 1 FROM Intakes WHERE Intake = @Intake)
        BEGIN
            SELECT 'Intake does not exist' AS Message;
            RETURN;
        END
		Declare @Old_SDate date ,@Old_EDate Date;
		Select @Old_SDate=Start_Date , @Old_EDate=End_Date
		From Intakes

        UPDATE Intakes
        SET 
            Start_Date = COALESCE(@Start_Date, Start_Date),
            End_Date = COALESCE(@End_Date, End_Date)
        WHERE Intake = @Intake;

        SELECT 'Intake updated successfully' AS Message;
    END TRY
    BEGIN CATCH
        SELECT 'An error occurred. Please try again later.' AS Message;
    END CATCH
END;



Execute UpdateIntakes 100,@Start_Date='2026-04-04';


CREATE PROCEDURE DeleteIntakes
    @Intake INT
AS
BEGIN
    BEGIN TRY
        IF NOT EXISTS (SELECT 1 FROM Intakes WHERE Intake = @Intake)
        BEGIN
            SELECT 'Intake does not exist' AS Message;
            RETURN;
        END

        DELETE FROM Intakes
        WHERE Intake = @Intake;

        SELECT 'Intake deleted successfully' AS Message;
    END TRY
    BEGIN CATCH
        SELECT 'An error occurred. Please try again later.' AS Message;
    END CATCH
END;


Execute DeleteIntakes 500;
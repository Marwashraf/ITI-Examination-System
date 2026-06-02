-- Insert MCQ Questions
INSERT INTO Questions (QUESTION_TYPE, QUESTION, choice_1, choice_2, choice_3, choice_4, correct_choice,Crs_ID)
VALUES 
('MCQ', 'Which programming language is commonly used for Android app development?', 'Swift', 'Java', 'Objective-C', 'C#', 'Java',6),
('MCQ', 'What does the term "UI" stand for in mobile app development?', 'User Input', 'User Interface', 'Unified Integration', 'User Identification', 'User Interface',6),
('MCQ', 'What is the purpose of a storyboard in iOS app development?', 'To define the app''s user interface layout', 'To manage user authentication', 'To handle background tasks', 'To implement data persistence', 'To define the app''s user interface layout',6),
('MCQ', 'Which of the following is NOT a mobile app distribution platform?', 'Google Play Store', 'Apple App Store', 'GitHub', 'Amazon Appstore', 'GitHub',6),
('MCQ', 'What does the term "APK" stand for in Android app development?', 'Android Package Kit', 'Application Programming Kit', 'Android Project Key', 'Application Package Key', 'Android Package Kit',6),
('MCQ', 'What is the purpose of a manifest file in Android app development?', 'To define the app''s user interface', 'To store user preferences', 'To declare the app''s components and permissions', 'To manage database connections', 'To declare the app''s components and permissions',6),
('MCQ', 'Which programming language is used for iOS app development?', 'Java', 'Swift', 'Kotlin', 'Objective-C', 'Swift',6),
('MCQ', 'What is the purpose of Xcode in iOS app development?', 'To write and debug code', 'To manage version control', 'To design user interfaces', 'To deploy apps to the App Store', 'To write and debug code',6),
('MCQ', 'Which of the following is NOT a popular cross-platform mobile app development framework?', 'React Native', 'Xamarin', 'Flutter', 'AngularJS', 'AngularJS',6),
('MCQ', 'What does the term "API" stand for in the context of mobile app development?', 'Application Programming Interface', 'Application Processing Interface', 'Application Protocol Interface', 'Application Performance Interface', 'Application Programming Interface',6);

-- Insert True/False Questions
INSERT INTO Questions (QUESTION_TYPE, QUESTION,Choice_1,Choice_2,Choice_3,Choice_4,correct_choice,Crs_ID)
VALUES 
('TrueFalse', 'React Native is a framework for building native Android apps.','True','False',Null,Null ,'False',6),
('TrueFalse', 'Firebase is a mobile and web application development platform developed by Google.', 'True','False',Null,Null,'True',6),
('TrueFalse', 'Swift is a programming language primarily used for Android app development.', 'True','False',Null,Null ,'False',6),
('TrueFalse', 'iOS apps can only be developed using Xcode.', 'True','False',Null,Null ,'True',6),
('TrueFalse', 'Flutter is an open-source UI software development kit created by Apple.', 'True','False',Null,Null ,'False',6),
('TrueFalse', 'The APK file format is used for distributing iOS apps.', 'True','False',Null,Null ,'False',6),
('TrueFalse', 'TestFlight is a platform provided by Apple for beta testing iOS apps.', 'True','False',Null,Null ,'True',6),
('TrueFalse', 'Android apps can be developed using both Java and Kotlin programming languages.','True','False',Null,Null ,'True',6),
('TrueFalse', 'GitHub is a popular version control system commonly used for mobile app development.', 'True','False',Null,Null,'True',6),
('TrueFalse', 'Mobile app development involves both frontend and backend development.', 'True','False',Null,Nulls,'True',6);

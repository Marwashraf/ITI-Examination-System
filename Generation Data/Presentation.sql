-- Insert MCQ Questions
INSERT INTO Questions (QUESTION_TYPE, QUESTION, choice_1, choice_2, choice_3, choice_4, correct_choice,Crs_ID)
VALUES 
('MCQ', 'What is a key element of effective presentation design?', 'Using a small font size to fit more content on slides', 'Including as much text as possible to ensure clarity', 'Limiting each slide to one main idea or concept', 'Using complex diagrams and charts to impress the audience', 'Limiting each slide to one main idea or concept',16),
('MCQ', 'What is the recommended maximum number of bullet points per slide in a presentation?', '3', '5', '7', '10', '7',16),
('MCQ', 'Which of the following is a non-verbal communication technique that can enhance a presentation?', 'Speaking quickly to maintain audience engagement', 'Avoiding eye contact to reduce nervousness', 'Using gestures and body language to emphasize key points', 'Reading directly from the slides without looking at the audience', 'Using gestures and body language to emphasize key points',16),
('MCQ', 'What is the purpose of a presentation agenda?', 'To provide a summary of the main points covered in the presentation', 'To outline the structure and flow of the presentation', 'To list all the attendees and their roles', 'To introduce the presenter and establish credibility', 'To outline the structure and flow of the presentation',16),
('MCQ', 'What is a common technique for engaging the audience during a presentation?', 'Speaking monotone to maintain professionalism', 'Asking questions and encouraging participation', 'Reading directly from a script without deviation', 'Using technical jargon to impress the audience', 'Asking questions and encouraging participation',16),
('MCQ', 'What is the purpose of using visual aids in a presentation?', 'To overwhelm the audience with information', 'To distract the audience from the main message', 'To reinforce key points and enhance understanding', 'To hide the presenter''s lack of knowledge', 'To reinforce key points and enhance understanding',16),
('MCQ', 'Which of the following is a best practice for designing effective slides?', 'Using a variety of fonts and colors for visual interest', 'Including lengthy paragraphs of text to provide detailed information', 'Using high-quality images and graphics to support key points', 'Avoiding the use of bullet points to prevent confusion', 'Using high-quality images and graphics to support key points',16),
('MCQ', 'What is the purpose of rehearsal in presentation delivery?', 'To memorize the script word-for-word', 'To ensure the presentation stays within the time limit', 'To eliminate any spontaneity and improvisation', 'To increase confidence and familiarity with the material', 'To increase confidence and familiarity with the material',16),
('MCQ', 'Which of the following is an effective technique for managing nerves before a presentation?', 'Avoiding preparation to maintain spontaneity', 'Taking deep breaths and practicing relaxation techniques', 'Drinking large amounts of caffeine to stay alert', 'Focusing on potential mistakes and negative outcomes', 'Taking deep breaths and practicing relaxation techniques',16),
('MCQ', 'What is the recommended way to handle questions from the audience during a presentation?', 'Interrupt the audience member and answer immediately', 'Deflect the question and move on to the next slide', 'Acknowledge the question and answer it to the best of your ability', 'Dismiss the question as irrelevant and continue with the presentation', 'Acknowledge the question and answer it to the best of your ability',16);

-- Insert True/False Questions
INSERT INTO Questions (QUESTION_TYPE, QUESTION, choice_1, choice_2, Choice_3,Choice_4,correct_choice,Crs_ID)
VALUES 
('TrueFalse', 'An effective presentation should have a clear objective or purpose.', 'True', 'False', Null,Null,'True',16),
('TrueFalse', 'It is important to maintain eye contact with the audience during a presentation to establish rapport.', 'True', 'False', Null,Null,'True',16),
('TrueFalse', 'Rehearsing a presentation can help reduce anxiety and improve delivery.', 'True', 'False', Null,Null,'True',16),
('TrueFalse', 'Using humor appropriately can help engage the audience and make a presentation memorable.', 'True', 'False', Null,Null,'True',16),
('TrueFalse', 'Slides with too much text are effective because they provide detailed information to the audience.', 'True', 'False', Null,Null,'False',16),
('TrueFalse', 'It is acceptable to read directly from slides during a presentation to ensure accuracy.', 'True', 'False', Null,Null,'False',16),
('TrueFalse', 'Visual aids, such as charts and graphs, should be used sparingly to avoid overwhelming the audience.', 'True', 'False', Null,Null,'True',16),
('TrueFalse', 'It is important to adjust the pace of speech and volume to maintain audience engagement.', 'True', 'False', Null,Null,'True',16),
('TrueFalse', 'Using a monotone voice throughout a presentation can help maintain professionalism.', 'True', 'False', Null,Null,'False',16),
('TrueFalse', 'Handling questions from the audience demonstrates competence and knowledge on the topic.', 'True', 'False', Null,Null,'True',16);

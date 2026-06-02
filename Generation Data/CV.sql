-- Insert questions for the CV and Interviewing Skills course into QUESTIONS table
INSERT INTO QUESTIONS (QUESTION_TYPE, QUESTION, choice_1, choice_2, choice_3, choice_4, correct_choice, crs_ID)
VALUES 
('MCQ', 'What does CV stand for?', 'Curriculum Vitae', 'Creative Visualization', 'Critical Vocabulary', 'Content Verification', 'Curriculum Vitae', 23),
('True/False', 'A CV is typically longer than a resume.', 'True', 'False', NULL, NULL, 'True', 23),
('MCQ', 'Which of the following is NOT typically included in a CV?', 'Personal interests', 'Work experience', 'Education history', 'Salary expectations', 'Salary expectations', 23),
('MCQ', 'What is the purpose of a cover letter?', 'To provide a summary of qualifications', 'To request an interview', 'To list job responsibilities', 'To provide references', 'To provide a summary of qualifications', 23),
('True/False', 'It is recommended to customize your CV for each job application.', 'True', 'False', NULL, NULL, 'True', 23),
('MCQ', 'What should be the primary focus of the CV?', 'Relevant skills and experiences', 'Personal hobbies', 'Previous salaries', 'Marital status', 'Relevant skills and experiences', 23),
('MCQ', 'What is a common mistake to avoid when formatting a CV?', 'Using an overly complex design', 'Including a professional summary', 'Organizing information chronologically', 'Using a standard font', 'Using an overly complex design', 23),
('True/False', 'References should always be included on the CV itself.', 'False', 'True', NULL, NULL, 'False', 23),
('MCQ', 'What is a behavioral interview question?', 'Questions that ask about past behavior in specific situations', 'Questions about hypothetical scenarios', 'Questions about technical skills', 'Questions about future career goals', 'Questions that ask about past behavior in specific situations', 23),
('MCQ', 'What is the purpose of the STAR method in interviews?', 'To structure responses to behavioral questions', 'To highlight technical skills', 'To negotiate salary', 'To request feedback', 'To structure responses to behavioral questions', 23),
('True/False', 'A functional resume emphasizes skills and experience rather than chronological work history.', 'True', 'False', NULL, NULL, 'True', 23),
('MCQ', 'What is the purpose of a thank-you letter after an interview?', 'To express gratitude and reiterate interest', 'To decline a job offer politely', 'To request additional information', 'To ask for a higher salary', 'To express gratitude and reiterate interest', 23),
('MCQ', 'Which of the following is NOT a common body language mistake in interviews?', 'Maintaining eye contact', 'Fidgeting', 'Crossing arms', 'Avoiding smiling', 'Maintaining eye contact', 23),
('True/False', 'It is acceptable to arrive late for an interview if you have a valid excuse.', 'True', 'False', NULL, NULL, 'False', 23),
('MCQ', 'What is the purpose of researching a company before an interview?', 'To demonstrate interest and preparation', 'To memorize company history', 'To criticize the company during the interview', 'To ask for a higher salary', 'To demonstrate interest and preparation', 23),
('MCQ', 'What is a common closing question in an interview?', 'Do you have any questions for us?', 'When can I start?', 'Can I work from home?', 'How much vacation time do I get?', 'Do you have any questions for us?', 23),
('True/False', 'It is important to follow up after an interview with a thank-you email or letter.', 'True', 'False', NULL, NULL, 'True', 23),
('MCQ', 'What is the purpose of mock interviews?', 'To practice answering common interview questions', 'To make fun of interviewees', 'To criticize the interviewer', 'To learn about company policies', 'To practice answering common interview questions', 23),
('MCQ', 'Which of the following is NOT a common interview mistake?', 'Being too prepared', 'Lack of confidence', 'Poor body language', 'Not asking questions', 'Being too prepared', 23),
('True/False', 'You should always dress formally for a job interview, regardless of the company culture.', 'True', 'False', NULL, NULL, 'False', 23);
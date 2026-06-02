-- Insert MCQ Questions
INSERT INTO Questions (QUESTION_TYPE, QUESTION, choice_1, choice_2, choice_3, choice_4, correct_choice,Crs_ID)
VALUES 
('MCQ', 'What is a common platform for finding freelance work?', 'LinkedIn', 'Upwork', 'Facebook', 'Amazon', 'Upwork',19),
('MCQ', 'What is a key advantage of freelancing?', 'Stable income', 'Fixed working hours', 'Flexibility', 'Limited growth opportunities', 'Flexibility',19),
('MCQ', 'Which of the following skills is essential for a successful freelance career?', 'Communication', 'Technical expertise', 'Time management', 'All of the above', 'All of the above',19),
('MCQ', 'How do freelancers typically charge for their services?', 'Hourly rate', 'Fixed project fee', 'Retainer fee', 'All of the above', 'All of the above',19),
('MCQ', 'What is a common challenge faced by freelancers?', 'Lack of clients', 'Limited autonomy', 'Lack of accountability', 'Stable income', 'Lack of clients',19),
('MCQ', 'What is the importance of a portfolio for freelancers?', 'It showcases their work and skills', 'It is optional and not necessary', 'It helps them avoid bidding on projects', 'It reduces their credibility', 'It showcases their work and skills',19),
('MCQ', 'How can freelancers effectively manage their finances?', 'By investing in high-risk stocks', 'By setting aside a portion of their income for taxes and savings', 'By spending all earnings immediately', 'By avoiding budgeting', 'By setting aside a portion of their income for taxes and savings',19),
('MCQ', 'What is the significance of networking for freelancers?', 'It has no impact on their career', 'It helps them expand their client base', 'It increases their workload', 'It reduces their credibility', 'It helps them expand their client base',19),
('MCQ', 'How can freelancers ensure timely payment for their services?', 'By not discussing payment terms upfront', 'By waiting for clients to initiate payment', 'By sending invoices promptly and following up', 'By offering discounts for delayed payments', 'By sending invoices promptly and following up',19),
('MCQ', 'What is the importance of setting boundaries as a freelancer?', 'It limits opportunities for growth', 'It helps maintain a healthy work-life balance', 'It reduces productivity', 'It increases client satisfaction', 'It helps maintain a healthy work-life balance',19);

-- Insert True/False Questions
INSERT INTO Questions (QUESTION_TYPE, QUESTION, choice_1, choice_2,Choice_3,Choice_4, correct_choice,Crs_ID)
VALUES 
('TrueFalse', 'Freelancers have the same level of job security as full-time employees.', 'True', 'False', Null,Null,'False',19),
('TrueFalse', 'Freelancers are not responsible for paying taxes on their income.', 'True', 'False', Null,Null,'False',19),
('TrueFalse', 'Freelancers can work from anywhere with an internet connection.', 'True', 'False', Null,Null,'True',19),
('TrueFalse', 'Freelancers do not need to market themselves or their services.', 'True', 'False', Null,Null,'False',19),
('TrueFalse', 'Freelancers do not have access to employee benefits such as health insurance and retirement plans.', 'True', 'False', Null,Null,'True',19),
('TrueFalse', 'Freelancers are not bound by traditional 9-to-5 working hours.', 'True', 'False', Null,Null,'True',19),
('TrueFalse', 'Freelancers cannot specialize in specific industries or niches.', 'True', 'False', Null,Null,'False',19),
('TrueFalse', 'Freelancers are not required to sign contracts with their clients.', 'True', 'False', Null,Null,'False',19),
('TrueFalse', 'Freelancers must handle all aspects of their business, including invoicing and accounting.', 'True', 'False', Null,Null,'True',19),
('TrueFalse', 'Freelancers cannot collaborate with other freelancers or agencies on projects.', 'True', 'False', Null,Null,'False',19);

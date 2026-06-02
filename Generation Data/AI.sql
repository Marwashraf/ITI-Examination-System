-- Insert questions for the AI course into QUESTIONS table
INSERT INTO QUESTIONS (QUESTION_TYPE, QUESTION, choice_1, choice_2, choice_3, choice_4, correct_choice, crs_ID)
VALUES 
('MCQ', 'What does AI stand for?', 'Artificial Intelligence', 'Automated Interaction', 'Advanced Integration', 'Adaptive Interpretation', 'Artificial Intelligence', 27),
('True/False', 'AI systems can learn from data.', 'True', 'False', NULL, NULL, 'True', 27),
('MCQ', 'Which of the following is a subset of AI?', 'Machine Learning', 'Computer Vision', 'Natural Language Processing', 'All of the above', 'All of the above', 27),
('MCQ', 'What is the goal of AI?', 'To create systems that can perform tasks that normally require human intelligence', 'To replace human intelligence', 'To automate all human tasks', 'To make humans obsolete', 'To create systems that can perform tasks that normally require human intelligence', 27),
('True/False', 'AI systems can understand and interpret human emotions.', 'True', 'False', NULL, NULL, 'True', 27),
('MCQ', 'Which of the following is NOT an application of AI?', 'Weather forecasting', 'Image recognition', 'Email communication', 'Speech recognition', 'Email communication', 27),
('MCQ', 'What is an AI algorithm?', 'A set of rules to be followed in calculations', 'A series of manual tasks', 'A decision-making process', 'A program that learns from data', 'A program that learns from data', 27),
('True/False', 'AI algorithms are static and cannot adapt to changing data.', 'False', 'True', NULL, NULL, 'False', 27),
('MCQ', 'What is reinforcement learning?', 'A type of machine learning where an agent learns to make decisions by being rewarded or punished', 'A method for data clustering', 'A technique for linear regression', 'A type of deep learning', 'A type of machine learning where an agent learns to make decisions by being rewarded or punished', 27),
('MCQ', 'Which company is known for developing the AI platform "Watson"?', 'IBM', 'Microsoft', 'Google', 'Amazon', 'IBM', 27),
('MCQ', 'What is Artificial Intelligence?', 'The simulation of human intelligence processes by machines', 'The process of automating tasks', 'The study of computer algorithms', 'The development of hardware components', 'The simulation of human intelligence processes by machines', 27),
('True/False', 'AI can only perform tasks that are explicitly programmed.', 'False', 'True', NULL, NULL, 'False', 27),
('MCQ', 'Which of the following is NOT a subfield of AI?', 'Database Management', 'Machine Learning', 'Natural Language Processing', 'Computer Vision', 'Database Management', 27),
('MCQ', 'What is machine learning?', 'A subset of AI that enables machines to learn from data', 'A method for securing networks', 'A type of computer vision technique', 'A branch of linguistics', 'A subset of AI that enables machines to learn from data', 27),
('True/False', 'Deep learning is a subset of machine learning.', 'True', 'False', NULL, NULL, 'True', 27),
('MCQ', 'What is a neural network?', 'A computational model inspired by the structure of the brain', 'A type of search algorithm', 'A form of natural language processing', 'A data visualization technique', 'A computational model inspired by the structure of the brain', 27),
('MCQ', 'What is reinforcement learning?', 'A type of machine learning where algorithms learn to perform actions to maximize rewards', 'A method for labeling data', 'A technique for compressing images', 'A form of supervised learning', 'A type of machine learning where algorithms learn to perform actions to maximize rewards', 27),
('True/False', 'AI systems can exhibit bias if the training data is biased.', 'True', 'False', NULL, NULL, 'True', 27),
('MCQ', 'What is natural language processing (NLP)?', 'The interaction between computers and human languages', 'A method for encrypting data', 'A technique for database management', 'A type of computer hardware', 'The interaction between computers and human languages', 27),
('MCQ', 'Which programming language is commonly used in AI development?', 'Python', 'Java', 'C++', 'JavaScript', 'Python', 27);

-- Insert MCQ Questions
INSERT INTO Questions (QUESTION_TYPE, QUESTION, choice_1, choice_2, choice_3, choice_4, correct_choice,Crs_ID)
VALUES 
('MCQ', 'What is the primary goal of data preprocessing in data science?', 'To increase the volume of data', 'To reduce the complexity of data', 'To introduce noise into the data', 'To make the data less accessible', 'To reduce the complexity of data',3),
('MCQ', 'Which of the following is NOT a supervised learning algorithm?', 'Decision Trees', 'K-Means Clustering', 'Support Vector Machines', 'Linear Regression', 'K-Means Clustering',3),
('MCQ', 'What does the term "feature engineering" refer to in machine learning?', 'The process of creating new features from existing ones', 'The process of removing features from a dataset', 'The process of visualizing data', 'The process of cleaning data', 'The process of creating new features from existing ones',3),
('MCQ', 'Which statistical measure is used to assess the spread or dispersion of data points in a dataset?', 'Mean', 'Median', 'Variance', 'Standard Deviation', 'Standard Deviation',3),
('MCQ', 'In machine learning, what is the purpose of the validation dataset?', 'To train the model', 'To test the model''s performance', 'To fine-tune hyperparameters', 'To evaluate the model''s generalization ability', 'To fine-tune hyperparameters',3),
('MCQ', 'Which of the following algorithms is used for dimensionality reduction?', 'Linear Regression', 'Logistic Regression', 'Principal Component Analysis (PCA)', 'K-Nearest Neighbors (KNN)', 'Principal Component Analysis (PCA)',3),
('MCQ', 'What is the purpose of regularization techniques in machine learning?', 'To increase model complexity', 'To decrease model complexity', 'To introduce noise into the data', 'To speed up model training', 'To decrease model complexity',3),
('MCQ', 'In natural language processing (NLP), what does TF-IDF stand for?', 'Term Frequency-Inverse Document Frequency', 'Text Feature-Inverse Data Filtering', 'Term Feature-Inverse Data Frequency', 'Text Frequency-Inverse Document Filtering', 'Term Frequency-Inverse Document Frequency',3),
('MCQ', 'Which algorithm is commonly used for image classification tasks in deep learning?', 'Support Vector Machines (SVM)', 'Decision Trees', 'Convolutional Neural Networks (CNN)', 'Random Forests', 'Convolutional Neural Networks (CNN)',3),
('MCQ', 'What does A/B testing involve in data science?', 'Comparing two or more algorithms to identify the best performing one', 'Testing different versions of a product to determine which one performs better', 'Analyzing the correlation between two variables in a dataset', 'Assessing the accuracy of a machine learning model', 'Testing different versions of a product to determine which one performs better',3);

-- Insert True/False Questions
INSERT INTO Questions (QUESTION_TYPE, QUESTION, Choice_1,Choice_2,Choice_3,Choice_4,correct_choice,Crs_ID)
VALUES 
('TrueFalse', 'In machine learning, unsupervised learning algorithms do not require labeled data for training.', 'False','True',Null,Null,'True',3),
('TrueFalse', 'A confusion matrix is used to evaluate the performance of a classifier by comparing predicted and actual values.' ,'False','True',Null,Null,'True',3),
('TrueFalse', 'The K-Means clustering algorithm is used for supervised learning tasks.', 'False','True',Null,Null,'False',3),
('TrueFalse', 'Overfitting occurs when a machine learning model performs well on the training data but poorly on unseen data.','False','True' ,Null,Null,'True',3),
('TrueFalse', 'Ensemble learning involves combining predictions from multiple machine learning models to improve performance.', 'False','True',Null,Null,'True',3),
('TrueFalse', 'Feature scaling is the process of transforming features to have a mean of zero and a standard deviation of one.', 'False','True',Null,Null,'True',3),
('TrueFalse', 'Principal Component Analysis (PCA) can be used for both dimensionality reduction and feature extraction.', 'True','False','True',Null,Null,3),
('TrueFalse', 'In regression analysis, the coefficient of determination (R-squared) measures the proportion of the variance in the dependent variable that is predictable from the independent variables.', 'False','True',Null,Null,'True',3),
('TrueFalse', 'Cross-validation is a technique used to estimate the performance of a machine learning model on unseen data.', 'False','True','True',Null,Null,3),
('TrueFalse', 'Regularization techniques penalize large coefficients in a machine learning model to prevent overfitting.', 'False','True','True',Null,Null,3);

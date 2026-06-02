INSERT INTO Questions (Question_Type  ,question, Choice_1, Choice_2, Choice_3, Choice_4, correct_Choice, Crs_ID)
VALUES 
('MCQ','What is machine learning?', 'The process of transferring knowledge from one domain to another.', 'The practice of using algorithms to parse data, learn from it, and then make a determination or prediction about something in the world.', 'A branch of artificial intelligence that involves the encryption and protection of data.', 'The study of computer algorithms that improve automatically through experience and by the use of data.', 'The practice of using algorithms to parse data, learn from it, and then make a determination or prediction about something in the world.',4),

('MCQ','Which of the following is an example of a supervised learning task?', 'Clustering', 'Dimensionality Reduction', 'Regression', 'Association', 'Regression',4),

('MCQ','What is the main goal of clustering in unsupervised learning?', 'To predict the outcome for a new data point.', 'To find a predictive modeling error.', 'To group a set of objects in such a way that objects in the same group are more similar to each other than to those in other groups.', 'To reduce the number of features in a dataset.', 'To group a set of objects in such a way that objects in the same group are more similar to each other than to those in other groups.',4),

('MCQ','What are neural networks inspired by?', 'Biological neural networks in the human brain.', 'The structure of social networks.', 'The design of computer processors.', 'The behavior of ant colonies.', 'Biological neural networks in the human brain.',4),

('MCQ','What distinguishes deep learning from traditional machine learning?', 'Deep learning algorithms are based on structured data only.', 'Deep learning requires less data to learn.', 'Deep learning is capable of learning from unstructured data through multiple layers of neural networks.', 'Deep learning models are always smaller than traditional machine learning models.', 'Deep learning is capable of learning from unstructured data through multiple layers of neural networks.',4),

('MCQ','What metric would you use to evaluate a models performance on a binary classification problem?', 'Mean Squared Error (MSE)', 'Accuracy', 'k-Means Clustering', 'Principal Component Analysis (PCA)', 'Accuracy',4),

('MCQ','What is overfitting in machine learning?', 'When a model is too simple, barely learning from the training data.', 'When a model performs well on the training data but does not generalize well to unseen data.', 'When the models performance on the training data improves as more data is added.', 'When a model deletes irrelevant features from the dataset.', 'When a model performs well on the training data but does not generalize well to unseen data.',4),

('MCQ','Which algorithm is widely used for classification problems?', 'Linear Regression', 'Decision Trees', 'K-Means Clustering', 'Apriori Algorithm', 'Decision Trees',4),

('MCQ','Why is feature scaling important in machine learning?', 'It speeds up the computation of algorithms.', 'It helps in reducing bias.', 'It is necessary for algorithms that compute distances between data.', 'It increases the accuracy of all machine learning models without exception.', 'It is necessary for algorithms that compute distances between data.',4),

('MCQ','What is the purpose of regularization in machine learning?', 'To fit the model perfectly to the training data.', 'To ensure that the model performs well on the training data only.', 'To prevent the model from overfitting by adding a penalty on the magnitude of coefficients.', 'To increase the number of features in the model to improve its performance.', 'To prevent the model from overfitting by adding a penalty on the magnitude of coefficients.',4)


INSERT INTO Questions (Question_Type  ,question, Choice_1, Choice_2, Choice_3, Choice_4, correct_Choice, Crs_ID)
VALUES 
('MCQ','What is Gradient Descent used for in machine learning?', 'For feature selection.', 'For increasing the size of the training data.', 'For optimizing the parameters of the model to minimize the cost function.', 'For categorizing text into different topics.', 'For optimizing the parameters of the model to minimize the cost function.',4),

('MCQ','What is cross-validation?', 'A technique to evaluate the model on the same portion of data.', 'A technique for assessing how the results of a statistical analysis will generalize to an independent data set.', 'A data visualization technique.', 'A method to increase the speed of the training process.', 'A technique for assessing how the results of a statistical analysis will generalize to an independent data set.',4),

('MCQ','What is a key advantage of using decision trees?', 'They inherently perform feature scaling.', 'They require minimal data preprocessing.', 'They can only be used for binary classification problems.', 'They guarantee the best possible solution.', 'They require minimal data preprocessing.',4),

('MCQ','Why is the Random Forest algorithm considered robust against overfitting?', 'Because it relies on a single decision tree.', 'Because it builds multiple decision trees and merges them together to get a more accurate and stable prediction.', 'Because it uses a very deep decision tree.', 'Because it reduces the dimensionality of the data.', 'Because it builds multiple decision trees and merges them together to get a more accurate and stable prediction.',4),

('MCQ','What is the main principle of Support Vector Machines (SVM)?', 'To minimize the error rate of the model.', 'To classify data by finding the decision boundary that maximizes the margin between the two classes.', 'To cluster the data into groups.', 'To find the mean value of the data points.', 'To classify data by finding the decision boundary that maximizes the margin between the two classes.',4),

('True/False','In machine learning, overfitting occurs when a model learns the detail and noise in the training data to the extent that it performs poorly on new data.', 'True', 'False', Null, Null, 'True',4),

('True/False','Support Vector Machines (SVM) can only be used for binary classification tasks.', 'True', 'False', Null, Null, 'False',4),

('True/False','Gradient Descent is an optimization algorithm used for minimizing the cost function in machine learning models.', 'True', 'False', Null, Null, 'True',4),

('True/False','A Convolutional Neural Network (CNN) is primarily used for time series forecasting.', 'True', 'False', Null, Null, 'False',4);
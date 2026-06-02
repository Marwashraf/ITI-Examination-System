-- Insert MCQ Questions
INSERT INTO Questions (QUESTION_TYPE, QUESTION, choice_1, choice_2, choice_3, choice_4, correct_choice,Crs_ID)
VALUES 
('MCQ', 'Which of the following is a correct way to comment out multiple lines of code in Python?', '// Comment', '/* Comment */', '# Comment', '<!-- Comment -->', '# Comment',9),
('MCQ', 'What is the output of the following code snippet?\nprint(10 % 3)', '3', '0.3333333333333333', '1', '0', '1',9),
('MCQ', 'Which of the following is NOT a valid variable name in Python?', 'myVar', '_myVar', '1stVar', 'MY_VAR', '1stVar',9),
('MCQ', 'What does the `len()` function in Python do?', 'Returns the length of a list, tuple, or string', 'Returns the logarithm of a number', 'Returns the largest element in a list', 'Returns the number of elements in a dictionary', 'Returns the length of a list, tuple, or string',9),
('MCQ', 'Which of the following is used to define a function in Python?', 'func()', 'define func()', 'def func():', 'function func():', 'def func():',9),
('MCQ', 'What is the result of `2 ** 3` in Python?', '5', '6', '8', '16', '8',9),
('MCQ', 'Which statement is used to exit a loop in Python?', 'quit', 'end', 'break', 'continue', 'break',9),
('MCQ', 'What is the output of the following code snippet?\nmy_list = [1, 2, 3, 4, 5]\nprint(my_list[2])', '1', '2', '3', '4', '3',9),
('MCQ', 'What is the purpose of the `strip()` function in Python?', 'To remove leading and trailing whitespace from a string', 'To split a string into a list of substrings', 'To concatenate two strings', 'To find the index of a substring within a string', 'To remove leading and trailing whitespace from a string',9),
('MCQ', 'Which module is used to work with regular expressions in Python?', 'regex', 're', 'regexpy', 'regexp', 're',9);

-- Insert True/False Questions
INSERT INTO Questions (QUESTION_TYPE, QUESTION, choice_1, choice_2, choice_3,Choice_4, correct_choice,Crs_ID)
VALUES 
('TrueFalse', 'Python is a dynamically typed language, meaning you don''t need to declare variable types explicitly.', 'True','False',Null,Null,'True',9),
('TrueFalse', 'Python uses indentation to define code blocks instead of curly braces.', 'True','False',Null,Null,'True',9),
('TrueFalse', 'Python lists are immutable, meaning you cannot change their elements after creation.', 'True','False',Null,Null,'False',9),
('TrueFalse', 'The `append()` method can be used to add elements to a Python list.', 'True','False',Null,Null,'True',9),
('TrueFalse', 'Python is a compiled language, meaning you need to compile your code before executing it.', 'True','False',Null,Null,'False',9),
('TrueFalse', 'A tuple in Python is mutable, meaning you can change its elements after creation.', 'True','False',Null,Null,'False',9),
('TrueFalse', 'Python dictionaries are ordered collections of items.', 'True','False',Null,Null,'True',9),
('TrueFalse', 'Python supports multiple inheritance, allowing a subclass to inherit from more than one superclass.', 'True','False',Null,Null,'True',9),
('TrueFalse', 'The `del` keyword in Python is used to delete variables, lists, or parts of lists.', 'True','False',Null,Null,'True',9),
('TrueFalse', 'The `str()` function in Python is used to convert a value to a string.', 'True','False',Null,Null,'True',9);

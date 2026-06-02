-- Insert questions for the C++ course into QUESTIONS table
INSERT INTO QUESTIONS (QUESTION_TYPE, QUESTION, choice_1, choice_2, choice_3, choice_4, correct_choice, crs_ID)
VALUES 
('MCQ', 'What is the correct syntax for declaring a variable in C++?', 'var x;', 'variable x;', 'x = var;', 'int x;', 'int x;', 26),
('True/False', 'In C++, "++" is the increment operator.', 'True', 'False', NULL, NULL, 'True', 26),
('MCQ', 'What does "cin" represent in C++?', 'Character input', 'Console input', 'Common input', 'Conditional input', 'Console input', 26),
('MCQ', 'Which of the following is a correct way to allocate dynamic memory in C++?', 'malloc()', 'new()', 'allocate()', 'alloc()', 'new()', 26),
('True/False', 'C++ supports multiple inheritance.', 'True', 'False', NULL, NULL, 'True', 26),
('MCQ', 'What is the purpose of the "const" keyword in C++?', 'To define a constant value', 'To declare a function as constant', 'To allocate memory', 'To initialize a variable', 'To define a constant value', 26),
('MCQ', 'What does the "this" pointer represent in C++?', 'It points to the previous object', 'It points to the current object', 'It points to the next object', 'It points to a random object', 'It points to the current object', 26),
('True/False', 'C++ allows for function overloading.', 'True', 'False', NULL, NULL, 'True', 26),
('MCQ', 'Which header file is needed to work with files in C++?', '<iostream>', '<file.h>', '<fstream>', '<stdio.h>', '<fstream>', 26),
('MCQ', 'What is the output of the following code snippet?\n\nint x = 5;\nint y = ++x;', '5', '6', '0', 'Compiler error', '6', 26),
('True/False', 'C++ does not support exception handling.', 'False', 'True', NULL, NULL, 'False', 26),
('MCQ', 'What is the correct way to comment multiple lines in C++?', '/* */', '//', '<!-- -->', '##', '/* */', 26),
('MCQ', 'Which loop in C++ is used to execute a block of code repeatedly?', 'for loop', 'if loop', 'while loop', 'switch loop', 'while loop', 26),
('True/False', 'C++ allows for direct manipulation of memory using pointers.', 'True', 'False', NULL, NULL, 'True', 26),
('MCQ', 'What does the "endl" manipulator do in C++?', 'Ends the line and moves the cursor to the next line', 'Ends the program', 'Ends the loop', 'Ends the function', 'Ends the line and moves the cursor to the next line', 26),
('MCQ', 'What is the purpose of the "static" keyword in C++?', 'To define constants', 'To declare a variable that retains its value between function calls', 'To allocate memory', 'To initialize a variable', 'To declare a variable that retains its value between function calls', 26),
('True/False', 'C++ allows for pass-by-reference in function calls.', 'True', 'False', NULL, NULL, 'True', 26),
('MCQ', 'What is the correct way to declare a pointer in C++?', 'pointer p;', 'int p;', 'p = pointer;', 'int* p;', 'int* p;', 26),
('MCQ', 'Which data type in C++ is used to store a single character?', 'char', 'character', 'chr', 'c', 'char', 26),
('True/False', 'C++ does not support object-oriented programming.', 'False', 'True', NULL, NULL, 'False', 26),
('MCQ', 'What does the "new" operator do in C++?', 'Allocates memory for a variable', 'Deallocates memory', 'Initializes a variable', 'Allocates memory for an array', 'Allocates memory for a variable', 26);
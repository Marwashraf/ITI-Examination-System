-- Insert MCQ Questions
INSERT INTO Questions (QUESTION_TYPE, QUESTION, choice_1, choice_2, choice_3, choice_4, correct_choice,Crs_ID)
VALUES 
('MCQ', 'Which of the following is NOT an essential component of an operating system?', 'Kernel', 'Shell', 'Compiler', 'File System', 'Compiler',10),
('MCQ', 'What is the main function of the operating system''s kernel?', 'To manage system resources and provide essential services', 'To translate high-level programming languages into machine code', 'To organize and store files on disk', 'To execute application software', 'To manage system resources and provide essential services',10),
('MCQ', 'What does CPU scheduling refer to in an operating system?', 'Managing multiple users'' access to the system', 'Allocating system resources to different processes', 'Managing files and directories on disk', 'Translating virtual memory addresses into physical memory addresses', 'Allocating system resources to different processes',10),
('MCQ', 'Which of the following scheduling algorithms gives each process a fixed time slot to execute?', 'First-Come, First-Served (FCFS)', 'Round Robin', 'Shortest Job Next (SJN)', 'Priority Scheduling', 'Round Robin',10),
('MCQ', 'What is the purpose of the "fork()" system call in Unix-like operating systems?', 'To create a new process', 'To terminate a process', 'To wait for a child process to exit', 'To execute a command in a shell', 'To create a new process',10),
('MCQ', 'Which memory management technique allows processes to be swapped in and out of main memory to accommodate more processes than can fit at one time?', 'Paging', 'Segmentation', 'Virtual Memory', 'Fragmentation', 'Virtual Memory',10),
('MCQ', 'What is the purpose of an interrupt in an operating system?', 'To stop the execution of a process', 'To indicate that a process has finished executing', 'To request the attention of the CPU for a specific task', 'To synchronize access to shared resources', 'To request the attention of the CPU for a specific task',10),
('MCQ', 'What is a deadlock in the context of operating systems?', 'A situation where two or more processes are waiting indefinitely for a resource held by each other', 'A situation where a process is waiting for a resource that is already held by another process', 'A situation where a process terminates without releasing allocated resources', 'A situation where a process consumes excessive CPU time', 'A situation where two or more processes are waiting indefinitely for a resource held by each other',10),
('MCQ', 'Which file system feature helps prevent data loss in the event of a system crash by ensuring that updates to critical filesystem structures are written to disk before proceeding with other operations?', 'Journaling', 'Encryption', 'Compression', 'RAID', 'Journaling',10),
('MCQ', 'What is the purpose of a device driver in an operating system?', 'To manage the allocation of system resources', 'To translate high-level programming languages into machine code', 'To facilitate communication between the operating system and hardware devices', 'To execute application software', 'To facilitate communication between the operating system and hardware devices',10);

-- Insert True/False Questions
INSERT INTO Questions (QUESTION_TYPE, QUESTION, choice_1, choice_2,Choice_3,Choice_4, correct_choice,Crs_ID)
VALUES 
('TrueFalse', 'Multitasking refers to the ability of an operating system to execute multiple processes simultaneously on a single processor.', 'True', 'False', Null,Null,'True',10),
('TrueFalse', 'Fragmentation occurs when free memory becomes divided into small, non-contiguous blocks over time.', 'True', 'False', Null,Null,'True',10),
('TrueFalse', 'A process is an instance of a program that is currently executing on the CPU.', 'True', 'False', Null,Null,'True',10),
('TrueFalse', 'A shell is a user interface that allows users to interact with the operating system through a command-line interface only.', 'True', 'False', Null,Null,'False',10),
('TrueFalse', 'A mutex (mutual exclusion) is a synchronization primitive used to protect shared resources from being accessed simultaneously by multiple processes.', 'True', 'False', Null,Null,'True',10),
('TrueFalse', 'Time-sharing operating systems allow multiple users to share the same hardware resources by providing each user with a dedicated processor.', 'True', 'False', Null,Null,'False',10),
('TrueFalse', 'A semaphore is a synchronization primitive that can only take two values: 0 and 1.', 'True', 'False', Null,Null,'False',10),
('TrueFalse', 'A page fault occurs when a requested page is not present in main memory and must be retrieved from secondary storage.', 'True', 'False', Null,Null,'True',10),
('TrueFalse', 'A real-time operating system guarantees that system tasks will be completed within a specified time frame.', 'True', 'False', Null,Null,'True',10),
('TrueFalse', 'Deadlocks can be prevented by ensuring that processes never request more resources than they need.', 'True', 'False', Null,Null,'False',10);

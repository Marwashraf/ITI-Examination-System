-- Insert questions for the Network course into QUESTIONS table
INSERT INTO QUESTIONS (QUESTION_TYPE, QUESTION, choice_1, choice_2, choice_3, choice_4, correct_choice, crs_ID)
VALUES 
('MCQ', 'What does LAN stand for?', 'Local Area Network', 'Large Area Network', 'Longwire Access Network', 'Local Access Node', 'Local Area Network', 25),
('True/False', 'A router operates at the network layer of the OSI model.', 'True', 'False', NULL, NULL, 'True', 25),
('MCQ', 'Which device is used to connect multiple computers in a LAN?', 'Switch', 'Router', 'Modem', 'Bridge', 'Switch', 25),
('MCQ', 'Which protocol is used for secure communication over a network?', 'HTTPS', 'HTTP', 'FTP', 'SMTP', 'HTTPS', 25),
('True/False', 'IP addresses are unique identifiers assigned to each device on a network.', 'True', 'False', NULL, NULL, 'True', 25),
('MCQ', 'What is the purpose of DHCP?', 'To dynamically assign IP addresses to devices', 'To provide secure communication', 'To filter incoming network traffic', 'To translate domain names to IP addresses', 'To dynamically assign IP addresses to devices', 25),
('MCQ', 'Which topology connects all devices in a sequential manner?', 'Bus', 'Star', 'Ring', 'Mesh', 'Bus', 25),
('True/False', 'A firewall is used to prevent unauthorized access to a network.', 'True', 'False', NULL, NULL, 'True', 25),
('MCQ', 'What is the function of an Ethernet cable in a network?', 'To connect devices within a LAN', 'To provide internet access', 'To connect devices wirelessly', 'To amplify network signals', 'To connect devices within a LAN', 25),
('MCQ', 'What is a DNS?', 'Domain Name System', 'Digital Network Service', 'Dynamic Network Server', 'Data Naming System', 'Domain Name System', 25),
('MCQ', 'Which of the following is NOT a type of network?', 'Single Area Network', 'LAN', 'WAN', 'MAN', 'Single Area Network', 25),
('True/False', 'MAC addresses are assigned by the Internet Service Provider (ISP).', 'False', 'True', NULL, NULL, 'False', 25),
('MCQ', 'What does VPN stand for?', 'Virtual Private Network', 'Very Personal Network', 'Virtual Public Network', 'Verified Private Network', 'Virtual Private Network', 25),
('MCQ', 'Which network device forwards data packets to their intended destination?', 'Router', 'Switch', 'Bridge', 'Hub', 'Router', 25),
('True/False', 'UDP is a connection-oriented protocol.', 'False', 'True', NULL, NULL, 'False', 25),
('MCQ', 'Which OSI layer is responsible for data encryption and decryption?', 'Presentation Layer', 'Transport Layer', 'Session Layer', 'Application Layer', 'Presentation Layer', 25),
('MCQ', 'What is the primary purpose of NAT?', 'To translate private IP addresses to public IP addresses', 'To establish secure connections between networks', 'To filter network traffic based on IP addresses', 'To authenticate users on a network', 'To translate private IP addresses to public IP addresses', 25),
('True/False', 'FTP is used for transferring files over a secure connection.', 'False', 'True', NULL, NULL, 'False', 25),
('MCQ', 'Which network device operates at Layer 2 of the OSI model?', 'Switch', 'Router', 'Firewall', 'Hub', 'Switch', 25),
('MCQ', 'What is the maximum data rate of a standard Ethernet connection?', '1 Gbps', '100 Mbps', '10 Gbps', '10 Mbps', '1 Gbps', 25);
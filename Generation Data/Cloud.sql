-- Insert MCQ Questions
INSERT INTO Questions (QUESTION_TYPE, QUESTION, choice_1, choice_2, choice_3, choice_4, correct_choice,Crs_ID)
VALUES 
('MCQ', 'What is the primary benefit of cloud computing?', 'Lower upfront costs', 'Increased security risks', 'Limited scalability', 'Decreased accessibility', 'Lower upfront costs',18),
('MCQ', 'Which of the following is not a cloud service model?', 'Infrastructure as a Service (IaaS)', 'Platform as a Service (PaaS)', 'Software as a Service (SaaS)', 'Mainframe as a Service (MaaS)', 'Mainframe as a Service (MaaS)',18),
('MCQ', 'What is the main characteristic of a public cloud?', 'It is owned and operated by a single organization', 'It is accessible only via a private network', 'It is available to the general public over the internet', 'It is located on-premises within an organization''s data center', 'It is available to the general public over the internet',18),
('MCQ', 'Which cloud deployment model provides the highest level of control and security?', 'Public cloud', 'Private cloud', 'Hybrid cloud', 'Community cloud', 'Private cloud',18),
('MCQ', 'What is autoscaling in cloud computing?', 'Automatically adjusting the number of servers based on demand', 'Automatically upgrading software without human intervention', 'Automatically backing up data to multiple locations', 'Automatically encrypting sensitive data', 'Automatically adjusting the number of servers based on demand',18),
('MCQ', 'Which cloud service model provides virtualized computing resources over the internet?', 'Infrastructure as a Service (IaaS)', 'Platform as a Service (PaaS)', 'Software as a Service (SaaS)', 'Function as a Service (FaaS)', 'Infrastructure as a Service (IaaS)',18),
('MCQ', 'What is a key advantage of cloud storage?', 'Limited accessibility', 'High upfront costs', 'Scalability', 'Limited redundancy', 'Scalability',18),
('MCQ', 'What does the term "multi-tenancy" refer to in cloud computing?', 'Hosting multiple data centers in different geographic locations', 'Sharing computing resources and infrastructure among multiple users or tenants', 'Using multiple cloud providers for redundancy', 'Managing multiple cloud environments simultaneously', 'Sharing computing resources and infrastructure among multiple users or tenants',18),
('MCQ', 'Which cloud service model allows developers to build, deploy, and manage applications without worrying about the underlying infrastructure?', 'Infrastructure as a Service (IaaS)', 'Platform as a Service (PaaS)', 'Software as a Service (SaaS)', 'Function as a Service (FaaS)', 'Platform as a Service (PaaS)',18),
('MCQ', 'What is a key consideration when migrating applications to the cloud?', 'Decreased flexibility', 'Increased control', 'Data security and compliance', 'Lower performance', 'Data security and compliance',18);

-- Insert True/False Questions
INSERT INTO Questions (QUESTION_TYPE, QUESTION, choice_1, choice_2, Choice_3,Choice_4,correct_choice,Crs_ID)
VALUES 
('TrueFalse', 'Cloud computing allows users to access computing resources and services over the internet on a pay-as-you-go basis.', 'True', 'False', Null,Null,'True',18),
('TrueFalse', 'Hybrid cloud is a deployment model that combines public and private clouds to enable data and application portability.', 'True', 'False',Null,Null, 'True',18),
('TrueFalse', 'Cloud storage typically offers unlimited storage capacity without any additional costs.', 'True', 'False', Null,Null,'False',18),
('TrueFalse', 'Cloud computing eliminates the need for organizations to maintain physical hardware and infrastructure on-premises.', 'True', 'False', Null,Null,'True',18),
('TrueFalse', 'Cloud security is the sole responsibility of the cloud provider, and customers have no role in ensuring the security of their data and applications.', 'True', 'False', Null,Null,'False',18),
('TrueFalse', 'Serverless computing, also known as Function as a Service (FaaS), requires developers to manage the underlying infrastructure and servers.', 'True', 'False', Null,Null,'False',18),
('TrueFalse', 'Cloud computing offers unlimited scalability, allowing organizations to easily increase or decrease resources as needed.', 'True', 'False', Null,Null,'True',18),
('TrueFalse', 'Cloud migration involves moving applications and data from on-premises infrastructure to the cloud without any modifications.', 'True', 'False', Null,Null,'False',18),
('TrueFalse', 'Cloud computing is a one-size-fits-all solution, suitable for all types of applications and workloads.', 'True', 'False', Null,Null,'False',18),
('TrueFalse', 'Cloud computing offers built-in disaster recovery capabilities, eliminating the need for organizations to invest in separate backup solutions.', 'True', 'False', Null,Null,'True',18);

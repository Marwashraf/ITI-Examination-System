-- Insert MCQ Questions
INSERT INTO Questions (QUESTION_TYPE, QUESTION, choice_1, choice_2, choice_3, choice_4, correct_choice,Crs_ID)
VALUES 
('MCQ', 'What is a data warehouse?', 'A database designed for operational data processing.', 'A database designed for transactional data processing.', 'A database designed for analytical data processing.', 'A database designed for real-time data processing.', 'A database designed for analytical data processing.',14),
('MCQ', 'Which of the following is not a characteristic of a data warehouse?', 'Subject-oriented', 'Integrated', 'Volatile', 'Time-variant', 'Volatile',14),
('MCQ', 'What is the primary purpose of a data warehouse?', 'To support online transaction processing (OLTP)', 'To support online analytical processing (OLAP)', 'To support real-time data processing', 'To support data entry and retrieval', 'To support online analytical processing (OLAP)',14),
('MCQ', 'What is ETL in the context of data warehousing?', 'Extract, Transfer, Load', 'Extract, Transform, Load', 'Extract, Translate, Load', 'Extract, Transaction, Load', 'Extract, Transform, Load',14),
('MCQ', 'Which of the following is not a component of a typical data warehouse architecture?', 'Data Mart', 'Data Staging Area', 'Data Mining Engine', 'Metadata Repository', 'Data Mart',14),
('MCQ', 'What is a star schema in data warehousing?', 'A schema where multiple fact tables are connected through shared dimensions.', 'A schema where a single fact table is connected to multiple dimension tables.', 'A schema where all tables are normalized to reduce redundancy.', 'A schema where multiple fact tables are connected to each other.', 'A schema where a single fact table is connected to multiple dimension tables.',14),
('MCQ', 'Which of the following is not a data warehouse modeling technique?', 'Star Schema', 'Snowflake Schema', 'Third Normal Form (3NF)', 'Fact Constellation Schema', 'Third Normal Form (3NF)',14),
('MCQ', 'What is a slowly changing dimension (SCD) in a data warehouse?', 'A dimension that changes very rapidly.', 'A dimension that changes at a fixed interval.', 'A dimension that changes slowly over time.', 'A dimension that never changes.', 'A dimension that changes slowly over time.',14),
('MCQ', 'What is the purpose of a data warehouse bus matrix?', 'To define the relationships between fact and dimension tables.', 'To define the granularity of data in the data warehouse.', 'To document the flow of data from source systems to the data warehouse.', 'To document the business processes and metrics that the data warehouse supports.', 'To document the business processes and metrics that the data warehouse supports.',14),
('MCQ', 'What is the role of OLAP in data warehousing?', 'To perform complex mathematical calculations on data.', 'To integrate data from multiple sources into a single repository.', 'To provide fast, interactive access to aggregated data.', 'To automate the extraction, transformation, and loading of data.', 'To provide fast, interactive access to aggregated data.',14);

-- Insert True/False Questions
INSERT INTO Questions (QUESTION_TYPE, QUESTION, choice_1, choice_2,Choice_3,Choice_4, correct_choice,Crs_ID)
VALUES 
('TrueFalse', 'A data warehouse is optimized for online transaction processing (OLTP).', 'True', 'False', Null,Null,'False',14),
('TrueFalse', 'Data warehousing involves the process of extracting, transforming, and loading data into a central repository.', 'True', 'False', Null,Null,'True',14),
('TrueFalse', 'Data marts are subsets of data warehouses that are designed for a specific business function or department.', 'True', 'False', Null,Null,'True',14),
('TrueFalse', 'Dimension tables in a data warehouse contain descriptive attributes about the business entities.', 'True', 'False', Null,Null,'True',14),
('TrueFalse', 'In a snowflake schema, dimension tables are normalized into multiple related tables.', 'True', 'False', Null,Null,'True',14),
('TrueFalse', 'Data mining is a process used in data warehousing to discover patterns and relationships in data.', 'True', 'False', Null,Null,'True',14),
('TrueFalse', 'A star schema is more complex than a snowflake schema.', 'True', 'False', Null,Null,'False',14),
('TrueFalse', 'Fact tables in a data warehouse contain numerical, additive data known as measures.', 'True', 'False', Null,Null,'True',14),
('TrueFalse', 'A data warehouse bus matrix is used to document the flow of data within the ETL process.', 'True', 'False', Null,Null,'False',14),
('TrueFalse', 'Data warehouse design should be driven by business requirements and analytical needs.', 'True', 'False', Null,Null,'True',14);

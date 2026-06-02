-- Insert MCQ Questions
INSERT INTO Questions (QUESTION_TYPE, QUESTION, choice_1, choice_2, choice_3, choice_4, correct_choice,Crs_ID)
VALUES 
('MCQ', 'What does XML stand for?', 'Extensible Markup Language', 'Extraordinary Markup Language', 'Extended Markup Language', 'Exceptional Markup Language', 'Extensible Markup Language',11),
('MCQ', 'Which symbol is used to denote the start and end of an XML element?', '<>', '{}', '[]', '<>', '<>',11),
('MCQ', 'In XML, what is the purpose of an attribute?', 'To define the structure of an element', 'To store text data within an element', 'To provide additional information about an element', 'To specify the ordering of child elements', 'To provide additional information about an element',11),
('MCQ', 'What is the XML declaration used for?', 'To define the root element of an XML document', 'To specify the character encoding of the document', 'To declare namespaces used in the document', 'To indicate the version of XML being used', 'To specify the character encoding of the document',11),
('MCQ', 'Which of the following is a valid XML element?', '<person name="John">', '<name>John</person>', '<person>John</person>', '<person><name>John</name></person>', '<person><name>John</name></person>',11),
('MCQ', 'What is the purpose of CDATA in XML?', 'To define a comment', 'To escape special characters', 'To define a processing instruction', 'To include character data that should not be parsed', 'To include character data that should not be parsed',11),
('MCQ', 'Which XML schema language is commonly used for defining the structure of XML documents?', 'DTD (Document Type Definition)', 'XML Schema', 'XSL (eXtensible Stylesheet Language)', 'XPath (XML Path Language)', 'XML Schema',11),
('MCQ', 'What does XPath stand for?', 'XML Path', 'XML Process', 'XML Parser', 'XML Protocol', 'XML Path',11),
('MCQ', 'Which of the following is NOT a valid XML namespace declaration syntax?', 'xmlns="http://example.com"', 'xmlns:prefix="http://example.com"', 'namespace="http://example.com"', 'xmlns:x="http://example.com"', 'namespace="http://example.com"',11),
('MCQ', 'What is the purpose of XSLT in XML?', 'To define the structure of XML documents', 'To transform XML documents into other formats', 'To query XML documents', 'To validate XML documents against a schema', 'To transform XML documents into other formats',11);

-- Insert True/False Questions
INSERT INTO Questions (QUESTION_TYPE, QUESTION, choice_1, choice_2, Choice_3,Choice_4,correct_choice,Crs_ID)
VALUES 
('TrueFalse', 'XML documents must have a root element.', 'True', 'False', Null,Null,'True',11),
('TrueFalse', 'XML is case-sensitive.', 'True', 'False', Null,Null,'True',11),
('TrueFalse', 'An XML document can contain multiple root elements.', 'True', 'False', Null,Null,'False',11),
('TrueFalse', 'XML attributes must always have a value enclosed in quotation marks.', 'True', 'False', Null,Null,'True',11),
('TrueFalse', 'XML elements can be nested to any depth.', 'True', 'False',Null,Null,'True',11),
('TrueFalse', 'XML documents can include JavaScript code for dynamic behavior.', 'True', 'False',Null,Null,'False',11),
('TrueFalse', 'XML Schema is a DTD replacement and provides more powerful validation capabilities.', 'True', 'False', Null,Null,'True',11),
('TrueFalse', 'XPath expressions are used to navigate through elements and attributes in an XML document.', 'True', 'False', Null,Null,'True',11),
('TrueFalse', 'XML namespaces are used to avoid element name conflicts in XML documents.', 'True', 'False', Null,Null,'True',11),
('TrueFalse', 'XSLT is used for styling and transforming XML documents but cannot be used for data extraction.', 'True', 'False', Null,Null,'False',11);

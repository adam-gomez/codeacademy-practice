 -- Q1: Start by getting a feel for the transaction_data table. What are the column names? id, full_name, email, zip, ip_address
 
 SELECT *
 FROM transaction_data
 LIMIT 10;

-- Q2: Find the full_names and emails of the transactions listing 20252 as the zip code

SELECT full_name, email
FROM transaction_data
WHERE zip = 20252;

-- Q3: ‘Art Vandelay’ for their full name or add a ‘der’ for their middle name

SELECT full_name, email
FROM transaction_data
WHERE full_name = "Art Vandelay" 
  OR full_name LIKE "% der %";

-- Q4: IP address beginning with ‘10.’

SELECT ip_address, email
FROM transaction_data
WHERE ip_address LIKE "10.%";

-- Q5: Find the emails in transaction_data with ‘temp_email.com’ as a domain

SELECT *
FROM transaction_data
WHERE email LIKE "%temp_email.com";

-- Q6: ip address starting with ‘120.’ and their full name starts with ‘John’

SELECT *
FROM transaction_data
WHERE ip_address LIKE "120.%"
  AND full_name LIKE "John%";
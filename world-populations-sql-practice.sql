-- This is the first query:

SELECT DISTINCT year from population_years;
-- DISTINCT year = 2000 - 2010 (inclusive)
-- Add your additional queries below:

SELECT population AS 'Largest Population Size for Gabon'
from population_years
WHERE country = 'Gabon'
ORDER BY population DESC
LIMIT 1;

-- Largest Population Size for Gabon = 1.54526

SELECT country AS 'Country in 2005', population
from population_years
WHERE year = 2005
ORDER BY population
LIMIT 10;

-- 10 Lowest Population Countries ('Niue', 'Falkland Islands (Islas Malvinas)'', 'Montserrat', 'Saint Pierre and Miquelon', 'Saint Helena', 'Nauru', 'Cook Islands', 'Turks and Caicos Islands', 'Virgin Islands,  British', 'Gibraltar')

SELECT DISTINCT country AS 'Countries With Population Over 100M in 2010'
FROM population_years
WHERE population > 100
AND year = 2010;

-- Countries With Population Over 100M in 2010 ('Mexico', 'United States', 'Brazil', 'Russia', 'Nigeria', 'Bangladesh', 'China', 'India', 'Indonesia', 'Japan', 'Pakistan')

SELECT DISTINCT country
FROM population_years
WHERE country LIKE "%islands%";

-- "Islands" Countries ('Cayman Islands', 'Faulkland Islands (Islas Malvinas)', 'Turks and Caicos Islands', 'Virgin Islands, U.S.', 'Virgin Islands, British', 'Faroe Islands', 'Cook Islands', 'Solomon Islands', 'U.S. Pacific Islands')

SELECT *
FROM population_years
WHERE country = 'Indonesia'
AND (year = 2000 
  OR year = 2010
);

-- Difference in population between 2000 and 2010 in Indonesia (242.96834 - 214.67661 = 28.29173)
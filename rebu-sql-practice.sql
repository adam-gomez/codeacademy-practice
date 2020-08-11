/* 
You are a data analyst at REBU, a ridesharing platform. For a project, you were given three tables:

trips - trips information
riders - users data
cars - autonomous cars
*/

-- Let’s examine the three tables.
SELECT * FROM trips;

SELECT * FROM riders;

SELECT * FROM cars;

-- What are the column names?
/*
trips:
- id: starts at 1001, autoincrement, primary key
- date: stored in YYYY-MM-DD format
- pickup: stored in HH:MM 24 hour clock format 
- dropoff: stored in HH:MM 24 hour clock format
- rider_id: 3 digit number, matches riders.id
- car_id: 1 digit number, matches cars.id
- type: text, 'X', 'POOL', or 'XL'
- cost: number with 2 decimal places

riders:
- id: starts at 101, auto increment, primary key
- first: first name
- last: last name
- username: @username
- rating: number with 2 decimal places
- total trips: integer
- referred: integer (some null values)

cars:
- id, starts at 1, auto increment, primary key
- model: TEXT
- OS: TEXT
- status: 'active' or 'maintenance'
- trips_completed: integer
*/

-- Trip Log with trips and users
SELECT *
FROM trips
LEFT JOIN riders
  ON trips.rider_id = riders.id;

-- Trips and cars used during those trips
SELECT *
FROM trips
  JOIN cars
    ON trips.car_id = cars.id;

-- New rider data (riders2). Union of riders and rider2 table
SELECT *
FROM riders
UNION
SELECT *
from riders2;

-- What is the average cost for a trip?
SELECT ROUND(AVG(cost), 2) as 'Average Trip Cost'
FROM trips;

-- Find all the riders who have used REBU less than 500 times!
SELECT *
FROM riders
WHERE total_trips < 500
UNION
SELECT *
FROM riders2
WHERE total_trips < 500;

-- Calculate the number of cars that are active
SELECT COUNT(*) AS "Number of Active Cars"
FROM cars
WHERE status = 'active';

-- Find the two cars that have the highest trips_completed.
SELECT *
FROM cars
ORDER BY trips_completed DESC
LIMIT 2;
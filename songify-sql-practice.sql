-- Songify Introduction
-- In this Code Challenge, you’ll be performing analysis for Songify, a fictional music streaming service. Songify has a “freemium” model, meaning that it offers both a free product and a premium paid product.
/*
You’ll be working with six tables:

plans: A table describing the various monthly subscription plans that Songify offers
- id: a unique identifier for th eplan
- price: the monthly cost of the plan
- description: a description of the plan

users: A table describing both free and paid users of Songify
- id: a unique identifier for each user
- first_name: the first name of the user
- last_name: the last name of the user
- age: the age name of the user
- gender: the gender name of the user

premium_users: A table describing onluy the paid users of Songify
- user_id: a unique identifier for each user (matches id in users)
- membership_plan_id: an ID for which payment plan that iuser is on (matches id in plans)
- purchase_date: the date when the user purchased their premium plan
- cancel_date: the date when the user canceled their plan (which can be 'NULL' if they haven't canceled yet)

songs: A list of all songs available on Songify
- id: a unique identifier for each song
- title: the title of the song
- artist: the artist who recorded the song
- year: the year that the song was released

months: A table with months in the year
- months: the first date of a month

plays: A table describing the songs played by each user on Songify
- user_id: A unique identifier for each user (matches id in users)
- song_id: an ID for which payment plan that user is on (matches id in songs)
- play_date: the date when the user played this song
- play_hour: the hour of day (0-23) when the user played this song
*/

-- Which plans are used by which premium members?
SELECT prem.user_id, plans.description
FROM premium_users AS prem
    JOIN plans 
        ON prem.membership_plan_id = plans.id;

 -- Titles of songs played by each user
SELECT plays.user_id, plays.play_date, songs.title
    FROM plays
        JOIN songs
            ON plays.song_id = songs.id
ORDER BY plays.user_id;

 -- Which users aren't premium users?
SELECT users.id
FROM users
    LEFT JOIN premium_users
        ON users.id = premium_users.user_id
WHERE premium_users.user_id IS NULL;

-- Users who played songs in January, but not February
WITH january AS (
  SELECT *
  FROM plays
  WHERE strftime("%m", play_date) = '01'
),
february AS (
  SELECT *
  FROM plays
  WHERE strftime("%m", play_date) = '02'

)
SELECT january.user_id
FROM january
  LEFT JOIN february
    ON january.user_id = february.user_id
WHERE february.user_id IS NULL;

 -- For each month in months, we want to know if each user in premium_users was active or canceled.

SELECT prem.user_id, prem.purchase_date, prem.cancel_date, months.months
FROM premium_users as prem
  CROSS JOIN months
ORDER BY prem.user_id;

-- Using CASE for clarity
SELECT premium_users.user_id,
  months.months,
  CASE
    WHEN (
      premium_users.purchase_date <= months.months
      )
      AND
      (
        premium_users.cancel_date >= months.months
        OR
        premium_users.cancel_date IS NULL
      )
    THEN 'active'
    ELSE 'not_active'
  END AS 'status'
FROM premium_users
CROSS JOIN months;

-- Songify has added some new songs to their catalog.
SELECT *
FROM songs
UNION 
SELECT *
FROM bonus_songs
LIMIT 10;

-- Besides stacking one table on top of another, we can also use UNION to quickly make a “mini” dataset:
SELECT '2017-01-01' as month
UNION
SELECT '2017-02-01' as month
UNION
SELECT '2017-03-01' as month;

-- The following query will give us the number of times that each song was played:
WITH play_count AS (
  SELECT song_id,
    COUNT(*) AS 'times_played'
  FROM plays
  GROUP BY song_id
)
SELECT songs.title, songs.artist, play_count.times_played
FROM songs
  JOIN play_count
    ON play_count.song_id = songs.id;
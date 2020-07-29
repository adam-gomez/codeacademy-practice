/* 
SELECT *
FROM hacker_news
LIMIT 20;


SELECT title, score
FROM hacker_news
ORDER BY score DESC
LIMIT 5;

Penny Arcade – Surface Pro 3 update	517

Hacking The Status Game	309

Postgres CLI with autocompletion and syntax highlighting	304

Stephen Fry hits out at ‘infantile’ culture of trigger words and safe spaces	282

Reversal: Australian Govt picks ODF doc standard over Microsoft	191

SELECT SUM(score)
FROM hacker_news;

SELECT user, SUM(score)
FROM hacker_news
GROUP BY user
HAVING SUM(score) > 200;

SELECT ROUND(((SELECT SUM(total)
        FROM (
          SELECT user, SUM(score) AS "total"
          FROM hacker_news
          GROUP BY user
          HAVING SUM(score) > 200
        ) AS group_hacker
)
/ (6366.0) * 100), 2) AS 'Percentage';

SELECT user, count(*)
FROM hacker_news
WHERE url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
GROUP BY user;


SELECT CASE
  WHEN url LIKE "%github.com%" THEN "GitHub"
  WHEN url LIKE "%medium.com%" THEN "Medium"
  WHEN url LIKE "%nytimes.com%" THEN "NYTimes"
  ELSE 'Other'
  END AS 'Source', COUNT(*) 
FROM hacker_news
GROUP BY 1;


SELECT timestamp, strftime('%H', timestamp)
FROM hacker_news
GROUP BY 1
LIMIT 20;



SELECT strftime('%H', timestamp) AS 'Hours', AVG(score), COUNT(*)
FROM hacker_news
GROUP BY 1
ORDER BY 2 DESC;
*/
SELECT strftime('%H', timestamp) AS 'hours', ROUND(AVG(score)) AS "average_score", COUNT(*) AS 'number_of_articles'
FROM hacker_news
WHERE timestamp IS NOT NULL
GROUP BY 1
ORDER BY 2 DESC;
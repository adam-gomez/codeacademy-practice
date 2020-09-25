-- BUILD A FUNNEL FROM A SINGLE TABLE
/* 
Mattresses and More users were asked to answer a five-question survey:

“How likely are you to recommend Mattresses and More to a friend?”
“Which Mattresses and More location do you shop at?”
“How old are you?”
“What is your gender?”
“What is your annual household income?”

However, not every user finished the survey!

We want to build a funnel to analyze if certain questions prompted users to stop working on the survey.

We will be using a table called survey_responses with the following columns:

question_text - the survey question
user_id - the user identifier
response - the user answer
*/

SELECT *
FROM survey_responses
LIMIT 10;

SELECT question_text, COUNT(DISTINCT user_id)
FROM survey_responses
GROUP BY question_text;

/*
Question 1 - 500
Question 2 - 475
Question 3 - 380
Question 4 - 361
Question 5 - 270

Question 1 - 100% completion
Question 2 - 95% completion out of those completing question 1
Question 3 - 82% completion out of those completing question 2
Question 4 - 95% completion out of those completing question 3
Question 5 - 74% completion out of those completing question 4

It appears that question 3 and 5 may be asking for information many users deem too sensitive to provide
*/

/*
The Product team at Mattresses and More has created a new design for the pop-ups that they believe will lead more users to complete the workflow.

They’ve set up an A/B test where:

50% of users view the original control version of the pop-ups
50% of users view the new variant version of the pop-ups
Eventually, we’ll want to answer the question:

How is the funnel different between the two groups?

We will be using a table called onboarding_modals with the following columns:

user_id - the user identifier
modal_text - the modal step
user_action - the user response (Close Modal or Continue)
ab_group - the version (control or variant)
*/
SELECT * 
FROM onboarding_modals
LIMIT 10;

-- the number of users completing each step of the funnel.
SELECT modal_text, COUNT(DISTINCT user_id)
FROM onboarding_modals
GROUP BY modal_text
ORDER BY modal_text;
/*
Modal 1 - 1000
Modal 2 - 695
Modal 3 - 575
Modal 4 - 447
Modal 5 - 379
*/

-- returns the count of distinct users whose ab_group value is ‘control’
SELECT modal_text, 
        COUNT(DISTINCT CASE WHEN ab_group = 'control' THEN user_id END) AS 'control_clicks'
FROM onboarding_modals
GROUP BY modal_text
ORDER BY modal_text;
/*
CONTROL
Modal 1 - 500
Modal 2 - 301
Modal 3 - 239
Modal 4 - 183
Modal 5 - 152
*/

-- Expands the query to also include variant ab_group value
SELECT modal_text, 
        COUNT(DISTINCT CASE WHEN ab_group = 'control' THEN user_id END) AS 'control_clicks', 
        COUNT(DISTINCT CASE WHEN ab_group = 'variant' THEN user_id END) AS 'variant_clicks'
FROM onboarding_modals
GROUP BY modal_text
ORDER BY modal_text;

/*
VARIANT
Modal 1 - 500
Modal 2 - 394
Modal 3 - 336
Modal 4 - 264
Modal 5 - 227
*/

/*
PERCENTILE ANALYSIS
Modal 1: Control - 100%; Variant - 100%
Modal 2: Control - 60%; Variant - 79%
Modal 3: Control - 80%; Variant - 85%
Modal 4: Control - 80%; Variant - 80%
Modal 5: Control - 85%; Variant - 85%

It appears that the variant pop ups are performing better than the control.
*/


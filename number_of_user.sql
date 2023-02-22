/*To write a SQL query that returns the number of users who logged in during a specific time period, you can use the COUNT function and the BETWEEN operator to filter the results based on the login time. Here is an example query:
*/
SELECT COUNT(DISTINCT user_id) AS num_users
FROM login_data
WHERE login_time BETWEEN '2022-01-01 00:00:00' AND '2022-01-31 23:59:59';

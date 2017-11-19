# Log Analysis Project
_______
In this project the task is to create an internal reporting tool that will use information contained in a database using python and postgresql.
# Pre-requisites
- Python2 or Python3
- psycopg2
- postgresql 9.5.8

# Setup:
Step 1. Load the data onto the database:
```psql -d news -f newsdata.sql```
Step 2. connect to database:
```psql -d news```
Step 3.  create views
 
# Create Your Views
```
create view article_view AS 
SELECT title, author, count(*) AS views from articles, log 
WHERE log.path like concat('%', articles.slug) GROUP BY articles.title, articles.author 
ORDER BY views desc;
```

```
create view error_log_view AS 
SELECT date(time), round(100.0*sum(case log.status when '200 OK' 
then 0 else 1 end)/count(log.status),2) AS "Percent Error" FROM log GROUP BY date(time) 
ORDER BY "Percent Error" desc;
  ```

# Run Module
```python newsdb.py```

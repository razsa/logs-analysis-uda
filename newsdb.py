#! /usr/bin/env python3
import psycopg2

DBNAME = 'news'

# What are the most popular three articles of all time?
sql_articles = 'select title, views from article_view limit 3'

# Who are the most popular article authors of all time?
sql_authors = '''select authors.name, sum(article_view.views) as views from
article_view, authors where authors.id = article_view.author
group by authors.name order by views desc'''

# On which days did more than 1% of requests lead to errors?
sql_error = 'select * from error_log_view where \"Percent Error\" > 1'

# To store results
q_one = dict()
q_one['title'] = '\n1. The 3 most popular articles of all time are:\n'

q_two = dict()
q_two['title'] = '''\n2. The most popular article authors of
all time are:\n'''

q_three = dict()
q_three['title'] = '''\n3. Days with more than 1% of request that
lead to an error:\n'''


# Returns query result
def get_query(query):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results


def display_authicles(return_authicles):
    print((return_authicles['title']))
    for authicles in return_authicles['results']:
        print(('\t\"{0}\" - {1} views'.format(authicles[0], authicles[1])))


def display_error(return_error):
    print((return_error['title']))
    for error in return_error['results']:
        print(('\t{0} - {1} views'.format(error[0], error[1])))

if __name__ == '__main__':
    # Stores query result
    q_one['results'] = get_query(sql_articles)
    q_two['results'] = get_query(sql_authors)
    q_three['results'] = get_query(sql_error)

# Print formatted output
display_authicles(q_one)
display_authicles(q_two)
display_error(q_three)

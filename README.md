# news-togo

## Problem 
Eye strain is a problem for me, and using electronics in the morning will often times cause eye strain later in the day. On top of that, Students don't read the news! It seems like a lot of university students get their news from social media sites like Facebook,  Reddit, Twitter, etc. That just isn't enough for students who are searching for internships or full-time opportunities, since they need to be caught up with current events(especially finance, business, economics majors). For a lot of students, reading the news feels like homework assignment. These two things conflicted for me, as most people often read the news in the morning, on an electronic device. I started development of this web application in hopes that it would help eye-strain conscious people like be able to read the news while minimizing view time of electronic devices. (Without considering a physical newspaper subscription)


## Objective
Create an application that generates a pdf of new articles summarized, with a QR-code next to the summary that links to the full article. Along the way, i hope to develop my programming abilities, work on git workflow, as well as practice data scraping, data modeling, data analysis and application development. 

## Technologies
- Web Framework : Flask http://flask.palletsprojects.com/en/1.1.x/
- Object-relational Mapper : SQLAlchemy https://www.sqlalchemy.org/
- Database Connector : psycopg https://pypi.org/project/psycopg2/
- Relational Database : PostgresSQL https://www.postgresql.org

## Deployment 
Deployment will be done via Heroku https://www.heroku.com/



### Other Misc stuff
Package Manager : pipenv https://pipenv.readthedocs.io/en/latest/

### Development
To install all dependencies
`pipenv install`

To run flask server
`pipenv run flask run`

# Movie-Data-Pipline
This project is a database that stores movies using PostgreSQL as the backend and Python to interact with it on Mac. 

## Software
- Homebrew 5.0.0
- PostgreSQL 14.19 (Homebrew)
- Visual Studio Code
- Python 3.14.0

## Installing Dependencies and Setting up the Database on Mac Terminal
1. Install Homebrew
   Run this code to install Homebrew in the Mac Terminal: \
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" \
   To verify if Hombrew was installed, run: \
   brew --version
   
3. Install PostgreSQL
   Run this code in the Mac Terminal to install PostgreSQL: \
   brew install postgresql \
   To start PostgreSQL run: \
   brew services start postgresql \
   To connect to PostgreSQL run: \
   psql postgres \
   If you get "postgres=#" prompt, it is running successfully. \
   You can verfiy your connection with "\l" to list all databases and "\du" to list all users/roles.

4. Create Movie Database
   Run this code in the Mac Terminal to create the movie database (Your prompt should be "postgres=#"): \
   CREATE DATABASE movie_db; \
   Run this code to connect to it: \
   \c movie_db \
   You should see: \
   You are now connected to database "movie_db" as user "yourusername". \
   To disconnect from PostgreSQL, run: \
   \q

5. Connect Python to PostgreSQL
   In the Mac Termincal, not in PostgreSQL, run: \
   pip install psycopg2-binary \

   TBC...
   
   



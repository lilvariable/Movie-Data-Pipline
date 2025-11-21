# Movie-Data-Pipline
This project is a database that stores movies using PostgreSQL as the backend and Python to interact with it on Mac. 

## Software
- Homebrew 5.0.0
- PostgreSQL 14.19 (Homebrew)
- Visual Studio Code
- Python 3.14.0

## Set up Python Environment in Visual Studio Code
1. In the VS Code terminal run: \
   python3 -m venv movie_env \
   source movie_env/bin/activate \
2. Install required Python packages \
   In the VS Code terminal run: \
   pip install pandas requests sqlalchemy psycopg2 apache-airflow

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
   In the Mac Termincal, not in PostgreSQL, run (if not already installed): \
   pip install psycopg2-binary \
   In your VS Code workspace, run the file "connect_postgresql.py" to connect Python to PostgreSQL ! Make sure to replace "user" with your own username on Mac ! \
   If it worked, you should see: \
   ✅ Connected to PostgreSQL successfully! \
   PostgreSQL version: ('PostgreSQL 17.x on arm64-apple-darwin, compiled by ...',) \
   🔒 Connection closed. \

   Next, run in VS Code "create_tables.py" to create the tables for your database /
   If it worked, you should see: \
   ✅ All tables created successfully! \
   🔒 Connection closed. \

   Inside your Mac Terminal, in PostgreSQL, run: \
   \dt \
   You should see the tables created. \

   After that, in VS Code, run "db_functions.py" to create the Python functions you will use to interact with your database in PostgreSQL \

   Finally, you can run "test_db" to test your database and add more movies as you wish. \

   ## Last Few Comments
   - In your Mac Terminal, run "psql postgresql" to connect to PostgreSQL \
   - To disconnect from PostgreSQL, run "\q" \
   - Make sure to change your "user" in each of the python files to your Mac username to make sure no errors occur when running the files.
  
   # Thank you for reading

   

   

   
   



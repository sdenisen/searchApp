# searchApp

### Deployment:

Minimum working searchApp instance consists of 2 parts:
- Web Application (Django based)
- sqlite database

#### Local Django web instance setup via cli and Pycharm:

1. Open command line, go to git_repository; 

2. Type "git clone https://github.com/sdenisen/searchApp.git"

3. Start Pycharm. File -> Open choose 'searchApp' folder.

4. Go to: Setting -> Project -> Project Interpreter
    - Create new Virtual Env (based on python3.7+)

3. Run in terminal in venv context
    - `pip install -r requirements.txt`

#### Create DataBase:
1. Copy excel table to searchApp/equipment_parts/data/ folder.
   The table with one sheet that contains 2 columns with names: "asv_id",  "full_name".
   Expected file name: "excel_data.xlsx"
   
2. Execute python file: python convert_excel_to_sqlite_db.py (will be created db.sqlite3 file).

3. Make sure that the db.sqlite3 file will be placed in root folder of project.
 
#### Verify:
4.  Run -> Edit configuration
    - Set `Host` to `0.0.0.0` so it will be available from all interfaces

6. Open `http://127.0.0.1:8000/` in browser
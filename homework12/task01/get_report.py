"""(*) optional task: write standalone script (get_report.py)
that retrieves and stores the following information into CSV file report.csv
for all done (completed) homeworks:
     Student name (who completed homework)
     Creation date
     Teacher name who created homework
"""
import sqlite3

import pandas as pd

conn = sqlite3.connect(
    "main.db")
db_df = pd.read_sql_query(
    "SELECT polls_student.first_name || ' ' || polls_student.last_name as student_name, created as creation_date, polls_teacher.first_name || ' ' || polls_teacher.last_name as teacher_name FROM polls_homeworkresult JOIN polls_teacher ON homework_done_id = polls_homeworkresult.id JOIN polls_student ON polls_student.id = author_id WHERE solution IS 'Done'",  # noqa: E501
    conn,
)
db_df.to_csv("report.csv", index=False)

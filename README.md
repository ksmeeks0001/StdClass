# StdClass
Allow dot access from a python dictionary

example

```python
from datetime import datetime
from decimal import Decimal

from StdClass import StdClass

# dictionary
customer_dict = {
    'name': 'Kevin',
    'timestamp': datetime.now(),
    'purchases': [
        {
            'item_name': 'Gatorade',
            'price': Decimal('1.27')
        },
        {
            'item_name': 'Chocolate Bar',
            'price': Decimal('.99')
        }

    ]

}

customer_class = StdClass(customer_dict)

# dot access on attributes
print(customer_class.name)

# key access remains
print(customer_class['name'])

# classes are created recursively
for purchase in customer_class.purchases:
    print(purchase.item_name, purchase.price)
```

Using MySQLCursorStdClass allows dot access on returned rows

```python
import mysql.connector

from MySQLCursorStdClass import MySQLCursorStdClass

dbconn = mysql.connector.connect(**db_args)
cursor = MySQLCursorStdClass(dbconn)

cursor.execute("""
    select 
        StudentName,
        CourseName,
        SemesterName,
        Grade,
        timestamp
    from CourseGrades
    ;
    """
    )
    
 for row in cursor.fetchall():
    print(row.StudentName, row.CourseName, row.SemesterName, row.Grade)
    
```

You can also easily add methods to your classes by deriving from StdClass

These classes can be used directly or with the database

```python

class CourseGrade(StdClass):

    def get_avg_grade(self):
        return (self.Spring + self.Fall) / 2

dbconn = mysql.connector.connect(**db_args)
cursor = MySQLCursorStdClass(dbconn, class_name=CourseGrade)

cursor.execute("""
        Select
            b.StudentName,
            d.CourseName,
            sum(if(c.SemesterName = 'Spring', a.Grade, 0)) as Spring,
            sum(if(c.SemesterName = 'Fall', a.Grade, 0)) as Fall
        From CourseGrades as a
        Join Students as b using(StudentID)
        Join Semesters as c using(SemesterID)
        Join Courses as d using(CourseID)
        group by StudentName, CourseName
        order by StudentName, CourseName
    ;
    """
    )
    
for row in cursor.fetchall():
    print(row.StudentName, row.CourseName, row.Spring, row.Fall, row.get_avg_grade())
    
 ```
        


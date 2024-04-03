# Ex02 Django ORM Web Application
## Date: 3/04/24

## AIM
To develop a Django application to store and retrieve data from a Book database using Object Relational Mapping(ORM).

## Entity Relationship Diagram

Include your ER diagram here

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM:

DEVELEOPED BY: MOHAMMED SAAJID S
REGISTER NUMBER: 212223240093

### admin.py

```
from django.contrib import admin
from .models import Book
admin.site.register(Book)
```

### models.py

```
from django.db import models as m

class Book(m.Model):
    bookid = m.IntegerField()
    bookname = m.CharField(max_length=20)
    bookdept = m.CharField(max_length=20)
    bookcategory = m.CharField(max_length=20)
```

## OUTPUT

![webex2](https://github.com/Mohammed-Saajid/ORM/assets/141727149/3a474c16-1f01-4d8c-b8e0-683c398fdc92)

![webex2i](https://github.com/Mohammed-Saajid/ORM/assets/141727149/8126c3eb-07e0-4b11-816e-09f829854478)

![webex2ii](https://github.com/Mohammed-Saajid/ORM/assets/141727149/aa341145-c3c8-44ae-8ee2-8423ead0fe6d)



## RESULT
Thus the program for creating a database using ORM hass been executed successfully

Overview:
  This app was developed for the purpose of storing academic files, sorted by departments and courses.
  Users can  navigate the site directory, search and sort files, as well as upload, download, and rate files.
  Admins can additionally create and remove courses, departments, and files. This is a Django Web App, deployed 
  through AWS S3, using django-star-ratings and django-watson.

Architecture:
  This app uses 3 classes: Academic_dept(models.Model), Academic_class(models.Model), and Upload(models.Model).
  Academic_dept is at the top of the heirarchy, and includes dept_code, which is the code for each department 
  (i.e. EECS), as well as dept_name (i.e. Electrical Engineering and Computer Science). Academic_class which 
  has dept_code as a Foreign Key from Academic_dept, class_code which is the code for each course (i.e. IT394),
  as well as class_name which is the full name of the course (i.e. Distributed Application Development).The 
  Upload class includes alias which is the user-defined alias for a file, class_code as a Foreign Key to Academic_class,
  document which is a FileField used for the actual file, rating which stores ratings from users, and upload_date which 
  stores the date at which the file was uploaded. We overrode the Meta class for Upload to order by upload date.

Testing:
  Tests include creating a department which should pass, getting a department that doesn't exist which should fail, &
  creating a class which should pass. Our tests are defined in wpFileSharing/final_proj/mysite/wpFiles/tests.py.
  
Known Issues:
  Warning flags for URL patterns '^ratings/' and '^search/', however this has not caused any issues thus far.


Future Improvements:
  Add features gained by creating an account with the site other than just being able to rate files. Users
  likely won't create accounts if that is the only feature they gain access to by signing up is rating files. 
  We wish to create a flag attribute which users can flag inappropriate content with, and admins can then easily
  identify inappropriate content and remove them. We would also like to add a 'favorite' feature wherein users 
  can favorite different files and they will be shown on their dashboard at login (we also wish to add a dashboard feature).
  Add feature to upload multiple files at once. Restructure app to allow for multiple files with same alias, and tie files to
  users who added them. Add a 'How to Use' button to help plebes with understanding the site.

Resources:
  http://wpfiles.herokuapp.com/wpFiles/ for general users
  http://wpfiles.herokuapp.com/admin/ for admin, username admin and password cisco
#Lend tech interview question  
  
How to install the app  
  
### Clone the repo  
<code> https://github.com/elviskirui/lendtech-interview.git  </code>
  
### Install packages  
  
<code> pip install -r requirements.txt </code>

 Update <code>.flaskenv</code> with your <code>SQLALCHEMY_DB_URI</code> and <code>SECRET_KEY</code>
 For our case please use <code>mysql</code> or <code>sqlit</code> for a smooth setup
 
### Setup the database
Run <code>flask shell</code> to open the shell
##### Import <code>db</code>
<code> >>>from src.database import db</code>
##### Create database tables
<code> >>> db.create_all() </code>
Exit the shell and start the server with 
<code>flask run</code>

Launch the app and register to create an account.

To test the features shared on the documentation, i have added a route to create sample data. Please note that this is only for demo purposes to show the functionality. This only works once you have created/registered an account.
Open the url : <code>http://127.0.0.1:5000/generate_random_data</code> to generate the sample data.
________

To run tests, run 
<code>pytest</code>
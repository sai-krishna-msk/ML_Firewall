I've trained a model Machine learning model which will protect websites from XSS attacks and SQL injections



If you have no idea what SQL injections are click  [here](https://www.youtube.com/watch?v=ciNHn38EyRc) to know about XSS click [here](https://www.youtube.com/watch?v=L5l9lSnNMxg) 

How it does is when ever a user sends a post request to the server before it getting parsed into an SQL query by the respective backend it sends it to the model which I have trained it data(containing a bunch of positive and negative samples of SQL and XSS attacks), So this model classifies it into a safe or malicious request, If it is safe then it proceeds or a default message pops in 

### Implementation

- For the purpose of demonstration I am using the template which is a backend built intentionally to test SQL injections which I got it from Jason [here](https://github.com/JasonHinds13/hackable) (*with permission*) 

- To test this demo website without the model you can fire up the server by navigating to the deploy folder and run

  ```
  python  vul.py
  ```

  and possibly run some SQL injections like(I am not teaching this are for testing purposes) I recommend you to visit the Repository of Jason for details regarding the template which I provided

  

  - For printing out all the elements in the present table

  ```sqlite
  %'--;
  ```

  <br>

  - For Checking if you can actually Penetrate into the system using the table sql_master

  ```sqlite
  juice' UNION SELECT 1,2,3 from sqlite_master WHERE type="table"; --
  ```

  <br>

  - For printing out all the tables

  ```sqlite
  juice' UNION SELECT name,sql,3 from sqlite_master WHERE type="table"; --
  ```

  <br>

  - Getting the information out of required table

  ```sqlite
  juice' UNION SELECT username,password,3 from employees;--
  ```

  

- After you have seen the possible exploits test it with the model by quitting the present server and running server with the model 

  ```python
  python mlFirewall.py
  ```

### Note:

- For making it more understandable  when every you enter name of a product, The SQL query which the server is going to send to the database is being appended to the file names "test.sql"  (You can see in Realtime how your enter is going to effect the SQL query)

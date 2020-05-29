

## **This repo consists material covered in null chapters seminar on application of ML on network security**

In case you've never heard or need a refresher on [SQL Injections](https://www.youtube.com/watch?v=ciNHn38EyRc) or [XSS](https://www.youtube.com/watch?v=L5l9lSnNMxg)



# Contents

- **Context**

- **SQL Material **

- **Training**

- **Demo**



# Context

As SQL injections simply are strings, ML model(NLP based) was trained to classify between valid user requests and user requests consisting of SQL injections or XSS attacks

Trained model is embedded into a Flask Server before a user request is used to run the SQL query server validates or sanitizes the user request by sending it to the model which then classifies thus protecting Web-Apps from malicious attacks



# SQL Material

**Material Used in the seminar is present in [SQL_practise](https://github.com/sai-krishna-msk/ML_Firewall/tree/master/SQL_practise) in markdown format**



## Training

**Code for model trained in the seminar along with the dataset are present in  [train](https://github.com/sai-krishna-msk/ML_Firewall/tree/master/train)**

# Demo

- Flask-App used in the demo, was specifically built to test SQL injections and is borrowed from [Jason](https://github.com/JasonHinds13/hackable) (*with permission to use it*) 

  

- To test the demo website without the model you can fire up the server by navigating to the [deploy](https://github.com/sai-krishna-msk/ML_Firewall/tree/master/deploy) folder and run

  ```bash
  python  vul.py
  ```

  

  Open the web app in the browser and try to get sensitive information through SQL injections, a few examples are given below

  

  

  - For printing out all the elements present in the table

  ```sqlite
  %'--;
  ```

  <br>

  - For Checking if you can actually Penetrate into the system query the master_table 

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

  

- After witnessing the  possible exploits, Stop the current server and test it with server equipped with ML model

  ```python
  python mlFirewall.py
  ```


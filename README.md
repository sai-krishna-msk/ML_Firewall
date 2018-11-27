

I wanted to train a Machine learning model to classify an http request as SQL injection(bad request) or a normal request(good request), I searched a lot for dataset and I finally found one which also had a column for XSS(I had no idea what it was till I saw it here ), Well then now my model can identify both.

So basically what is SQL  injection (you can find out [here](https://www.youtube.com/watch?v=ciNHn38EyRc)) but tldr: In dynamic website when we send a request to the server asking for some item present in our database, The name of the product we send is concatenated with an SQL query and is sent to the database,
This how a three tier system works Adapted by most of dynamic websites(__If you are new to SQL then skip to  SQL practice__) Now what a hacker may do is since our item sent is concatenated he will send in a SQL query statement instead of a product name to get additional information out of the database(usernames , passwords etc.) There are a lot of easy and conventional approaches to solve this problem but an advantage of using l here can just be understood from what I have told above our model also protest's our site from
XSS I did not even know what that was I just had the data( so you don't need to learn all different methods and ways you  just need to a labeled set of data , this is not to say that domain knowledge is not required but it is not necessary at the scale at which I am Implementing.)



To see how I Trained kindly navigate to train folder and checkout the code and the dataset, to
```
python train.py
```

### Implementation:
I wanted to see my model in action, Instead of me writing code for a demo website which is vulnerable to SQL injection, I just found a template [here](https://github.com/JasonHinds13/hackable) it is a classic website to demo SQL injection written in flask ( So , I don't have to make an API to use it to the actual website, instead now I could  just plug that in)So what I do is when I receive a http request asking for some product instead of directly concatenating it with SQL query and sending it to the database we put a filter in between which is first it needs to get approval from the mode we have trained then it would be interacting it with database
You can test that out by navigating to the deploy folder and run
```
python  vul.py
```
and do some hacking,

### SQL injections: 

- These are just some of SQL keywords/operations which we are going to take advantage of , (I am not teaching SQL injection here since it out of the scope of this project)

* "%" it is called wildcard , which means it returns all of the data , no matter what the logic says

* UNION , it is used to marge two merge two tables in a database( condition is it should be having same number of columns)

* sql_master a default table which contains metadata, of all the other tables

* *Commenting out "--"*

<br>



* For printing out all the elements in the present table
```
%'--;
```
<br>

* For Checking if you can actually Penetrate into the system using the table sql_master
```
juice' UNION SELECT 1,2,3 from sqlite_master WHERE type="table"; --
```

<br>
* For printing out all the tables
```
juice' UNION SELECT name,sql,3 from sqlite_master WHERE type="table"; --
```

<br>

* Getting the information out of required table
```
juice' UNION SELECT username,password,3 from employees;--
```

<br></br>


Now you can test it with the filter (our model plugged in) and perform the same with what you did above and compare the result's
```
python mlFirewall.py
```


### Note:
- For making it more understandable  when every you enter name of a product, The SQL query which the server is going to send to the database is being appended to the file names "test.sql"  (You can see in Realtime how your enter is going to effect the SQL query)


### SQL Practice:
- I have also provided a file name SQL_Practise where I have created a python server and a database so now you would be playing role of a server creating SQL queries for the database(SO instead of you entering the name of the product like last time you can instead enter the whole SQL query yourself to get the results), I consists a database with the table and their values can be seen Readme.md present in that folder.

To start up the server
```
python sql_practise.py
```
and when you go to the local host you can enter different types of queries there(I know front-end does not look so look but It works)

You can view the commands you can type in the readme.md file in that folder

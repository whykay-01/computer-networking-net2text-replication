## Weekly Report 2 - November 5th, 2023

### Ashley Chen

This week, I worked on trying to run the dataset generation provided by the Net2Text paper writers but was unable to run the code. I worked on attempting to run the code in different Python versions, fixing syntax errors. I have also looked over the code for how the the dataset is generated. Additionally, I attended Xinyu's small lecture about the paper itself and comprehended more elements, such as the equations that the paper provides. More of the paper and how the algorithm works makes a lot more sense now and gives me more direction for what we need to work on. For next week, I will probably start working more on writing the algorithm from the database we worked on this week.

### Malachi Daniel

I initialized our SQLlite database so that we can eventually query it and translate those outputs into natural language. And then I also reorganized the repository file structure.

### Minjae Lee

I have been adding more rules to the NLP2SQL file, created rules for all 4 types of queries. After discussing with Xinyu, we came to a conclusion that only the "How" type question will use the Compass Algorithm. In addition, I have created a file to start working on translating the results back to SQL.

### Yan Konichshev

This week Malachi and I worked on the database generation. The main problem with the initial database was that the data was not in a relational database format. After brainstorming about the way we should approach this problem, we decided to stick with a simple SQLite engine, as creating Docker DB server and deploying it using MySQL would have been somewhat redundant.

Finally, I have worked on the script that would allow us to convert the data from the python list of lists into a SQLite DB entries.

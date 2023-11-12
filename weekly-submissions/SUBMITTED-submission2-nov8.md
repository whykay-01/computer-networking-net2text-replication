## Weekly Report 2 - November 5th, 2023

### Ashley Chen

This week, I worked on trying to run the dataset generation provided by the Net2Text paper writers but was unable to run the code. I worked on attempting to run the code in different Python versions, fixing syntax errors. I have also looked over the code for how the the dataset is generated. Additionally, I attended Xinyu's small lecture about the paper itself and comprehended more elements, such as the equations that the paper provides. More of the paper and how the algorithm works makes a lot more sense now and gives me more direction for what we need to work on. For next week, I will probably start working more on writing the algorithm from the database we worked on this week.

### Malachi Daniel

Before Yan worked with PhD students (Xinyu and Yongting) to get the Net2Text generator working, I looked into ways for us to create mock data in Python, using SQLAlchemy as the database engine and Faker to create dummy data. I read some implementations about it and played around locally with the library to see how useful it would be compared to generated data and example data in the paper. It was not as useful as having the originally genrated data. Luckily Yan was able to get the generator working, so we don't need to create mock data using other libraries.

### Minjae Lee

I commited a file 2 days ago that translates English to MySQL, currently it can only support texts that are like written in the rules that I set, but I plan to add more rules. Specifically the program can translate questions like "How is Google's traffic managed?".

### Yan Konichshev

I have been working on managing the team work and coordinating our efforts. In addition to that, I attended the meeting with the PhD students and discussed the project with them. I also worked on the dataset generation and the network database. Right now, the snapshot of the network is loaded, but the challenge is that it is simply stored in a local variable in python. This following week, I am going to be working on understanding (and scripting the basic version of) ComPass algorithm. Additionally, I plan on converting the network database from the variable into an actual set of a relational database (MySQL).

This concludes the weekly report for the week of November 5th, 2023.

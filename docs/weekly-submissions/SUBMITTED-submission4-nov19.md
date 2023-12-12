## Weekly Report 4 - November 19th, 2023

### Ashley Chen

This week, I worked more on the ComPass algorithm. First, I got a sense of what was going on with our database and what is going in and how to read the database. After that, I incorporated that into the ComPass algorithm I wrote last week. I changed a couple of things and have more of an understanding of how things interact with each other. The ComPass algorithm now is capable of returning a specification set. The general algorithm has remained the same, but I changed some of the data types to make the argmax and scoring features work.

### Malachi Daniel

I worked with Yan to finish loading the output of the generator in to our network database and then I created a dictionary of router ids to location names, so we can accurately show the path taken instead of just numbers

### Minjae Lee

Nov 19th Weeky report. I have added more matching patterns so that now ingress, egress can be spotted in 2 different ways. For example, for a to spot a ingress one way is to directly spot "ingress is" and another is spotting the word following "from". I am currently working on covering cases when organizations or ingress or egresses are more than one word. I feel that I have created the general pipeline for text to SQL translation, so I wish to help Ashley on the compass algorithm next week or on other parts of the project as well.

### Yan Konichshev

This week has been quite productive as I have finished inserting data into the database and casting it to the appropriate types. Additionally, I have started some preliminary preparation for the final presentation of the project (e.g. creating a presentation template, preparing network topologies etc.). I was assisting the team in coordinating the work on the ComPass algorithm, and I have also started working on the algorithm myself.

# Net2Text Computer Networking

This is a repo for us to collaborate on all the files / papers we will be working on. Please commit appropriately. Don't forget to sync the repo once every 2-3 days.

# Explanation of our work

This is a project Yan Konichshev, Malachi Daniel, Ashley Chen, and Minjae Lee undertook as a part of the computer networking class at NYU Shanghai. Part of the course evaluation included some work with regards to the [Net2Text](https://www.usenix.org/conference/nsdi18/presentation/birkner) paper. We were tasked with creating a database of networks and then using the Compass algorithm (efficient summarization algotrithm), Argmax algorithm (to realize which features are making the most sense to summarize), and scoring function (to score features which will be used for summarization) to generate the natural language descriptions of the networks. We were also tasked with creating a natural language to SQL translator. This repo contains all the code we used to complete the project.

To replicate our emulations and experimental findings -- please follow instructions below. Do not hesitate to reach out to us if you have any questions. But before that, we encourage you to read the paper and the codebase to understand what we did and how we did it.

To start working with this repo, please make sure that you are meeting all the prerequisites. If you are not, please install them into the newly created virtual environment before continuing.

```shell
python -m venv .env
source .env/bin/activate
pip install -r requirements.txt
```

## Database generator

We used the database provided to us by the PhD students (Yongting and Xinyu). This database was initially sourced from the [Paper's authors](https://github.com/nsg-ethz/net2text), although we had to make some changes to the python scripts as they were all written in the depreciated python version. Additionally, we had to make some minor changes to make sure that the depreciated packages used by the author function appropriately. Codebase for that could be found in the `net2text_generator` folder in the root folder of the repository.

## SQLite Engine

Malachi and Yan initiated, created, and instantiated the network database using the SQLite engine. We used packages such as SQLite and SQLAlchemy to migrate the data from the python script (previously data was simply stored in the python list of lists) into the SQLite database. The database file is located in the `db` folder of the repository.

This means that you do not have to initiate the database yourself. However, if you want to do that, please follow the instructions below. It is a plug and play solution, so you do not have to worry about instantiating the server, just connect to the `.db` file and query from it.

```shell
cd src/db
```

### NOTE: THIS FOLLOWING COMMAND WILL GENERATE A NEW DATABASE. IF YOU WANT TO USE THE EXISTING DATABASE, PLEASE SKIP THIS STEP.

```shell
python insert_data_script.py ../../net2text_generator/examples/att_na_100
```

If you change the `att_na_100` part of the command to something more advanced, such as `att_na_1000`, or `att_na_10000` then you will load a **bigger dataset** into the database. However, please note that the bigger the dataset, the longer it will take to load it into the database.

Right now, it could be easily accessed via the VS Code extension. Here are the details of the extension you could use:

```
Name: SQLite
Id: alexcvzz.vscode-sqlite
Description: Explore and query SQLite databases.
Version: 0.14.1
Publisher: alexcvzz
VS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite
```

To access the database, simply install the extention and then open the `db/network.db` file using `Cmd + Shift + P` and typing `SQLite: Open Database` in the window that appears there. After that press `Enter`. Nothing will happen on your screen, however the database will be initiated on your device. After that, please open the command palette again and type `SQLite: Quick Query`, type `sql SELECT * FROM network` and press `Enter`. The new window will appear with all the data from the database.

(You can also use the `SQLite: Run Query` command to run the query in the current window.)

Additionally, you can use some other packages / extensions to access the database.

## Network Visualizer

Network visualizer is located in the `src/external` folder. To run it, please run the script without any positional arguments. It is a simple generator that has already produced a basic network visualization for the `att_na_10000` dataset. It could be accessed via your browser. Simply open the `src/external/nx.html` file in your browser and you will see the network visualization.

## SQL to Natural Language

The following part is created by Minjae.

This file translates Natural language(English) to SQL. It uses spaCy to tokenize queries. The file is located in the parse folder in the repository.

```shell
cd src/parse
```

Run these commands to install spacy in a virtual environment:

```shell
python -m venv .env
source .env/bin/activate
pip install -U pip setuptools wheel
pip install -U spacy
```

To Download a trained pipeline in spaCy, run:

```shell
python -m spacy download en_core_web_sm
```

The underlying concept behind this translation is context-free grammars. Using spaCy, used matching rules to match user's inputs with SQL queries. More rules could be added or machine learning concepts could be used for improvment. Currently, you could easily ask questions in which it would not understand. If you enter conditions that are not in the database, the query won't translate it into SQL.

## Natural language to SQL

This file translates the results of the compass algorithm back to Natural Language(English)

First, the functions add traffic weights in percentages to the compass result, then the compass result is translated to natural language.

## ComPass
The `compass.py` consists the ComPass algorithm mentioned in the Net2Text paper which is an approximation algorithm for generating high-level summaries. The main function used is the `ComPass(R, q, k, t)` method. 

The algorithm finds the feature function that scores the highest from the `argmax(Q, R)` function and adds it to the set L while removing it from the set of candidate features Q. After that, it optimizes the next searches by only searching the remaining feature functions per path. This set is added to set S which is the return set. `ComPass` repeats the process until the set S has reached maximum specifications.

The other two functions are `argmax` and `score_feature(q, v, R)`. `score_feature` adds the traffic size to the weight of the path if that is the current value we are checking for. `argmax` uses the `score_feature` function and returns the path with the highest score.

# Net2Text Computer Networking

This is a repo for us to collaborate on all the files / papers we will be working on. Please commit appropriately. Don't forget to sync the repo once every 2-3 days.

# Explanation of our work

#TODO: finish this after we're done

## Database generator

We used the database provided to us by the PhD students (Yongting and Xinyu). This database was initially sourced from the [Paper's authors](#TODO: link here), although we had to make some changes to the python scripts as they were all written in the depreciated python version. Additionally, we had to make some minor changes to make sure that the depreciated packages used by the author function appropriately. Codebase for that could be found in the `net2text_generator` folder in the root folder of the repository.

## SQLite Engine

Malachi and Yan initiated, created, and instantiated the network database using the SQLite engine. We used packages such as SQLite and SQLAlchemy to migrate the data from the python script (previously data was simply stored in the python list of lists) into the SQLite database. The database is located in the `db` folder of the repository.

```shell
cd src/db
```

### NOTE: THIS WILL GENERATE A NEW DATABASE. IF YOU WANT TO USE THE EXISTING DATABASE, PLEASE SKIP THIS STEP.

```shell
python insert_data_script.py ../../net2text_generator/examples/att_na_100
```

If you change the `att_na_100` part of the command to something more advanced, such as `att_na_1000`, or `att_na_10000` then you will load a bigger dataset into the database. However, please note that the bigger the dataset, the longer it will take to load it into the database.

Right now, it could be easily accessed via the VS Code extension. Here are the details:

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

Network visualizer is located in the `src/external` folder. To run it, please run the script without any positional arguments.

## SQL to Natural Language

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

## Natural language to SQL

This file translates the results of the compass algorithm back to Natural Language(English)

First, the functions add traffic weights in percentages to the compass result, then the compass result is translated to natural language.

## Yan Konichshev - Additional Report For The Final Research Project

## Introduction:

I have been working as a team leader of the project and have been responsible for the following tasks:

1. Setting up the project structure
2. Managing responsibilities and tasks within the team
3. Providing regular updates to the team about the progress and deadlines
4. Creating the database generator
5. Creating the SQLite engine
6. Initializing the database
7. I have managed to make the feature extraction (aka scoring function) algorithm and argmax function work

## Short summary of the project (taken from multiple sorces produced by our team):

Final goal of the project: Ease life for network operators to understand the inner forwarding state of the whole network in a more concise and faster way + give them a chance to query more details about specific routes and paths.

Our goals: Understanding concepts which allowed researchers to simplify the process of querying the network state + replicating the project from scratch

Summary of the pipeline we had to come up with:

1. Come up with a relevant question about the network state
2. Translate it to the SQL-format
3. Query the database and obtain the results
4. Utilize ComPass algorithm to reduce the search space from the DB query
5. Use the output of the summarization algorithm to translate it back to the NL

## My contributions to the project:

As I have previously mentioned, I have substantially contributed to the project. I have been responsible for making the network database work, which essentially was the backbone for the algorithm and NL2SQL and SQL2NL translation. To achieve these goals, I have learned a lot about how the network database is organized. In addition to that, I think it was a rewarding experience, as I was able to experience paper's ideas first-hand and see how they work in practice.

I have also been responsible for making the feature extraction work and the argmax functions work. This means, that I have been able to help our team to have a meaningful interpretation of the SQL query results and summarize scores for the most desired feature values, so that they could be prioritized and used for the ComPass algorithm.

Finally, since I was a project teamlead, I have been responsible for the project structure (GitHub repository maintenance) and the overall management of the project. We have had weekly meetings with a group of PhD students, where we arranged our day to day tasks and discussed the progress.

For more information, please consult the `README.md` file in the root of the repository. I have documented our work in tiniest details there.

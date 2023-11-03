import spacy 
from spacy.matcher import Matcher
# Load the English language model
nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)
# Sample English query
query = "How does all Google network traffic go through?"

# Process the query with spaCy
doc = nlp(query)

# Initialize variables for SQL translation
intent = "SELECT"
org = None
ingress = None
egress = None

# Define entity and intent recognition rules
#yes or no pattern
yes_or_no_pattern = [{"POS": "AUX"}, {"POS": "PRON"}, {"POS": "VERB"}]
#how pattern
how_pattern = [{"LOWER": "how"}]
org_pattern = [{"ENT_TYPE": "ORG"}]
egress_pattern = [{"TEXT": "to"}, {"ENT_TYPE": "GPE"}]
ingress_pattern = [{"TEXT": "from"}, {"ENT_TYPE": "GPE"}]

#adding patterns to the matcher
matcher.add("YES_OR_NO_PATTERN", [yes_or_no_pattern])
matcher.add("HOW_PATTERN", [how_pattern])
matcher.add("ORG_PATTERN", [org_pattern])
matcher.add("EGRESS_PATTERN", [egress_pattern])
matcher.add("INGRESS_PATTERN", [ingress_pattern])

matches = matcher(doc)

for match_id, start, end in matches:
    if match_id == nlp.vocab.strings["YES_OR_NO_PATTERN"]:
        intent = "YES_OR_NO"
    elif match_id == nlp.vocab.strings["HOW_PATTERN"]:
        intent = "HOW"
    elif match_id == nlp.vocab.strings["ORG_PATTERN"]:
        org = doc[start:end]
    elif match_id == nlp.vocab.strings["EGRESS_PATTERN"]:
        egress = doc[start+1:end]
    elif match_id == nlp.vocab.strings["INGRESS_PATTERN"]:
        ingress = doc[start+1:end]
# Construct the SQL query
#Question type 1: yes or no questions
if intent == "YES_OR_NO":
    pass
#Question type 2: counting queries
if intent == "COUNT":
    pass
#Question type 3: How questions
elif intent == "HOW":
    sql_query = "SELECT * FROM paths WHERE"
    if ingress:
        sql_query += f" ingress'{ingress}' AND" 
    if egress:
        sql_query += f" ingress'{egress}' AND" 
    if org:
        sql_query += f" org='{org}' AND"
    if sql_query[-3:] == "AND":
        sql_query = sql_query[0:-4]
    print("Translated SQL Query:", sql_query)
#Question type 4 Where questions
elif intent == "WHERE":
    pass
else:
    print("Unable to translate the query.")


import spacy 
from spacy.matcher import Matcher
# Load the English language model
nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)
# Sample English query
query = "How does the shortest path of Google network traffic go through?"

# Process the query with spaCy
doc = nlp(query)

# Initialize variables for SQL translation
intent = ""
org = None
ingress = None
egress = None
shortest_path = False

# Define entity and intent recognition rules
#yes or no pattern
yes_or_no_pattern = [{"POS": "AUX"}, {"POS": "PRON"}, {"POS": "VERB"}]
#how pattern
how_pattern = [{"LOWER": "how"}, {"LEMMA": {"in": ["be", "will", "would", "do"]}}]
#count pattern
count_pattern = [{"LOWER": "how"}, {"LEMMA": "many"}]
#data retrieval pattern
data_retrieval_pattern = [{"LOWER": "what"}, {"LEMMA": "be"}]
org_pattern = [{"ENT_TYPE": "ORG"}]
egress_pattern = [{"TEXT": "to"}, {"ENT_TYPE": "GPE"}]
ingress_pattern = [{"TEXT": "from"}, {"ENT_TYPE": "GPE"}]
shortest_path_pattern = [{"POS": "ADJ", "LOWER": {"in": ["shortest", "quickest", "fastest"]},
     "OP": "+"},
    {"LOWER": "path"}]
#adding patterns to the matcher
matcher.add("YES_OR_NO_PATTERN", [yes_or_no_pattern])
matcher.add("HOW_PATTERN", [how_pattern])
matcher.add("COUNT_PATTERN", [count_pattern])
matcher.add("DATA_RETRIEVAL_PATTERN", [data_retrieval_pattern])
matcher.add("ORG_PATTERN", [org_pattern])
matcher.add("EGRESS_PATTERN", [egress_pattern])
matcher.add("INGRESS_PATTERN", [ingress_pattern])
matcher.add("SHORTEST_PATH_PATTERN", [shortest_path_pattern])

matches = matcher(doc)

for match_id, start, end in matches:
    if match_id == nlp.vocab.strings["YES_OR_NO_PATTERN"]:
        intent = "YES_OR_NO"
    elif match_id == nlp.vocab.strings["HOW_PATTERN"]:
        intent = "HOW"
    elif match_id == nlp.vocab.strings["COUNT_PATTERN"]:
        intent = "COUNT"
    elif match_id == nlp.vocab.strings["ORG_PATTERN"]:
        org = doc[start:end]
    elif match_id == nlp.vocab.strings["EGRESS_PATTERN"]:
        egress = doc[start+1:end]
    elif match_id == nlp.vocab.strings["INGRESS_PATTERN"]:
        ingress = doc[start+1:end]
    elif match_id == nlp.vocab.strings["SHORTEST_PATH_PATTERN"]:
        shortest_path = True
# Construct the SQL query
#Question type 1: yes or no questions

def Select_intent (intent):
    if intent == "YES_OR_NO":
        sql_query = "SELECT CASE WHEN COUNT(*) > 0 THEN TRUE ELSE FALSE ENDS AS result FROM paths WHERE"
#Question type 2: counting queries
    elif intent == "COUNT":
        sql_query = "SELECT COUNT(*) FROM paths WHERE"
#Question type 3: How questions
    elif intent == "HOW":
        sql_query = "SELECT * FROM paths WHERE"   
#Question type 4 Where questions
    elif intent == "DATA_RETRIEVAL":
        pass
    else:
        print("Unable to translate the query.")
    return sql_query


def Select_conditions (sql_query):
    if ingress:
        sql_query += f" ingress'{ingress}' AND" 
    if egress:
        sql_query += f" egress'{egress}' AND" 
    if org:
        sql_query += f" org='{org}' AND"
    if shortest_path:
        sql_query += f" shortest_path='{True}' AND"
    if sql_query[-3:] == "AND":
        sql_query = sql_query[0:-4]
    return sql_query

sql_query = Select_intent(intent)
if sql_query:
    sql_query = Select_conditions(sql_query)
print(sql_query)
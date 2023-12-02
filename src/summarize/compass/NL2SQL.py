import spacy
from spacy.matcher import Matcher
import sqlite3

# Add the project's root directory to the Python path

# Now you can import the module using an absolute path
query = "When the ingress is Salt Lake City, how does the Yahoo's traffic go through?"
query1 = "How does the Tikona Digital Networks Pvt Ltd.'s traffic go through from New York to Chicago?"
query2 = "How does the traffic get handled?"

def parse(query):
    con = sqlite3.connect("src/db/network.db")
    cur = con.cursor()
    possible_destinations = []
    for row in cur.execute(
        "SELECT destination FROM network;"
    ):
        if row[0] not in possible_destinations:
            possible_destinations.append(row[0])
    ROUTERS = {
        "0": "New York",
        "1": "Cambridge",
        "2": "Chicago",
        "3": "Cleveland",
        "4": "Raleigh",
        "5": "Atlanta",
        "6": "Philadelphia",
        "7": "Washington",
        "8": "Nashville",
        "9": "St. Louis",
        "10": "New Orleans",
        "11": "Houston",
        "12": "San Antonio",
        "13": "Dallas",
        "14": "Orlando",
        "15": "Denver",
        "16": "Kansas City",
        "17": "San Francisco",
        "18": "Sacramento",
        "19": "Portland",
        "20": "Seattle",
        "21": "Salt Lake City",
        "22": "Los Angeles",
        "23": "San Diego",
        "24": "Phoenix",
    }


    # Load the English language model
    nlp = spacy.load("en_core_web_sm")
    matcher = Matcher(nlp.vocab)
    # Process the query with spaCy
    doc = nlp(query)
    # Initialize variables for SQL translation
    intent = None
    org = None
    ingress = None
    egress = None
    shortest_path = False

    # Define entity and intent recognition rules
    # yes or no pattern
    yes_or_no_pattern = [{"POS": "AUX"}, {"POS": "PRON"}, {"POS": "VERB"}]
    # how pattern
    how_pattern = [{"LOWER": "how"}, {"LEMMA": {"in": ["be", "will", "would", "do"]}}]
    # count pattern
    count_pattern = [{"LOWER": "how"}, {"LEMMA": "many"}]
    # data retrieval pattern
    data_retrieval_pattern = [{"LOWER": "what"}, {"LEMMA": "be"}]
    #org_pattern = [{"LOWER": destination.lower()} if " " in destination else {"TEXT": destination} for destination in possible_destinations]
    egress_pattern1 = [
        {"TEXT": "to"},
        {"ENT_TYPE": "GPE"},
        {"ENT_TYPE": "GPE", "OP": "*"},
    ]
    egress_pattern2 = [
        {"lower": "egress"},
        {"lower": "is"},
        {"ENT_TYPE": "GPE"},
        {"ENT_TYPE": "GPE", "OP": "*"},
    ]
    ingress_pattern1 = [
        {"TEXT": "from"},
        {"ENT_TYPE": "GPE"},
        {"ENT_TYPE": "GPE", "OP": "*"},
    ]
    ingress_pattern2 = [
        {"lower": "ingress"},
        {"lower": "is"},
        {"ENT_TYPE": "GPE"},
        {"ENT_TYPE": "GPE", "OP": "*"},
    ]
    shortest_path_pattern1 = [
        {"POS": "ADJ", "LOWER": {"in": ["shortest", "quickest", "fastest"]}, "OP": "+"},
        {"LOWER": "path"},
    ]
    shortest_path_pattern2 = [
        {"lower": "shortest"},
        {"lower": "path"},
        {"lower": "is"},
        {"lower": "true"},
    ]
    word_org_pattern = [{"LOWER": "orgnization"}]
    word_egress_pattern = [{"LOWER": "egress"}]
    word_ingress_pattern = [{"LOWER": "ingress"}]
    word_path_pattern = [{"LOWER", "path"}]
    word_traffic_size_pattern = [{"LOWER": "traffic"}, {"LOWER": "size"}]
    word_prefix_pattern = [{"LOWER": "prefix"}]
    # adding patterns to the matcher
    matcher.add("YES_OR_NO_PATTERN", [yes_or_no_pattern])
    matcher.add("HOW_PATTERN", [how_pattern])
    matcher.add("COUNT_PATTERN", [count_pattern])
    matcher.add("DATA_RETRIEVAL_PATTERN", [data_retrieval_pattern])
    matcher.add("EGRESS_PATTERN", [egress_pattern1, egress_pattern2])
    matcher.add("INGRESS_PATTERN", [ingress_pattern1, ingress_pattern2])
    matcher.add(
        "SHORTEST_PATH_PATTERN", [shortest_path_pattern1, shortest_path_pattern2]
    )

    matches = matcher(doc)
    for match_id, start, end in matches:
        if match_id == nlp.vocab.strings["YES_OR_NO_PATTERN"]:
            intent = "YES_OR_NO"
        elif match_id == nlp.vocab.strings["HOW_PATTERN"]:
            intent = "HOW"
        elif match_id == nlp.vocab.strings["COUNT_PATTERN"]:
            intent = "COUNT"
        #elif match_id == nlp.vocab.strings["ORG_PATTERN"]:
            #org = doc[start:end]
        elif match_id == nlp.vocab.strings["EGRESS_PATTERN"]:
            for key, value in ROUTERS.items():
                if value in str(doc[start:end]):
                    egress = key
        elif match_id == nlp.vocab.strings["INGRESS_PATTERN"]:
            for key, value in ROUTERS.items():
                if value in str(doc[start:end]):
                    ingress = key
        elif match_id == nlp.vocab.strings["SHORTEST_PATH_PATTERN"]:
            shortest_path = True
    #initializing destination(org)
    for phrase in possible_destinations:
        if phrase in query:
            org = phrase
    # Construct the SQL query
    def Select_intent(intent):
        # Question type 1: yes or no questions
        if intent == "YES_OR_NO":
            sql_query = "SELECT CASE WHEN COUNT(*) > 0 THEN TRUE ELSE FALSE ENDS AS result FROM network WHERE"
        # Question type 2: counting queries
        elif intent == "COUNT":
            sql_query = "SELECT COUNT(*) FROM network WHERE"
        # Question type 3: How questions
        elif intent == "HOW":
            sql_query = "SELECT path, destination, traffic_size, ingress, egress, shortest_path FROM network WHERE"
        # Question type 4 Where questions
        elif intent == "DATA_RETRIEVAL":
            sql_query = "SELECT * FROM network WHERE"
        else:
            print("Unable to translate the query.")
        return sql_query

    def Select_conditions(sql_query):
        print(ingress)
        original_conditions = []
        if ingress:
            sql_query += f" ingress='{ingress}' AND"
            original_conditions.append(ingress)
        if egress:
            sql_query += f" egress='{egress}' AND"
            original_conditions.append(egress)
        if org:
            sql_query += f" destination='{org}' AND"
            original_conditions.append(org)
        if shortest_path:
            sql_query += f" shortest_path='{True}' AND"
        if sql_query[-3:] == "AND":
            sql_query = sql_query[0:-4]
        if sql_query[-5:] == "WHERE":
            sql_query = sql_query[:-5]
            return sql_query, original_conditions
        return sql_query, original_conditions

    sql_query = Select_intent(intent)
    if sql_query:
        sql_query, original_conditions = Select_conditions(sql_query)
        if sql_query:
            return sql_query, original_conditions
        else:
            return "Unable to translate the query"
    else:
        return "Unable to translate the query"


result = parse(query2)
print(result)

import sqlite3
compass_result = [{('shortest_path', 1)}, 
{('egress', '7'), ('shortest_path', 1)}, 
{('egress', '7'), ('ingress', '16'), ('shortest_path', 1)}, 
{('destination', 'Charter Communications'), ('egress', '7'), ('ingress', '16'), ('shortest_path', 1)}]
compass_result2 = [{('destination', 'Tikona Digital Networks Pvt Ltd.')}, 
                   {('shortest_path', 1), ('destination', 'Tikona Digital Networks Pvt Ltd.')},
                   {('shortest_path', 1), ('destination', 'Tikona Digital Networks Pvt Ltd.'), ('egress', '8')},
                   {('shortest_path', 1), ('ingress', '7'), ('destination', 'Tikona Digital Networks Pvt Ltd.'), ('egress', '8')}] 
condition = ['7', 'Tikona Digital Networks Pvt Ltd.']
def back_to_natural_language(compass_result, condition):
    con = sqlite3.connect("src/db/network.db")
    cur = con.cursor()
    possible_destinations = []
    compass_result = compass_result[-1]
    '''for row in cur.execute(
        "SELECT traffic FROM network;"
    ):
        if row[0] not in possible_destinations:
            possible_destinations.append(row[0])'''
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
    
    result = ""
    for specification_tuple in compass_result:
        if specification_tuple[0] == "destination":
            destination = specification_tuple[1]
        elif specification_tuple[0] == "ingress":
            ingress = ROUTERS[specification_tuple[1]]
        elif specification_tuple[0] == "egress":
            egress = ROUTERS[specification_tuple[1]]
        elif specification_tuple[0] == "shortest_path":
            if specification_tuple[1] == 1:
                shortest_path = "shortest"
            else:
                shortest_path = ""
    result = f"{destination}'s traffic takes the {shortest_path} path to exit from {egress} and enter {ingress}."
    example = "Google's traffic "
    return result

result = back_to_natural_language(compass_result2, condition)
#print(result)


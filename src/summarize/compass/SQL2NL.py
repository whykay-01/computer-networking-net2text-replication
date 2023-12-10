import sqlite3

def format_compass_result (compass_result):
    formatted_list = []
    for s in compass_result:
        inner_list = []
        for t in s:
            inner_list.append(t)
        formatted_list.append(inner_list)
    return formatted_list
            
        

def back_to_natural_language(compass_result, condition):
    print(condition)
    compass_result = format_compass_result(compass_result)
    con = sqlite3.connect("src/db/network.db")
    cur = con.cursor()
    possible_destinations = []
    compass_result_end = compass_result[-1]
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
    for specification_tuple in compass_result_end:
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
    first_traffic_size = 0
    second_traffic_size = 0
    third_traffic_size = 0
    if len(condition) == 0:
        return "Unable to reply. The question is invalid."
    elif len(condition) == 1:
        if tuple(condition[0]) not in compass_result[-1]:
            return "Unable to reply. The question is invalid."
        second_condtition = None
        third_condition = None
        for row1 in cur.execute(
            f"SELECT traffic_size FROM network WHERE {condition[0][0]}='{condition[0][1]}'"
        ):
            first_traffic_size += row1[0]
        
        for t in compass_result[2]:
            if t[0] != "shortest_path" and t[0] != condition[0][0]:
                second_condition = t
                condition.append(second_condition)
        for t in compass_result[-1]:
            if t[0] != "shortest_path" and list(t) not in condition and t != second_condition: 
                third_condition = t
                condition.append(third_condition)
        for row2 in cur.execute(
            f"SELECT traffic_size FROM network WHERE {condition[0][0]}='{condition[0][1]}' AND {second_condition[0]}='{second_condition[1]}'"
        ):  
            second_traffic_size += row2[0]
        for row3 in cur.execute(
            f"SELECT traffic_size FROM network WHERE {condition[0][0]}='{condition[0][1]}' AND {second_condition[0]}='{second_condition[1]}' AND {third_condition[0]}='{third_condition[1]}'"
        ):
            third_traffic_size += row3[0]
        if first_traffic_size == 0:
            first_percentage = 0
        else:
            first_percentage = format(second_traffic_size/first_traffic_size * 100, ".1f")
        if second_traffic_size == 0:
            second_percentage = 0
        else:
            second_percentage = format(third_traffic_size/second_traffic_size * 100, ".1f")
        if condition[0][0] == "destination":
            result = f"{first_percentage}% of {destination}'s traffic "
            if second_condition[0] == "egress":
                result += f"exits to {egress}. "
                result += f"{second_percentage}% of its traffic exitting to {egress} takes the {shortest_path} path and enters from {ingress}."
            elif second_condition[0] == "ingress":
                result += f"enters from {ingress}. "
                result += f"{second_percentage}% of its traffic entering from {ingress} takes the {shortest_path} path to exit to {egress}."
        elif condition[0][0] == "ingress":
            result = f"{first_percentage}% of traffic from {ingress} "
            if second_condition[0] == "egress":
                result += f"exits to {egress}. "
                result += f"{second_percentage}% of its traffic exiting to {egress} takes the {shortest_path} path and is handled by {destination}."
            elif second_condition[0] == "destination":
                result += f"is handled by {destination}. "
                result += f"{second_percentage}% of its traffic handled by {destination} takes the {shortest_path} path to exit to {egress}."
        elif condition[0][0] == "egress":
            result = f"{first_percentage}% of traffic to {egress} "
            if second_condition[0] == "ingress":
                result += f"enters from {ingress}. "
                result += f"{second_percentage}% of its traffic entering from {ingress} takes the {shortest_path} path and is handled by {destination}."
            elif second_condition[0] == "destination":
                result += f"is handled by {destination}. "
                result += f"{second_percentage}% of its traffic handled by {destination} takes the {shortest_path} path to enters from {ingress}."
    elif len(condition) == 2:
        if tuple(condition[0]) not in compass_result[-1] or tuple(condition[1]) not in compass_result[-1]:
            return "Unable to reply. The question is invalid."
        for t in compass_result[-1]:
            if t[0] != "shortest_path" and list(t) not in condition:
                third_condition = t
                condition.append(third_condition)
        for row4 in cur.execute(
            f"SELECT traffic_size FROM network WHERE {condition[0][0]}='{condition[0][1]}' AND {condition[1][0]}='{condition[1][1]}'"
        ):  
            first_traffic_size += row4[0]
        for row5 in cur.execute(
            f"SELECT traffic_size FROM network WHERE {condition[0][0]}='{condition[0][1]}' AND {condition[1][0]}='{condition[1][1]}' AND {third_condition[0]}='{third_condition[1]}'"
        ):  
            second_traffic_size += row5[0]
        first_percentage = format(second_traffic_size/first_traffic_size * 100, ".1f")
        if third_condition[0] == "ingress":
            result = f"{first_percentage}% of {destination}'s traffic that exits to {egress} enters from {ingress}."
        elif third_condition[0] == "egress":
            result = f"{first_percentage}% of {destination}'s traffic that enters from {ingress} exits to {egress}."
        elif third_condition[0] == "destination":
            result = f"{first_percentage}% of traffic that exits to {egress} enters from {ingress} is handled by {destination}."
    elif len(condition) == 3:
        if tuple(condition[0]) not in compass_result[-1] or tuple(condition[1]) not in compass_result[-1] or tuple(condition[2]) not in compass_result[-1]:
            return "Unable to reply. The question is invalid."
        for row6 in cur.execute(
            f"SELECT traffic_size FROM network WHERE destination='{destination}'"
        ):  
            first_traffic_size += row6[0]
        for row7 in cur.execute(
            f"SELECT traffic_size FROM network WHERE {condition[0][0]}='{condition[0][1]}' AND {condition[1][0]}='{condition[1][1]}' AND {condition[2][0]}='{condition[2][1]}'"
        ):  
            second_traffic_size += row7[0]
        first_percentage = format(second_traffic_size/first_traffic_size * 100, ".1f")
        result = f"{first_percentage}% of {destination}'s traffic enters from {ingress} and exits to {egress} and takes the {shortest_path} path."
            
            
    return result

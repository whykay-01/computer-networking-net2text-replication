compass_result = [['60', {'egress': "NY"}], 
                  ['40', {"egress": "Washington"}], 
                  ['39.6', {"egress": "New York", "shortest_path": True, "waypoint": "Atlanta"}]]
intent = "HOW"
percentage = float(compass_result[2][0]) / float(compass_result[0][0])
if intent == "HOW":
    result = f"It exits in {compass_result[0][1].get('egress')} ({compass_result[0][0]}%) and {compass_result[1][1].get('egress')} ({compass_result[1][0]}%). "
if intent == "HOW" and compass_result[2][1].get('shortest_path'):
    result += f"{str(percentage*100)}% of the traffic exiting in {compass_result[2][1].get('egress')} follows the shortest path and crosses {compass_result[2][1].get('waypoint')}."

print(result)

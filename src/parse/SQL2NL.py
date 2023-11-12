compass_result = [[60, {'egress': "NY"}], 
                  [40, {"egress": "Washington"}], 
                  [39.6, {"egress": "New York", "shortest_path": True, "waypoint": "Atlanta"}]]
intent = "HOW"
percentage = compass_result[2][0] / compass_result[0][0]

if intent == "HOW" and compass_result[2][1].get('shortest_path'):
    result = f"{percentage}% of the traffic exiting in {compass_result[2][1].get('egress')} follows the shortest path and crosses {compass_result[2][1].get('waypoint')}."

print(result)

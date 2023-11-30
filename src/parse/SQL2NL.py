compass_result = [['60', {'egress': "NY"}], 
                  ['40', {"egress": "Washington"}], 
                  ['39.6', {"egress": "New York", "shortest_path": True, "waypoint": "Atlanta"}]]
compass_result2 = {{"NY": "egress"},
                   {"Wahsington": 'egress'},
                   {"Wahsington": 'egress', "shortest_path": True},
}
class RoutingPath:
    def __init__(self, path, destination, ingress, egress, shortest_path, traffic_size):
        self.path = path
        self.destination = destination
        self.ingress = ingress
        self.egress = egress
        self.shortest_path = shortest_path
        self.traffic_size = traffic_size
set1 = RoutingPath(None, None, None,"NY", None, None)
set2 = RoutingPath(None, None, None,"Washington", None, None)
set3 = RoutingPath(None, None, None,"NY", True, None)
compass_result3 = {set1, set2, set3}
def back_to_natural_language(compass_result2):
    egress_part = 'it exits in '
    '''percentage = float(compass_result[2][0]) / float(compass_result[0][0]) '''
    for object in compass_result2:
        if compass_result2.egress and compass_result2.shortest_path == None:
            egress_part += str(compass_result2.egress) + ", "
    result = f"It exits in {compass_result[0][1].get('egress')} ({compass_result[0][0]}%) and {compass_result[1][1].get('egress')} ({compass_result[1][0]}%). "
    return result

result = back_to_natural_language(compass_result)
print(result)


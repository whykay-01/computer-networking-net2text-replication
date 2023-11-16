"""
Created with:

import json
from networkx import read_graphml, Graph

graph: Graph = read_graphml("../../net2text_generator/examples/att_na/AttMpls.graphml")

d = dict()
for id, data in graph.nodes.data():
    d[id] = data

with open("router_map.py", "w") as file:
    file.write("routers = " + json.dumps(d))
"""

from typing import Final, TypedDict


class Router(TypedDict):
    Internal: int
    Latitude: float
    Country: str
    type: str
    id: int
    Longitude: float
    label: str
    hub_name: str


ROUTERS: Final[dict[str, Router]] = {
    "0": {
        "Internal": 1,
        "Latitude": 40.71427,
        "Country": "United States",
        "type": "Completion 2007 - 2008",
        "id": 0,
        "Longitude": -74.00597,
        "label": "NY54",
        "hub_name": "New York, NY",
    },
    "1": {
        "Internal": 1,
        "Latitude": 42.3751,
        "Country": "United States",
        "type": "Completion 2007 - 2008",
        "id": 1,
        "Longitude": -71.10561,
        "label": "CMBR",
        "hub_name": "Cambridge, MA",
    },
    "2": {
        "Internal": 1,
        "Latitude": 41.85003,
        "Country": "United States",
        "type": "Completed",
        "id": 2,
        "Longitude": -87.65005,
        "label": "CHCG",
        "hub_name": "Chicago, IL",
    },
    "3": {
        "Internal": 1,
        "Latitude": 41.4995,
        "Country": "United States",
        "type": "Completed",
        "id": 3,
        "Longitude": -81.69541,
        "label": "CLEV",
        "hub_name": "Cleveland, OH",
    },
    "4": {
        "Internal": 1,
        "Latitude": 35.7721,
        "Country": "United States",
        "type": "Completion 2007 - 2008",
        "id": 4,
        "Longitude": -78.63861,
        "label": "RLGH",
        "hub_name": "Raleigh, NC",
    },
    "5": {
        "Internal": 1,
        "Latitude": 33.749,
        "Country": "United States",
        "type": "Completed",
        "id": 5,
        "Longitude": -84.38798,
        "label": "ATLN",
        "hub_name": "Atlanta, GA",
    },
    "6": {
        "Internal": 1,
        "Latitude": 39.95234,
        "Country": "United States",
        "type": "Completed",
        "id": 6,
        "Longitude": -75.16379,
        "label": "PHLA",
        "hub_name": "Philadelphia, PA",
    },
    "7": {
        "Internal": 1,
        "Latitude": 38.89511,
        "Country": "United States",
        "type": "Completed",
        "id": 7,
        "Longitude": -77.03637,
        "label": "WASH",
        "hub_name": "Washington, DC",
    },
    "8": {
        "Internal": 1,
        "Latitude": 36.16589,
        "Country": "United States",
        "type": "Completion 2007 - 2008",
        "id": 8,
        "Longitude": -86.78444,
        "label": "NSVL",
        "hub_name": "Nashville, TN",
    },
    "9": {
        "Internal": 1,
        "Latitude": 38.62727,
        "Country": "United States",
        "type": "Completed",
        "id": 9,
        "Longitude": -90.19789,
        "label": "STLS",
        "hub_name": "St. Louis, MO",
    },
    "10": {
        "Internal": 1,
        "Latitude": 29.95465,
        "Country": "United States",
        "type": "Completion 2007 - 2008",
        "id": 10,
        "Longitude": -90.07507,
        "label": "NWOR",
        "hub_name": "New Orleans, LA",
    },
    "11": {
        "Internal": 1,
        "Latitude": 29.76328,
        "Country": "United States",
        "type": "Completed",
        "id": 11,
        "Longitude": -95.36327,
        "label": "HSTN",
        "hub_name": "Houston, TX",
    },
    "12": {
        "Internal": 1,
        "Latitude": 29.42412,
        "Country": "United States",
        "type": "Completion 2007 - 2008",
        "id": 12,
        "Longitude": -98.49363,
        "label": "SNAN",
        "hub_name": "San Antonio, TX",
    },
    "13": {
        "Internal": 1,
        "Latitude": 32.78306,
        "Country": "United States",
        "type": "Completed",
        "id": 13,
        "Longitude": -96.80667,
        "label": "DLLS",
        "hub_name": "Dallas, TX",
    },
    "14": {
        "Internal": 1,
        "Latitude": 28.53834,
        "Country": "United States",
        "type": "Completed",
        "id": 14,
        "Longitude": -81.37924,
        "label": "ORLD",
        "hub_name": "Orlando, FL",
    },
    "15": {
        "Internal": 1,
        "Latitude": 39.73915,
        "Country": "United States",
        "type": "Completion 2007 - 2008",
        "id": 15,
        "Longitude": -104.9847,
        "label": "DNVR",
        "hub_name": "Denver, CO",
    },
    "16": {
        "Internal": 1,
        "Latitude": 39.11417,
        "Country": "United States",
        "type": "Completion 2007 - 2008",
        "id": 16,
        "Longitude": -94.62746,
        "label": "KSCY",
        "hub_name": "Kansas City, MO",
    },
    "17": {
        "Internal": 1,
        "Latitude": 37.77493,
        "Country": "United States",
        "type": "Completed",
        "id": 17,
        "Longitude": -122.41942,
        "label": "SNFN",
        "hub_name": "San Francisco, CA",
    },
    "18": {
        "Internal": 1,
        "Latitude": 38.58157,
        "Country": "United States",
        "type": "Completion 2007 - 2008",
        "id": 18,
        "Longitude": -121.4944,
        "label": "SCRM",
        "hub_name": "Sacramento, CA",
    },
    "19": {
        "Internal": 1,
        "Latitude": 45.52345,
        "Country": "United States",
        "type": "Completion 2007 - 2008",
        "id": 19,
        "Longitude": -122.67621,
        "label": "PTLD",
        "hub_name": "Portland, OR",
    },
    "20": {
        "Internal": 1,
        "Latitude": 47.60621,
        "Country": "United States",
        "type": "Completion 2007 - 2008",
        "id": 20,
        "Longitude": -122.33207,
        "label": "STTL",
        "hub_name": "Seattle, WA",
    },
    "21": {
        "Internal": 1,
        "Latitude": 40.76078,
        "Country": "United States",
        "type": "Completion 2007 - 2008",
        "id": 21,
        "Longitude": -111.89105,
        "label": "SLKC",
        "hub_name": "Salt Lake City, UT",
    },
    "22": {
        "Internal": 1,
        "Latitude": 34.05223,
        "Country": "United States",
        "type": "Completed",
        "id": 22,
        "Longitude": -118.24368,
        "label": "LA03",
        "hub_name": "Los Angeles, CA",
    },
    "23": {
        "Internal": 1,
        "Latitude": 32.71533,
        "Country": "United States",
        "type": "Completion 2007 - 2008",
        "id": 23,
        "Longitude": -117.15726,
        "label": "SNDG",
        "hub_name": "San Diego, CA",
    },
    "24": {
        "Internal": 1,
        "Latitude": 33.44838,
        "Country": "United States",
        "type": "Completion 2007 - 2008",
        "id": 24,
        "Longitude": -112.07404,
        "label": "PHNX",
        "hub_name": "Phoenix, AZ",
    },
}

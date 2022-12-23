import networkx as nx
import matplotlib.pyplot as plt


def ReturnAddress(key):
    return key + " is at the " + Floors[key[1]] + " of the " + Buildings[key[0]] + " Building"
def CheckInputExists(dic, key):
    if key in dic:
        return True
    return False


Floors = {"B": "Basement",
          "G": "Ground Floor",
          "1": "1st Floor",
          "2": "2nd Floor",
          "3": "3rd Floor",
          "4": "4th Floor"
          }
Buildings = {"F": "Fine Arts"
             }

F1_Data = {"Entrance": "Entrance",
           "F108": "Lab",
           "F106": "Room",
           "F102": "Class",
           "F103": "Class",
           "F104": "Class",
           "F105": "Class",
           "F101": "Bathroom",
           "F100": "Corridor",
           "F109": "Lab",
           "F110": "Lab",
           "F111": "Bathroom",
           "F114": "Room",
           "F112": "Class",
           "F113": "Class",
           "F116": "Gallery",
           "F171": "Store Room",
           "F122": "Room",
           "F123": "Room",
           "F135": "Workshop",
           "F124": "Room",
           "F125": "Room",
           "F126": "Room",
           "F127": "Room",
           "F128": "Room",
           "F129": "Room",
           "F130": "Room",
           "F131": "Room",
           "F132": "Room",
           "F133": "Room",
           "F172": "Sound Studio",
           "F142": "Sound Studio",
           "F136": "Electric Room",
           "F137": "Class",
           "F138": "Class",
           "F139": "Class",
           "F140": "Class",
           "F141": "Class",
           "F144": "Bathroom",
           "F145": "Bathroom",
           "F146": "Cinema Studio",
           "F148": "Class",
           "F149": "Class",
           "F150": "Light Current Room",
           "F151": "Room",
           "F153": "Workshop",
           "F154": "Store Room",
           "F155": "Stadium",
           "F157": "Light Current Room",
           "F156": "Room",
           "F160": "Admin Bathroom",
           "F161": "Control",
           "F162": "Control",
           "F163": "Control",
           "F164": "Control",
           "F169": "Room",
           "F165": "Administration ",
           }
F2_Data = {"F201": "Bathroom",
           "F202": "Class",
           "F203": "Class",
           "F204": "Class",
           "F205": "Class",
           "F206": "Room",
           "F208": "Labs",
           "F209": "Labs",
           "F210": "Electric Room",
           "F212": "Lecture Hall",
           "F214": "Room",
           "F215": "Class",
           "F216": "Class",
           "F217": "Bathroom",
           "F219": "Gallery",
           "F220": "Studio",
           "F221": "Studio",
           "F225": "Studio",
           "F230": "Studio",
           "F223": "Bathroom",
           "F228": "Stairs",
           "F229": "Electric Room",
           "F231": "Studio",
           "F227": "Bathroom",
           "F233": "Light Current Room",
           "F234": "Room",
           "F237": "Lobby",
           "F241": "Cafeteria",
           "F240": "Stadium",
           "F245": "Room",
           "F248": "Bathroom",
           "F249": "Affairs",
           "F250": "Affairs",
           "F251": "Affairs",
           "F252": "Affairs",
           "F253": "Affairs",
           "F254": "Affairs",
           "F255": "Affairs",
           "F256": "Affairs",
           "F259": "Room",
           "F257": "Bathroom"}
F3_Data = {
    "F302": "Class",
    "F303": "Class",
    "F304": "Class",
    "F305": "Class",
    "F307": "Corridor",
    "F309": "Lecture Hall",
    "F308": "Electric room",
    "F311": "Lab",
    "F312": "Lab",
    "F314": "Drawing Hall",
    "F315": "Room",
    "F318": "Gallery",
    "F319": "Drawing Hall",
    "F320": "Drawing Hall",
    "F321": "Drawing Hall",
    "F322": "Drawing Hall",
    "F325": "Drawing Hall",
    "F3--": "Mac Design",
    "F332": "Light Current Room",
    "F333": "Room",
    "F334": "Lobby",
    "F347": "PROF Room",
    "F348": "PROF Room",
    "F349": "PROF Room",
    "F350": "PROF Room",
    "F351": "PROF Room",
    "F352": "PROF Room",
    "F353": "PROF Room",
    "F354": "PROF Room",
    "F342": "Vice Dean",
    "F338": "Secretary",
    "F339": "Dean Of Collage",
    "F341": "Meeting Room",
    "F340": "Secretary",
    "F343": "Vice Dean",
    "F357": "Secretary",
    "F358": "Vice Dean",
    "F359": "Collage Council",
    "F360": "Vice Dean",
    "F361": "Secretary",
    "F365": "Light Currant Room",
    "F364": "PROF Room",
    "F367": "PROF Room",
    "F370": "PROF Room",
    "F373": "PROF Room",
    "F376": "PROF Room",
    "F379": "PROF Room",
    "F382": "PROF Room",
    "F388": "PROF Room",
    "F368": "Secretary",
    "F371": "Secretary",
    "F374": "Secretary",
    "F377": "Secretary",
    "F380": "Secretary",
    "F383": "Secretary",
    "F385": "Secretary",
    "F369": "Sec Head",
    "F372": "Sec Head",
    "F375": "Sec Head",
    "F378": "Sec Head",
    "F381": "Sec Head",
    "F384": "Sec Head",
    "F386": "Sec Head"
}
FineArts_Rooms = F1_Data | F2_Data | F3_Data

F1_Nodes = [
    ("Entrance", "F1A", 0),
    ("F1A", "F1B", 1),
    ("F1A", "F1E", 1),
    ("F1A", "F1F", 1),
    ("F1A", "F1G", 1),
    ("F1A", "F1L", 1),
    ("F1B", "F1C", 1),
    ("F1C", "F1D", 1),
    ("F1E", "F1D", 1),
    ("F1G", "F1H", 1),
    ("F1H", "F1I", 1),
    ("F1L", "F1K", 1),
    ("F1K", "F1J", 1),
    ("F1J", "F1I", 1),

    ("F1B", "F109", 0.5),
    ("F1B", "F110", 0.5),
    ("F1C", "F105", 0.5),
    ("F1C", "F104", 0.5),
    ("F1C", "F103", 0.5),
    ("F1C", "F102", 0.5),
    ("F1C", "F102", 0.5),
    ("F1E", "F112", 0.5),
    ("F1E", "F113", 0.5),
    ("F1G", "F122", 0.5),
    ("F1G", "F125", 0.5),
    ("F1H", "F171", 0.5),
    ("F1I", "F142", 0.5),
    ("F1I", "F143", 0.5),
    ("F1I", "F136", 0.5),
    ("F142", "F143", 0.5),
    ("F1J", "F146", 0.5),
    ("F1J", "F147", 0.5),
    ("F1K", "F137", 0.5),
    ("F1K", "F138", 0.5),
    ("F1K", "F139", 0.5),
    ("F1K", "F140", 0.5),
    ("F1K", "F141", 0.5),
    ("F1K", "F148", 0.5),
    ("F1K", "F149", 0.5),
    ("F1K", "F150", 0.5)
]
F2_Nodes = []
F3_Nodes = []
FloorConnections = []


def main():
    # Initialize Directional Graph
    FineArts_Graph = nx.Graph()
    FineArts_Graph.add_weighted_edges_from(F1_Nodes)

    # DEBUGGING: Draws a Graph
    nx.draw_planar(FineArts_Graph, with_labels=True, font_weight='bold')
    plt.show()

    SourceNode = input("Where are you currently at = ")
    while not CheckInputExists(FineArts_Rooms, SourceNode):
        SourceNode = input("Entry not found, Try Again = ")

    TargetNode = input("Where do you wanna go = ")
    while not CheckInputExists(FineArts_Rooms, TargetNode):
        TargetNode = input("Entry not found, Try Again = ")

    # Entrance, F109
    paths = nx.shortest_path(FineArts_Graph)
    print(paths[SourceNode][TargetNode])


if __name__ == "__main__":
    main()

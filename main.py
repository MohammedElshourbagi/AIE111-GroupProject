import ImageProcessing as IP
import networkx as nx
import matplotlib.pyplot as plt


def main():
    # Initialize Directional Graph
    Engineering1stFloor = nx.DiGraph()

    # List of all Rooms & Hallways
    Hallways = [
        # (START, END, WEIGHT)
        (),
        (),
        ()
    ]
    Rooms = [
        (),
        (),
        ()
    ]

    Engineering1stFloor.add_weighted_edges_from(Hallways)
    Engineering1stFloor.add_weighted_edges_from(Rooms)

    # De-referencing ROOMID to dictionary of ROOMID: list of attributes
    def DeReferenceID(string, roomtype):
        Building = string[:]
        Floor = string[:]
        return Building, Floor, roomtype

    ROOMS = {
        "1": DeReferenceID("", ""),
        "2": DeReferenceID("", ""),

    }

    # DEBUGGING: Draws a Graph
    nx.draw(Engineering1stFloor, with_labels=True, font_weight='bold')
    plt.show()
    

if __name__ == "__main__":
    main()

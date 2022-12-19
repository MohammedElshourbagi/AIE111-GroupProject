import ImageProcessing as IP
import PathFindingAlgorithms as PF


def main():
    PIXELS = IP.TranslateImageTo2DArray(r"floorplan.jpg")
    print(PIXELS)  # returns a 2d numpy array


if __name__ == "__main__":
    main()

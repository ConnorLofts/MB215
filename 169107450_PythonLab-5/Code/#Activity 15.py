# Activity 15

import matplotlib.pyplot as plt

def main():
   
    x_coords = [0, 1, 2, 3, 4]
    y_coords = [0, 3, 1, 5, 2]

    plt.plot(x_coords, y_coords)

    plt.show()

if __name__ == "__main__":
    main()

left_edges = [0, 10, 20, 30, 40]
heights = [100, 200, 300, 400, 500]

plt.bar(left_edges, heights)
plt.show()

values = [20, 60, 80, 40]
plt.pie(values)
plt.show()

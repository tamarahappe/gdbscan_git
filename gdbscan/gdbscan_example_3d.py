from gdbscan import GDBSCAN, Points
import math



UNCLASSIFIED = -2


class Point:
    def __init__(self, x, y, z, value):
        self.x = x
        self.y = y
        self.z = z
        self.val = value
        self.cluster_id = UNCLASSIFIED

    def __repr__(self):
        return '(x:{}, y:{}, z:{}, val:{}, cluster:{})' \
            .format(self.x, self.y, self.z, self.val, self.cluster_id)

def n_pred3d(p1 : Point, p2: Point):
    return all([math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2 + (p1.z - p2.z)**2) <= 1]
                )

def w_card(points):
    return len(points)



###############
# Plotting functions 
##############



def scatter3d(dictionary_clusters):
    #in is dictionary with clusters and data points in each cluster
    #out is 3dscatter plot of the clusters and data points
    import matplotlib.pyplot as plt
    cluster = []
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    for key, items in dictionary_clusters.items():

        x =[]
        y = []
        z = []
        for i in items:
            cluster.append(key)
            x.append(i.x)
            y.append(i.y)
            z.append(i.z)
        if key == -1:
            colour = "black"
            label = "noise"
        else:
            colour = 'red'
            label = f"Cluster #{key}"
        ax.scatter(x, z, y, s=40, label=label) #c=colour,
    ax.set_xlabel("X")    
    ax.set_ylabel("Y")    
    ax.set_zlabel("Z")
    ax.legend()
    ax.set_title("Gdbscan in 3D")
    plt.show()


###############
# TESTING on fake data
##############

def test():
    p1 = Point(0, 0, 0, 1)
    p2 = Point(0, 1, 0, 2)
    p3 = Point(1, 0, 1, 3)
    p4 = Point(2, 1, 2, 1)
    p5 = Point(2, 2, 0, 2)
    p6 = Point(1, 2, 1, 3)

    points = [p1, p2, p3, p4, p5, p6]

    clustered = GDBSCAN(Points(points), n_pred3d, 2, w_card)
    # print(clustered)
    scatter3d(clustered)


def test2():
    p1 = Point(0, 0, 0, 1)
    p2 = Point(0, 1, 0, 0)
    p3 = Point(1, 0, 1, 0)
    p4 = Point(2, 1, 2, 0)
    p5 = Point(2, 2, 0, 1)
    p6 = Point(1, 2, 1, 1)
    p7 = Point(1, 2, 2, 1)
    p8 = Point(1, 2, 3, 1)
    p9 = Point(2, 2, 1, 1)
    p10 = Point(2, 2, 2, 1)
    p11 = Point(2, 2, 3, 1)
    p12 = Point(1, 3, 1, 0)

    points = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11]

    clustered = GDBSCAN(Points(points), n_pred3d, 2, w_card)
    # print(clustered)
    scatter3d(clustered)


##############

if __name__ == '__main__':
    test()
    test2()


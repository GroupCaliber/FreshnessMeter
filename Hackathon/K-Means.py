import cv2
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sys


class DominantColors:
    CLUSTERS = None
    IMAGE = None
    COLORS = None
    LABELS = None
    rgb = None

    def __init__(self, image, clusters=3):
        self.CLUSTERS = clusters
        self.IMAGE = image

    def dominantColors(self):
        # read i
        img = cv2.imread(self.IMAGE)

        # convert to rgb from bgr
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # reshaping to a list of pixels
        img = img.reshape((img.shape[0] * img.shape[1], 3))

        # save image after operations
        self.IMAGE = img

        # using k-means to cluster pixels
        kmeans = KMeans(n_clusters=self.CLUSTERS)
        kmeans.fit(img)

        # the cluster centers are our dominant colors.
        self.COLORS = kmeans.cluster_centers_

        # save labels
        self.LABELS = kmeans.labels_

        # returning after converting to integer from float
        return self.COLORS.astype(int)

    def rgb_to_hex(self, rgb):
        return '#%02x%02x%02x' % (int(rgb[0]), int(rgb[1]), int(rgb[2]))

    def plotClusters(self):
        # plotting
        fig = plt.figure()
        ax = Axes3D(fig)
        for label, pix in zip(self.LABELS, self.IMAGE):
            ax.scatter(pix[0], pix[1], pix[2], color=self.rgb_to_hex(self.COLORS[label]))
        plt.show()

img = "res/out20.jpg"

import numpy as np
from sklearn.cluster import KMeans
XX=cv2.imread(img)
print(XX.shape)
xx=np.reshape(XX,(XX.shape[0]*XX.shape[1],3))
print(xx.shape)
kmeans = KMeans(n_clusters=5, random_state=0).fit(xx)

colors=kmeans.cluster_centers_

col=kmeans.predict(xx)
col=np.reshape(col,(XX.shape[0],XX.shape[1]))
cv2.imwrite("col.jpg",col)


# clusters = 5
# dc = DominantColors(img, clusters)
# colors = dc.dominantColors()
print(colors)
fig = plt.figure()
ax = fig.add_subplot(111,projection = "3d")

ax.scatter(colors[:, 0], colors[:, 1], colors[:, 2])
ax.set_xlabel('r')
ax.set_ylabel('g')
ax.set_zlabel('b')
fig.add_axes(ax)
plt.show()

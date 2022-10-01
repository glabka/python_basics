import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from imageio import imread
# if not set by default this will force the plots to be vector based not raster
# from IPython import display
# display.set_matplotlib_formats('svg')

# -------------------- plotting with matplotlib.pyplot --------------------
plt.plot(3, 4, 'o', label="blue circle") # also 's' for square, 'p' for pentagram, '^' for triangle etc.
plt.plot(2, 4.2, 'r^', label="red triangle") # red triangle
plt.legend() # plot legend
# alternative legend
# plt.plot(3, 4, 'o')
# plt.plot(2, 4.2, 'r^')
# plt.legend(["blue", "read"]) # legend corresponds to order of things plotted
plt.xlabel("x")
plt.ylabel("y")
plt.title("My Plot")
plt.show()

# plotting curve
plt.plot([0, 1, 3], [0, 2, -1], 'ms-') # magenta squares with connecting lines
plt.gca().set_aspect(0.1) # gca = get current axes; sets ratio between units of length of x and y axes
plt.show()

# subplot
plt.subplot(1, 2, 1) # one row, two columns, index of plot (indexed from 1)
plt.plot(np.random.randn(10))

plt.subplot(1, 2, 2) # one row, two columns, index of plot
plt.plot(np.random.randn(10))
plt.show()

# subplots
fig, ax = plt.subplots(1, 2, figsize=(10, 3)) # 1 row, two columns, fig = figure and ax axis, figsize = whole figure size
x = np.arange(10)

ax[0].plot(x, x**2, 'b')
ax[0].set_xlabel('x')
ax[0].plot(x, x, 'k')
ax[1].plot(x, np.sqrt(x), 'r')

plt.tight_layout() # nicer layout (no overlap etc.)
plt.show()

# -------------------- plotting with seaborn --------------------
# works on top of matlplotlib
n = 200
D = np.zeros((n, 2))

D[:, 0] = np.linspace(0, 10, n) + np.random.randn(n) # random to add some noise
D[:, 1] = D[:, 0]**2 + np.random.randn(n) * 10

sns.jointplot(D[:,0], D[:,1])
plt.show()

# other example (two variables)
x = np.linspace(-1, 1, n)
y1 = x**2
y2 = np.sin(3 * x)
y3 = np.exp(-10 * x**2)

sns.scatterplot(x=y1, y=y2, hue=y3, legend=False, palette='Spectral')
plt.show()

# -------------------- visualization of matrices (matplotlib) --------------------
m = 3
n = 5
M = np.random.randint(10, size=(m, n))
plt.imshow(M)

for i in range(len(M)):
    for j in range(len(M[i])):
        plt.text(j, i, str(M[i, j]), fontsize=20, horizontalalignment='center', verticalalignment='center') # plots text on specified coordinates

plt.colorbar()
plt.show()

# -------------------- importing images (imageio) --------------------
# imread parameter -> filename or url
# img = imread("https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Einstein_1921_by_F_Schmutzer_-_restoration.jpg/800px-Einstein_1921_by_F_Schmutzer_-_restoration.jpg")
# print(img.shape)
img = imread('https://upload.wikimedia.org/wikipedia/en/8/86/Einstein_tongue.jpg')
plt.imshow(img)
plt.show()
plt.imshow(img, cmap='gray', vmin=50, vmax=200) # cmap = color map, vmin - clipping all values smaller than 50 -> enhancing contrast
# plt.xticks([]) # no tick on x axes -> not necessary useful for image
plt.axis('off') # no axes
plt.show()

plt.hist(img.flatten(), bins=100) # flatten -> matrix represented by array of arrays converted to just one array; bins = into how many intervals the data is devided
plt.show()

# -------------------- saving plots --------------------
x = np.linspace(0.5, 5, 10)
y = np.log(x)
plt.plot(x, y, 'bo-')
plt.savefig('test_plot.png') # raster
plt.savefig('test_plot.pdf') # vector
plt.show()
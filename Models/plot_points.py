# importing the module
import json
import matplotlib.pyplot as plt
import numpy as np
  
# reading the data from the file
with open('data/data1.txt') as f:
    data = f.read()
  
print("Data type before reconstruction : ", type(data))
      
# reconstructing the data as a dictionary
js = json.loads(data)
  
print("Data type after reconstruction : ", type(js))
# print(js["results"])
lats = []
longs = []

for item in js["results"]:
  lat, long = item["geometry"]["location"].values()
  lats.append(lat)
  longs.append(long)

#plot gradient
x_grid = np.linspace(50, 80, 100)   
y_grid = np.linspace(80, 280, 100)   
X, Y = np.meshgrid(x_grid, y_grid)

#data points
plt.scatter(lats, longs, color = 'blue')

# decision boundary
plt.xlabel('lats')
plt.ylabel('longs')
plt.title('lda contour and decision boundary')
# plt.savefig("lda.pdf")
plt.show()
  

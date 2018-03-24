import numpy as np
import time
import matplotlib.pyplot as plt

file_path = '/Users/apple/ownCloud/Yue/python/test/t2_file'
a = np.linspace(0,10,500000)
start_time = time.time()
with open(file_path, 'w') as f:
    np.save(f,a)
end_time = time.time()
print(end_time-start_time)

start_time = time.time()

with open(file_path,'r') as f:
    f.seek(0)
    data = np.load(f)
end_time = time.time()
print(end_time-start_time)

plt.plot(data)
plt.show()

import numpy as np
 
var=np.random.randint(1,20,15)

print("ORGINAL ARRAY")
print(var)

print("\n------------------------------------------------------------\n")

array =var.reshape(3,5)
print("RESHAPED ARRAY")
print(array)

print("\n------------------------------------------------------------\n")

print("SETTING MAX VALUE TO 0")
array = np.where(array==[[i] for i in np.amax(array,axis=1)],0,array)
print(array)

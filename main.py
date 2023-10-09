# This entrypoint file to be used in development. Start by reading README.md
import mean_var_std
from unittest import main

dict1 = mean_var_std.calculate([0,1,2,3,4,5,6,7,8])
#print(dict1)
print("{")
for k,v in dict1.items():
  
  print("\'{}\' : {}".format(k,v))
print("}")


#print(mean_var_std.calculate([0,1,2,3,4,5,6,7,8]))

# Run unit tests automatically
main(module='test_module', exit=False)  
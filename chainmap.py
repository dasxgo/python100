from collections import ChainMap

details = {"first_name" :"David", "last_name": "Sarmiento"}
more_details = {"Country" : "Colombia", "profession" : "Engineer"} 


chain = ChainMap(details, more_details)


# list the keys 
print(list(chain.keys()))

# list the values
print(list(chain.values()))

# Get the country value
print(chain["Country"])

# try another example

print(chain["last_name"])

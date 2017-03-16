import nba
#print the method list
nba.print_method_list()

#get the list of all the methods
methods = nba.get_method_list()

#print all the parameters for each function
for method in methods:
    params = nba.get_params(method)
    print(method + " has parameters: " + ", ".join(map(str, params)))

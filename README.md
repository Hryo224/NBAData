# NBAData

NBAData is a simple wrapper for the http://data.nba.net api. 

NBAData provides a simple method that allows for the user to call the nba_data function with the endpoint name and the parameters to return the raw json. 

In order to see the list of methods you can call the print_methods_list() function. You can also return a list of all the methods with get_method_list(). Additionally, there is a function to get all the parameters a given function. 

Some examples:
```python
import nba
#print the method list
nba.print_method_list()

#get the list of all the methods
methods = nba.get_method_list()

#print all the parameters for each function
for method in methods:
  params = nba.get_params(method)
  print(method + " has parameters " + ", ".join(map(str, params)))
```
To use NBAData, simply call one function, nba_data, which takes in the function name and the function's given parameters:
```python
from nba import nba_data
from pprint import pprint
#Get the scoreboard for 12/05/2016
scoreboard = nba_data("scoreboard", 20161205)
for game in scoreboard.get('games'):
  game_id = game.get('gameId')
  #Get the recap for the games on 12/05/2016
  recap = nba_data("recap_article", 20161205, game_id)
  pprint(recap)
  ```
  



# Assignment 3 
# Dijkstra Baalti Algorithm
# Group Members 
# 1.	Ali Murtaza (39)
# 2.	Sardar Moazzam Sajid (17)
# 3.	Hamza Iqbal (10)
# 4.	Muhammad Asad Ayyub (25)



# Read the data from the File      
dist = open('ha30_dist.txt', 'r')    
dists = dist.read().split()
citdist_j = open('ha30_name.txt','r') 
cities = citdist_j.read().splitlines()



index_dist = 3
graph = {}
for i in range(0,len(cities)):                   
    city_data = []
    for j in range(0,len(cities)):
        city_with_dist = (cities[j], int(dists[index_dist]))  # Converted the  graph data to into dictionary named graph
        city_data.append(city_with_dist)
        index_dist += 1 
    c = {cities[i]:city_data}
    graph.update(c)                   # Stored the values with key as city name and its adjacent city tuple which has name and distance
    
def Dijsktra_Baalti(graph, root):
    bucket = []
    queue = []
    parent = {}
    treeLevels = {}
    Up_dists = {}    # Updated distances dictionary
    short_paths = {} # This dictionary is made to keep track of shortest paths


    treeLevels[root] = 0
    parent[root] = '' 
    dict_keys = list(graph.keys())               # Name of all cities which are keys of dict_graph
    
    for i in range(len(dict_keys)):
        if dict_keys[i] == root:
            b = dict_keys[i]
            Up_dists[b] = 0    # Updated distances dictionary initializing source with 0
        else:
            a = dict_keys[i]
            Up_dists[a] = 99999999999999999999999999999999999 # Updated distances dictionary initializing other vecticess with infinity
   


    
    bucket.append(root)
    queue.extend(graph[root])
    print("Queue",queue,"Bucket",bucket)
    

    for v in graph[root]:
        treeLevels[v] = treeLevels[root] + 1
        parent[v] = root
       
      
    while len(queue) !=0 :
        temp = 10000000000000000000000000000000  
       
        for v in bucket:
            
            b_graph= graph[v]  # Graph of city in bucket
            updated_dist = Up_dists[v] # Updated distance of city coming from bucket
           
            for j in b_graph:
              
                dist_j = j[1]
                name_j = j[0]
                dist_vj = updated_dist + dist_j  # New Distances Updated 
    
                if j in queue and name_j not in bucket and dist_j != 0 :
                    if dist_vj < temp:
                        temp = dist_vj
                        prior = j
                        a = (v,name_j)     # two cities root and destination 
                        Up_dists[name_j] = temp # Distances between root and destination updated 
                        short_paths[a] = temp  # Distances between root and destination stored in short path dictionary  with cities as key and distance as value

                        
            for i in range(len(queue)):
                if queue[i] == prior:
                    queue[0],queue[i] = queue[i],queue[0] # Swap city on the basis of priority to pop  from queue
      



            
        TupleCity = queue.pop(0)
        NameCity = TupleCity[0]
        if NameCity not in bucket:
            bucket.append(NameCity)
            city_graph = graph[NameCity]
            
            queue.extend(city_graph) 
            for v in graph[NameCity]:
                if v not in treeLevels.keys():
                   
                    treeLevels[v] = treeLevels[TupleCity] + 1
                    parent[v] = NameCity

        print("Queue",queue,"Bucket",bucket)

    return bucket,parent,short_paths,Up_dists

# This Function can be used to find shortest route between two cities      
def shortest_route(graph,root, destination):
    bucket,parent,short_dists,levels = Dijsktra_Baalti(graph, root) # Calling Dijistra Algorithm to get short route
    route = short_dists # Using short path dictionary because it has all short paths with their distances from root
    tmp_list = []
    root_dest = (root,destination)
    for i,j in route.items():
        if i == root_dest:              # Direct Path
            city_with_dist = (i,j)          
            return city_with_dist
        if i[0] == root:      
            tmp_list.append(i)
    for i in tmp_list:               # if Not direct path
        real_path = []
        t = route[i]
        o = (i,t)
        real_path.append(o)
        temp = i[1]
        for j,k in route.items():     # Checking the paths which has start element root to know that which path has our destination 
            if temp == j[0]:         
                z = (j,k)
                real_path.append(z)
                temp = j[1]

            if temp == destination:  # Checking if our destination is found or not if found then return that path
                return real_path
    x = print("Invalid cities")
    return x                         # If input is invalid




# This Function can be used to find shortest route to travel all 30 cities starting from any city of choice     
def shortest_tour(graph, root):
    bucket = []
    queue = []
    parent = {}
    treeLevels = {}
    Up_dists = {}
    short_paths = {}   # It has track of all  paths starting with root 
    route = {}         #  It has the track of the shortest path travling from root   and  visting every other, World Tour 


    treeLevels[root] = 0
    parent[root] = '' 
    dict_keys = list(graph.keys())
  
    for i in range(len(dict_keys)):
        if dict_keys[i] == root:
            b = dict_keys[i]
            Up_dists[b] = 0
        else:
            a = dict_keys[i]
            Up_dists[a] = 99999999999999999999999999999999999
    
   

    bucket.append(root)
    queue.extend(graph[root])
 
    

    for v in graph[root]:
        treeLevels[v] = treeLevels[root] + 1
        parent[v] = root
       
        
        
    while len(queue) !=0 :
        
        
        temp =1000000000000000
        v = bucket[len(bucket)-1]
       
        b= graph[v]
        b_graph = Up_dists[v]  
        for j in b:
             
            dist_j = j[1]
            name_j = j[0]
            dist_vj = b_graph + dist_j
          
            if j in queue and name_j not in bucket and dist_j != 0 :
                if dist_vj < temp:
                    temp = dist_vj
                    prior = j
                    a = (v,name_j)  # Starting and ending city
                    Up_dists[name_j] = temp    # Starting and ending city distance updated with previous distance added
                    short_paths[a] = temp      # Updated distance also stored in Short Paths to keep track
                route_dist = temp       # Short Distance Stored in route dist    
                route_cities = a        # Short Distances of city stored in variable route_cities


                        
        for i in range(len(queue)):
            if queue[i] == prior:
                queue[0],queue[i] = queue[i],queue[0]
    

        route[route_cities] = route_dist
        TupleCity = queue.pop(0)
        NameCity = TupleCity[0]
        DistCity = TupleCity[1]
        if NameCity not in bucket and DistCity != 0:
            bucket.append(NameCity)
            a = graph[NameCity]

            queue = []            # Emptying Queue each time since we dont want to keep track of previous root cities
            queue.extend(a) 
            for v in graph[NameCity]:
                if v not in treeLevels.keys():
                  
                    treeLevels[v] = treeLevels[TupleCity] + 1
                    parent[v] = NameCity

        print("Queue",queue,"Bucket",bucket)
 

    city_list = [] # List to check if every city has been visited or not and if not which city has not been visited
    for i in dict_keys:
        found = True
        for j in bucket:
            if i == j:
                found = False 
        if found == True:
            city_list.append(i)
    
        
    if len(city_list) == 0:
        return bucket,route
    else:
        for i in n_list:               # Visiting  City  which hasn't been visted 
            path_list = list(route)
            dist_list = list(route.values())
            temp_dist = dist_list[len(dist_list)-1]
            c_location = path_list[len(path_list)-1]
            city_from = c_location[1]

            g = shortest_route(graph, city_from, i)

            already_travel = 0
            for i in g:
                path_dist = i[1]
                city_path = i[0]
                city_dist = path_dist - already_travel
                already_travel = path_dist              
                dist_travel = city_dist + temp_dist
                route[city_path] = dist_travel
                path_list = list(route)
                dist_list = list(route.values())
                temp_dist = dist_list[len(dist_list)-1]

        return bucket,route            # Returning Bucket and Shortest World Tour Route    
            
            
# This Function can be used to find longest route between two cities      
def longest_tour(graph, root):
    bucket = []
    queue = []
    parent = {}
    treeLevels = {}
    Up_dists = {}
    long_paths = {} # Keep Track of all paths with high distances priority
    route = {}


    treeLevels[root] = 0
    parent[root] = '' 
    dict_keys = list(graph.keys())
  
    for i in range(len(dict_keys)):
        if dict_keys[i] == root:
            b = dict_keys[i]
            Up_dists[b] = 0
        else:
            a = dict_keys[i]
            Up_dists[a] = 99999999999999999999999999999999999
    
   

    bucket.append(root)
    queue.extend(graph[root])
 
    

    for v in graph[root]:
        treeLevels[v] = treeLevels[root] + 1
        parent[v] = root
       
        
        
    while len(queue) !=0 :
        
        
        temp =0
        v = bucket[len(bucket)-1]  # Last Element of Bucket
       
        b= graph[v]
        b_graph = Up_dists[v] # Graph of Last Bucket element
        for j in b:
             
            dist_j = j[1]
            name_j = j[0]
            dist_vj = b_graph + dist_j      
          
            if j in queue and name_j not in bucket and dist_j != 0 :
                if dist_vj > temp:
                    temp = dist_vj
                    prior = j
                    a = (v,name_j)
                    Up_dists[name_j] = temp
                    long_paths[a] = temp
                route_dist = temp     # Most Long Distance between Two cities one root and other adjacent
                route_cities = a       #  two Cities which has Most long route


                        
        for i in range(len(queue)):
            if queue[i] == prior:
                queue[0],queue[i] = queue[i],queue[0]
    

        route[route_cities] = route_dist
        TupleCity = queue.pop(0)
        NameCity = TupleCity[0]
        DistCity = TupleCity[1]
        if NameCity not in bucket and DistCity != 0:
            bucket.append(NameCity)
            a = graph[NameCity]

            queue = []
            queue.extend(a) 
            for v in graph[NameCity]:
                if v not in treeLevels.keys():
                  
                    treeLevels[v] = treeLevels[TupleCity] + 1
                    parent[v] = NameCity

        print("Queue",queue,"Bucket",bucket)
 
    return bucket,route    



# # This Function can be used to findlongest route between two cities      
def longest_route(graph, root,destination):
    bucket = []
    queue = []
    parent = {}
    treeLevels = {}
    Up_dists = {}

    treeLevels[root] = 0
    parent[root] = '' 
    dict_keys = list(graph.keys())
  
    for i in range(len(dict_keys)):
        if dict_keys[i] == root:
            b = dict_keys[i]
            Up_dists[b] = 0
        else:
            a = dict_keys[i]
            Up_dists[a] = 99999999999999999999999999999999999
    
    long_paths = {}
    route = {}

    bucket.append(root)
    queue.extend(graph[root])
 
    

    for v in graph[root]:
        treeLevels[v] = treeLevels[root] + 1
        parent[v] = root
       
        
        
    while len(queue) !=0 :
        
        
        temp =0
        v = bucket[len(bucket)-1]
       
        b= graph[v]
        b_graph = Up_dists[v]
        for j in b:
             
            dist_j = j[1]
            name_j = j[0]
            dist_vj = b_graph + dist_j
          
            if j in queue and name_j not in bucket and dist_j != 0 and name_j != destination:
                if dist_vj > temp:
                    temp = dist_vj
                    prior = j
                    a = (v,name_j)
                    Up_dists[name_j] = temp
                    long_paths[a] = temp
                route_dist = temp
                route_cities = a


                        
        for i in range(len(queue)):
            if queue[i] == prior:
                queue[0],queue[i] = queue[i],queue[0]
    

        route[route_cities] = route_dist
        TupleCity = queue.pop(0)
        NameCity = TupleCity[0]
        DistCity = TupleCity[1]
        if NameCity not in bucket and DistCity != 0:
            bucket.append(NameCity)
            a = graph[NameCity]

            queue = []
            queue.extend(a) 
            for v in graph[NameCity]:
                if v not in treeLevels.keys():
                  
                    treeLevels[v] = treeLevels[TupleCity] + 1
                    parent[v] = NameCity

        print("Queue",queue,"Bucket",bucket)
    
    temp_dists = list(route.values())         
    temp_cities = list(route.keys())
    x = temp_cities[len(temp_cities)-1]
    city = x[1]
    city_dist = temp_dists[len(temp_dists)-1]
    for i in graph[city]:
        if i[0] == destination:
            tmp  = (city,destination)
            tmp_dist = city_dist + i[1]
            route[tmp] = tmp_dist
            return bucket,route     
    
                           
                          

# Checking Distances of All cities and knowing to start from which to get the most shortest  or best  path for world tour   
def world_tour_best(graph):
    list_t =[]
    temp= 10000000000000000000000
    for i in range(len(cities)):
        bucket,path = shortest_tour(graph, cities[i]) 
        temp_dists = list(path.values())
        path_dist = temp_dists[len(temp_dists)-1]
        list_t.append(path_dist)
        if path_dist < temp:
            temp = path_dist
            shortest_path = path
    return shortest_path

# Checking Distances of All cities and knowing to start from which to get the most longest or worst path for world tour   
def world_tour_worst(graph):
    list_t =[]
    temp= 0
    for i in range(len(cities)):
        bucket,path = longest_tour(graph, cities[i])
        temp_dists = list(path.values())
        path_dist = temp_dists[len(temp_dists)-1]
        list_t.append(path_dist)
        if path_dist > temp:
            temp = path_dist
            longest_path = path
    return longest_path


    

while True:
    print('\n \n  ')
    print("Press 1 if want to take a  shortest world tour starting from your desired city")
    print("Press 2 if want to take a  longest world tour starting from your desired city")
    print("Press 3 if want to take a  best world tour from these cities" )
    print("Press 4 if want to take a  worst world tour from these cities")
    print("Press 5 if want to take the  shortest route between two cities")
    print("Press 6 if want to take the longest route  between two cities")
    print("Press 0 to exit")
    QNo= int(input())
    if QNo == 1:
        city_name = input(print("Enter desired city name from which you start your tour from given below cities",'\n \n', cities))
        bucket,route = shortest_tour(graph, city_name)
        print(" \n The shortest path of world tour starting from",city_name, 'is given below','\n \n', route)
    elif QNo == 2:
        city_name = input(print("Enter desired city name from which you start your tour from given below cities",'\n \n', cities))
        bucket,route = longest_tour(graph, city_name)
        print(" \n The longest path of world tour starting from",city_name, 'is given below','\n \n', route)
    elif QNo == 3:
        best_path = world_tour_best(graph)
        print(" \n The best path to follow to do a world tour given these cities is below \n \n  ")
        print(best_path)
    elif QNo == 4:
        worst_path = world_tour_worst(graph)
        print(" \n The worst path to follow to do a world tour given these cities is below \n \n  ")
        print(worst_path)
    elif QNo == 5:
        origin = input(print(cities," \n Enter desired city name from which you start your journey from given above cities",' \n'))
        destination = input(print(cities," \n Enter desired city name at which you end your journey from given above cities",' \n'))
        route = shortest_route(graph, origin, destination)
        print( " \n The shortest path starting from ",origin,'to ',destination,'is given below','\n' , route)
    elif QNo == 6:
        origin = input(print(cities, "Enter desired city name from which you start your journey from given above cities",'\n \n' ))
        destination = input(print(cities, "Enter desired city name at which you end your journey from given above cities",'\n \n'))
        bucket, route = longest_route(graph, origin, destination)
        print( " \n The longest path starting from ",origin,'to ',destination,'is given below','\n', route)
    elif QNo == 0 :
        print("  Stop Traveling")
        break
    else:
        print("Wrong Input")


              
    





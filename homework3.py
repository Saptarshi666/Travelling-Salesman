import random
import numpy as np
def mutate1(next_generation,Chance_to_mutate,childfitnesslist,childfitnesslistcity):
    i = 0
    j = 0.1 * len(next_generation)
    while i < j:
        selected_child = random.choice(next_generation)
        index_of_selected_child = childfitnesslistcity.index(selected_child)
        chance_to_change = Chance_to_mutate[index_of_selected_child]
        random_prob = random.uniform(0,1)
        if chance_to_change > random_prob:
            index_of_selected = next_generation.index(selected_child)
            index1 = random.randint(1,len(selected_child)-2)
            index2 = random.randint(1,len(selected_child)-2)
            startindex = -1
            endindex = -1
            if index1 <= index2:
                startindex = index1
                endindex = index2
            else:
                startindex = index2
                endindex = index1
            if startindex != endindex:
                temp = selected_child[startindex]
                selected_child[startindex] = selected_child[endindex]
                selected_child[endindex] = temp
            next_generation[index_of_selected] = selected_child
            i = i +1

def mutate(next_generation):
    i = 0
    j = 0.1 * len(next_generation)
    while i < j:
        selected_child = random.choice(next_generation)
        index_of_selected = next_generation.index(selected_child)
        index1 = random.randint(1,len(selected_child)-2)
        index2 = random.randint(1,len(selected_child)-2)
        startindex = -1
        endindex = -1
        if index1 <= index2:
            startindex = index1
            endindex = index2
        else:
            startindex = index2
            endindex = index1
        if startindex != endindex:
            temp = selected_child[startindex]
            selected_child[startindex] = selected_child[endindex]
            selected_child[endindex] = temp
        next_generation[index_of_selected] = selected_child
        i = i +1
    

def chance_of_breeding(fitnesslistcity,matingpool):
    chance_to_breed = [-1] * len(matingpool)
    i = 0
    if len(matingpool) >= 10:
        while i < len(matingpool):
            path = matingpool[i]
            index_of_path = fitnesslistcity.index(path)
            top_10 = 0.1 * len(fitnesslistcity)
            if  0 <= index_of_path and index_of_path <= top_10 -1 :
                chance_to_breed[i] = 0.7
            elif top_10 <= index_of_path and index_of_path <= (3*top_10) -1:
                chance_to_breed[i] = 0.6
            elif (3*top_10) <= index_of_path and index_of_path <= (6*top_10) -1 :
                chance_to_breed[i] = 0.5
            elif (6*top_10) <=index_of_path and index_of_path <= (8*top_10) -1 :
                chance_to_breed[i] = 0.4
            elif (8*top_10) <= index_of_path and index_of_path <= (9* top_10) -1 :
                chance_to_breed[i] = 0.2
            else:
                chance_to_breed[i] = 0.1
            i = i +1
        return chance_to_breed
    else:
        while i < len(matingpool):
            path = matingpool[i]
            index_of_path = fitnesslistcity.index(path)
            if index_of_path == 0:
                chance_to_breed[i] = 0.7
            elif 1 <= index_of_path and index_of_path < 2:
                chance_to_breed[i] = 0.6
            elif 2<= index_of_path and index_of_path < 4:
                chance_to_breed[i] = 0.4
            else:
                chance_to_breed[i] = 0.1
            i = i +1
        return chance_to_breed
def distance_between_cities(Matrix,num):
    m = [[0 for i in range(num)] for j in range(num)]
    i = 0
    j = 0
    while i < num:
        j = 0
        while j < num :
            
            diff_in_x_sq = (Matrix[i][0] - Matrix[j][0])**2
            diff_in_y_sq = (Matrix[i][1]- Matrix[j][1])**2
            diff_in_z_sq = (Matrix[i][2]-Matrix[j][2])**2
            distance = np.sqrt(diff_in_x_sq+diff_in_y_sq+diff_in_z_sq)
            m[i][j] = distance
            j = j +1
        i = i +1
    return m

def breeding(fitnesslist,fitnesslistcity,matingpoolsize,matingpool,bestofgeneration,nextgeneration):
    probability_to_breed = chance_of_breeding(fitnesslistcity,matingpool)
    i = 0
    a = 0
    while i < len(fitnesslist) - len(bestofgeneration):
        current_generation = matingpool
        parent1 = random.choice(current_generation)
        index = current_generation.index(parent1)
        current_generation.remove(parent1)
        parent2 = random.choice(current_generation)
        child =['']* len(parent2)
        current_generation.insert(index,parent1)
        pb_parent1 = probability_to_breed[matingpool.index(parent1)]
        pb_parent2 = probability_to_breed[matingpool.index(parent2)]
        if pb_parent1 + pb_parent2 >= 0.84:
            index1 = random.randint(0,len(parent1)-2)
            index2 = random.randint(0, len(parent2)-2)
            startindex = -1  
            endindex = -1
            if(index1>=index2):
                startindex = index2
                endindex = index1
            else:
                startindex = index1
                endindex = index2
            subtstring = parent1[startindex:endindex+1]
            j = 0
            k = startindex
            while j < len(subtstring):
                child[k] = subtstring[j]
                k= k + 1
                j = j +1
            j = 0
            while j < startindex:
                child[j] = parent2[j]
                j = j + 1
            j = endindex + 1
            while j < len(parent2):
                child[j] = parent2[j]
                j = j + 1
            if child[0] != child[len(child) -1]:
                child[len(child)-1] = child[0]
            j = 0
            test1 = parent2[0:len(parent2)-1]
            test2 = child.copy()
            repeatingpositions = [-1] * len(parent2)
            k = 0
            while j < len(child)-1:
                character_to_be_checked = child[j]
                if character_to_be_checked in test1:
                    index_of_checked_character = test1.index(character_to_be_checked)
                    test1.pop(index_of_checked_character)
                else:   
                    repeatingpositions[k] = j
                    k = k +1
                j = j +1
            j = 0
            while repeatingpositions[j] != -1:
                position_of_repeating_in_child = repeatingpositions[j]
                child[position_of_repeating_in_child] = test1[j]
                j = j +1
            nextgeneration[i] = child
            i = i +1
                
 




def selectbest(matingpool,fitnesslist,fitnesslistcity):
    i = 0
    if(len(matingpool)>=5):
        bestofgeneration = [''] *5
        generation = matingpool
        while i < 5:
            best = generation[0]
            j = 0
            while j < len(generation):
                bestindex = fitnesslistcity.index(best)
                challengerindex = fitnesslistcity.index(generation[j])
                if fitnesslist[challengerindex] > fitnesslist[bestindex]:
                    best = generation[j]
                j = j +1
            bestofgeneration[i] = best
            generation.remove(best)
            i = i +1
        return bestofgeneration
    else:
        bestofgeneration = [''] * 1
        generation = matingpool
        while i < 1:
            best = generation[0]
            j = 0
            while j < len(generation):
                bestindex = fitnesslistcity.index(best)
                challengerindex = fitnesslistcity.index(generation[j])
                if fitnesslist[challengerindex] > fitnesslist[bestindex]:
                    best = generation[j]
                j = j + 1
            bestofgeneration[i] = best
            generation.remove(best)
            i = i + 1
        return bestofgeneration


def totalsum(fitnesslist):
    sum = 0
    for i in range(0,len(fitnesslist)):
        sum = sum + fitnesslist[i]
    return sum

def selection(fitnesslist,fitnesslistcity, elitesize):
    total_fitness = totalsum(fitnesslist)
    i = 0
    if len(fitnesslistcity) >= elitesize:
        matingpool = [""] * elitesize
        while i < elitesize:
            value = random.uniform(0, total_fitness)
            j = 0
            sum = 0
            while sum < value:
                sum = sum + fitnesslist[j]
                j = j +1
            if j == 0 :
                matingpool[i] = fitnesslistcity[0]
            else:
                matingpool[i] = fitnesslistcity[j-1]
            i = i + 1
        return matingpool
    else:
        matingpool = [""] * len(fitnesslistcity)
        while i < len(fitnesslistcity):
            value = random.uniform(0, total_fitness)
            j = 0
            sum = 0
            while sum < value:
                sum = sum + fitnesslist[j]
                j = j +1
            if j == 0 :
                matingpool[i] = fitnesslistcity[0]
            else:
                matingpool[i] = fitnesslistcity[j-1]
            i = i + 1
        return matingpool

   
def calculatedistance(route,distance_between_cities):
    j = 0
    distace = 0;
    while j < len(route) -1:
        k = int(route[j])
        l = int(route[j+1])
        if k <= l:
            distace = distace + distance_between_cities[k][l]
        else:
            distace = distace +distance_between_cities[l][k]
        j = j + 1
    return distace

def fitnessppopulation(fitnesslist,fitnesslistcity,initiallist,Dict,distance_between_cities):
    for i in range (0, len(initiallist)):
        ilist = tuple(initiallist[i])
        distance = -1
        if ilist not in Dict:
            list_Rev = ilist[::-1]
            a1 = tuple(list_Rev)
            if a1 not in Dict:
                distance = calculatedistance(initiallist[i],distance_between_cities)
                Dict[ilist] = distance
            else:
                distance = Dict[a1]
        else:
            distance = Dict.get(ilist)
        fitness = 1/distance
        j = 0
        while (True):
            if fitnesslist[j] < fitness:
                fitnesslist.insert(j,fitness)
                fitnesslistcity.insert(j,initiallist[i])
                break
            else:
                j = j +1

    
def initialpopulation(cityname, initial_list_size, num):
  initialcitylist = [[-1]*(num +1)] * initial_list_size
  i = 0
  initialcity = -1
  while i < initial_list_size:
      route = initialcitylist[i].copy()
      j = 0
      check = cityname.copy()
      initialcity = -1
      while j < num:
        city = random.choice(check)
        if j == 0 :
            initialcity = city
        route[j] = city
        check.remove(city)
        j = j +1
      route[j] = initialcity
      initialcitylist[i] = route
      i = i +1
  return initialcitylist   
def breeding1(fitnesslist,fitnesslistcity,matingpoolsize,matingpool,bestofgeneration,nextgeneration):
    probability_to_breed = chance_of_breeding(fitnesslistcity,matingpool)
    i = 0
    a = 0
    while i < len(fitnesslist) - len(bestofgeneration):
        current_generation = matingpool
        parent1 = random.choice(current_generation)
        index = current_generation.index(parent1)
        current_generation.remove(parent1)
        parent2 = random.choice(current_generation)
        child =['']* len(parent2)
        current_generation.insert(index,parent1)
        pb_parent1 = probability_to_breed[matingpool.index(parent1)]
        pb_parent2 = probability_to_breed[matingpool.index(parent2)]
        if pb_parent1 + pb_parent2 >= 0.84:
            j = 0
            while j < len(parent1)-1:
                b= random.randint(0,1)
                if b >= 0.5:
                    child[j] = parent1[j]
                j = j +1
            if(child[0] == ''):
                j = 0
            else:
                j = 1
            while j < len(parent2)-1:
                if child[j] == '':
                    child[j] = parent2[j]
                j = j + 1
            child[len(parent2)-1] = child[0]
            test1 = parent2[0:len(parent2)-1]
            test2 = child.copy()
            repeatingpositions = [-1] * len(parent2)
            k = 0
            j = 0
            while j < len(child)-1:
                character_to_be_checked = child[j]
                if character_to_be_checked in test1:
                    index_of_checked_character = test1.index(character_to_be_checked)
                    test1.pop(index_of_checked_character)
                else:   
                    repeatingpositions[k] = j
                    k = k +1
                j = j +1
            j = 0
            while repeatingpositions[j] != -1:
                position_of_repeating_in_child = repeatingpositions[j]
                child[position_of_repeating_in_child] = test1[j]
                j = j +1
            nextgeneration[i] = child
            i = i +1
""" def breeding2(fitnesslist,fitnesslistcity,matingpoolsize,matingpool,bestofgeneration,next_generation):
    probability_to_breed = chance_of_breeding(fitnesslistcity,matingpool)
    i = 0
    a = 0
    while i < len(fitnesslist) - len(bestofgeneration):
        current_generation = matingpool
        parent1 = random.choice(current_generation)
        index = current_generation.index(parent1)
        current_generation.remove(parent1)
        parent2 = random.choice(current_generation)
        child1 =['']* len(parent2)
        child2 = [''] * len(parent2)
        current_generation.insert(index,parent1)
        pb_parent1 = probability_to_breed[matingpool.index(parent1)]
        pb_parent2 = probability_to_breed[matingpool.index(parent2)]
        if pb_parent1 + pb_parent2 >= 0.84:
            index1 = random.randint(0,len(parent1)-2)
            index2 = random.randint(0, len(parent2)-2)
            startindex = -1  
            endindex = -1
            if(index1>=index2):
                startindex = index2
                endindex = index1
            else:
                startindex = index1
                endindex = index2
            Dict_parent1 = {}
            Dict_parent2 = {}
            j = startindex
            while j <= endindex:
                Dict_parent1[parent2[j]] = parent1[j]
                Dict_parent2[parent1[j]] = parent2[j]
                j = j + 1 
            subtstring1 = parent1[startindex:endindex+1]
            substring2 = parent2[startindex:endindex+1]
            j = 0
            k = startindex
            while j < len(subtstring1):
                child1[k] = substring2[j]
                child2[k] = subtstring1[j]
                k= k + 1
                j = j +1
            j = 0
            while j < startindex:
                child1[j] = parent1[j]
                child2[j] = parent2[j]
                j = j + 1
            j = endindex + 1
            while j < len(parent2):
                child1[j] = parent1[j]
                child2[j] = parent2[j]
                j = j + 1
            child1[len(child1)-1] = child1[0]
            child2[len(child2)-1] = child2[0]
            j = 1
            while j < startindex:
                character_of_child1 = child1[j]
                while character_of_child1 in substring2:
                    character_of_child1 = Dict_parent1[character_of_child1]
                child1[j] = character_of_child1
                character_of_child2 = child2[j]
                while character_of_child2 in subtstring1:
                    character_of_child2 = Dict_parent2[character_of_child2]
                child2[j] = character_of_child2
                j = j +1
            j = startindex + 1
            while j < len(child1) - 1:
                character_of_child1 = child1[j]
                while character_of_child1 in substring2:
                    character_of_child1 = Dict_parent1[character_of_child1]
                child1[j] = character_of_child1
                character_of_child2 = child2[j]
                while character_of_child2 in subtstring1:
                    character_of_child2 = Dict_parent2[character_of_child2]
                child2[j] = character_of_child2
                j = j +1
            j = startindex + 1

            next_generation[i] = child1
            next_generation[i+1] = child2
            i = i + 2
    return next_generation
 """
def probability_to_mutate(childfitnesslist,childfitnesslistcity):
    total_fitness = totalsum(childfitnesslist)
    avg_fitness = total_fitness/len(childfitnesslist)
    dict_for_mutate = [-1] * len(childfitnesslist)
    i = 0
    for fitness in childfitnesslist:
        if fitness < avg_fitness:
            dict_for_mutate[i] = 0.8
        else:
            dict_for_mutate[i] = 0.2
        i = i +1
    return dict_for_mutate


def initialpopulation2(cityname,initial_list_size, num,Matrix_of_distance):
  initialcitylist = [[-1]*(num +1)] * initial_list_size
  i = 0
  initialcity = -1
  copy_of_original = Matrix_of_distance.copy()
  visited = []
  already_created = []
  number_of_times_created = {}
  while i < initial_list_size:
      route = initialcitylist[i].copy()
      j = 1
      check = cityname.copy()
      initialcity = random.choice(check)
      route[0] = initialcity
      city = initialcity
      visited.append(city)
      if city not in already_created:
        while j < num:
          neighbours = copy_of_original[city].copy()
          neighbours[city] = 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
          shortest_distance = min(neighbours)
          index_of_city = neighbours.index(shortest_distance)
          if index_of_city not in visited:
            route[j] = index_of_city
            city = index_of_city
            visited.append(index_of_city)
          else:      
                while city in visited:
                  neighbours[index_of_city] = 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
                  shortest_distance = min(neighbours)
                  index_of_city = neighbours.index(shortest_distance)
                  city = index_of_city
                route[j] = city
                visited.append(city)              
          j = j +1          
        route[j] = route[0]
        initialcitylist[i] = route
        visited = []
        i = i +1
        already_created.append(route[0])
      else:
          if city not in number_of_times_created:
              number_of_times_created[city] = 1
          else:
              number_of_times_created[city] = number_of_times_created[city] + 1
          neighbours = copy_of_original[city].copy()
          positon_to_be_placed = int((number_of_times_created[city]/num)+1)
          a = 1
          while a <positon_to_be_placed:
              shortest_distance = min(neighbours)
              index_of_city = neighbours.index(shortest_distance)
              if index_of_city not in visited:
                route[a] = index_of_city
                city = index_of_city
                visited.append(index_of_city)
              else:      
                while city in visited:
                  neighbours[index_of_city] = 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
                  shortest_distance = min(neighbours)
                  index_of_city = neighbours.index(shortest_distance)
                  city = index_of_city
                route[a] = city
                visited.append(city)              
              a = a +1
          neighbours = copy_of_original[route[a-1]].copy()
          neighbours[route[a-1]] = 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
          neighbours_copy = copy_of_original[route[a-1]].copy()
          neighbours_copy[route[a-1]] = 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
          neighbours.sort()
          city_tobe_added = number_of_times_created[route[0]] % (num-1)
          if city_tobe_added == num - 1:
              city_tobe_added = 0
           
          value_selected = neighbours[city_tobe_added]
          city_selected = neighbours_copy.index(value_selected)
          while city_selected in visited:
              
              if city_tobe_added >= len(neighbours):
                  break 
              value_selected = neighbours[city_tobe_added]
              city_selected = neighbours_copy.index(value_selected)
              city_tobe_added = city_tobe_added + 1
          if city_tobe_added == len(neighbours):
              for m in neighbours:
                  chosen = neighbours_copy.index(m)
                  if chosen not in visited:
                      city_selected = chosen
                      break   
          route[a] = city_selected
          a = a + 1
          visited.append(city_selected)
          current_city = route[a-1]
          while a < len(route) - 1:
              neighbours = copy_of_original[current_city].copy()
              neighbours[current_city] = 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
              shortest_distance = min(neighbours)
              index_of_city = neighbours.index(shortest_distance)
              if index_of_city not in visited:
                route[a] = index_of_city
                current_city = index_of_city
                visited.append(index_of_city)
              else:      
                while current_city in visited:
                  neighbours[index_of_city] = 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
                  shortest_distance = min(neighbours)
                  index_of_city = neighbours.index(shortest_distance)
                  current_city = index_of_city
                route[a] = current_city
                visited.append(current_city)              
              a = a +1
          route[a] = route[0]
          initialcitylist[i] = route
          visited = []
          i = i +1
              

              


           

  return initialcitylist



def initialpopulation1(cityname,initial_list_size, num,Matrix_of_distance):
  initialcitylist = [[-1]*(num +1)] * initial_list_size
  i = 0
  initialcity = -1
  copy_of_original = Matrix_of_distance.copy()
  visited = []
  while i < initial_list_size:
      route = initialcitylist[i].copy()
      j = 1
      check = cityname.copy()
      initialcity = random.choice(check)
      route[0] = initialcity
      city = initialcity
      visited.append(city)
      while j < num:
          neighbours = copy_of_original[city].copy()
          neighbours[city] = 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
          shortest_distance = min(neighbours)
          index_of_city = neighbours.index(shortest_distance)
          if index_of_city not in visited:
            route[j] = index_of_city
            city = index_of_city
            visited.append(index_of_city)
          else:      
                while city in visited:
                  neighbours[index_of_city] = 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
                  shortest_distance = min(neighbours)
                  index_of_city = neighbours.index(shortest_distance)
                  city = index_of_city
                route[j] = city
                visited.append(city)              
          j = j +1          
      route[j] = route[0]
      initialcitylist[i] = route
      visited = []
      i = i +1
  return initialcitylist
def selection1(fitnesslist,fitnesslistcity,matingpoolsize):
    total_fitness = totalsum(fitnesslist)
    point_distance = total_fitness/matingpoolsize
    start_point = random.uniform(0,point_distance)
    points = [start_point + i * point_distance for i in range(matingpoolsize)]
    mating_pool = []
    i = 0
    
    for p in points:
        sum = 0
        j = 0
        while sum < p :
            sum = fitnesslist[j] + sum
            j = j +1
        
        mating_pool.append(fitnesslistcity[j-1])
    return mating_pool



def main():
    f = open("input.txt","r")
    num = int(f.readline())
    if num == 0:
        f.close()
        f = open("output.txt","w")
        f.write("0")
        f.close()
    elif num == 1:
        city = f.readline()
        f.close()
        f = open("output.txt","w")
        to_Write = '0'+'\n'+city+'\n'+city
        f.write(to_Write)
        f.close()
    else:
        Matrix = [[0] * 3 for i in range(num)]
        cityname = [None] * num
        j = -1
        for i in range(len(Matrix)):
            line = f.readline()
            cord = line.split()
            Matrix[i][0] = float(cord[0])
            Matrix[i][1] = float(cord[1])
            Matrix[i][2] = float(cord[2])
            cityname[i] = i
            j = i 
        f.close()
        initial_list_size = 100
        Matrix_of_distance = distance_between_cities(Matrix,num)
        if num >= 100:
            intitiallist = initialpopulation1(cityname,initial_list_size, num,Matrix_of_distance)
        else:
            intitiallist = initialpopulation1(cityname,initial_list_size, num,Matrix_of_distance)
        initialist1 = intitiallist
        Dict = {}
        fitnesslist = [-1] 
        fitnesslistcity = [""]
        i = 0 
        j = 0
        while i < 2300:
            fitnesslist = [-1]
            fitnesslistcity = [""]
            fitnessppopulation(fitnesslist,fitnesslistcity,initialist1,Dict,Matrix_of_distance)
            if fitnesslist[len(fitnesslist)-1] == -1:
                fitnesslist.pop()
            if fitnesslistcity[len(fitnesslistcity)-1] == "":
                fitnesslistcity.pop() 
            matingpoolsize = 30
            matingpool = selection1(fitnesslist,fitnesslistcity,matingpoolsize)
            besofgeneration = selectbest(matingpool,fitnesslist,fitnesslistcity)
            matingpool = matingpool + besofgeneration
            next_generation = [''] * (len(intitiallist) - len(besofgeneration))
            next_generation = next_generation + besofgeneration
            breeding(fitnesslist,fitnesslistcity,matingpoolsize,matingpool,besofgeneration,next_generation)
        #ask what to do if size of next generation
            next_generation = [j for j in next_generation if j != '']
            childfitnesslist = [-1]
            childfitnesslistcity = [""]
            fitnessppopulation(childfitnesslist,childfitnesslistcity,next_generation,Dict,Matrix_of_distance)
            if childfitnesslist[len(childfitnesslist)-1] == -1:
                childfitnesslist.pop()
            if childfitnesslistcity[len(childfitnesslistcity)-1] == "":
                childfitnesslistcity.pop() 
            Chance_to_mutate = probability_to_mutate(childfitnesslist,childfitnesslistcity)
            mutate1(next_generation,Chance_to_mutate,childfitnesslist,childfitnesslistcity)
           # mutate(next_generation)
            initialist1 = next_generation
            i = i +1
        max_fitness_value = max(fitnesslist)
        max_fitness_index = fitnesslist.index(max_fitness_value)
        best_path_city = fitnesslistcity[max_fitness_index]
        #make a condition to check if the output.txt exists, if not then create
        f = open("output.txt","w")
        #make a big string with all coordinates and distance travelled and call write once
        i = 0
        to_write =""
        distance_travelled = 1/max_fitness_value
        distance_travelled = str(distance_travelled)
        to_write = to_write + distance_travelled +"\n"
        while i < len(best_path_city):
            city = best_path_city[i]
            city = int(city)
            to_write = to_write + str(int(Matrix[city][0])) + " " + str(int(Matrix[city][1])) + " " + str(int(Matrix[city][2]))+ '\n'
            i = i +1
        f.write(to_write)
        f.close()

if __name__ == "__main__":
    main()


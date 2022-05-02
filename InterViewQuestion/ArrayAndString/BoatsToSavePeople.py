# Explanation - Boats to save people - Medium

# People : people array, indes is people's index , value is people's weight .
# Limit : the limit of boats max weight cap.

# People : [1,2]
# Limit : 3 
# Answer : 1

# People : [3,2,2,1]
# Limit : 3 
# Answer : 3

# Weight Limit : 
# 1. No weight more than boat's limit
# 2. No weight less than 0 


'''
# Example 

numRescueBoats(people,limit){

    # from lighter weight to heavy weight
    people.sort()
    
    # Argument
    heavyP = people.length-1
    lightP = 0
    boats = 0

    # Cauluate
    while(heavyP>=lightP){
        if(people[heavyP]+people[lightP] <= limit){
            # heavy and light one boats
            boats+=1
            heavyP-=1
            lightP+=1
        }else{
            #  heavy one boats
            boats+=1
            heavyP-=1
        }
    }
    # return answer
    return boats
}

'''


from typing import List

def boatsCal(peopleArr:List[int],limit:int) -> int:

    # peopleArr : people arr with people num and weight.
    # limit : the limit of boat.

    # from lighter weight to heavy weight
    peopleArr.sort()

    # Argument
    heavyP = len(peopleArr) -1
    lightP = 0
    boats = 0

    # Cauluate
    while(heavyP>=lightP):
        if peopleArr[heavyP] + peopleArr[lightP] <= limit:
            # heavy and light one boats
            boats+=1
            heavyP-=1
            lightP+=1
        else:
            #  heavy one boats
            boats+=1
            heavyP-=1

    return boats

if __name__ == '__main__':

    arr = [1,2,3,2]
    limit = 3
    ans = boatsCal(arr,limit)
    print(ans)
from src.calander.utils import timer, read_input
import heapq

def get_sums(input):
    all_sums=[]
    #print (sql_code)
    all_calories = input.split("\n\n")
    for i in range (len(all_calories)):
        all_calories[i] = [int(x) for x in all_calories[i].split()]
        all_sums.append(sum(all_calories[i]))
    print (max((all_sums)))
    return all_sums  
         

@timer        
def main():
    day_number=1
    calories = read_input(day_number)
    calories_sums = get_sums(input=calories)
    max_sum = (max(calories_sums))
    print (f"Part 1:")
    print (f"Highest sum is {max_sum}")
    print (f"Part 2:")
    print (f"Total of the three highest sums are {sum(heapq.nlargest(3, calories_sums))}")
    


if __name__ == '__main__':
    main()
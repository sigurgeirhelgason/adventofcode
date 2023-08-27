import time

def read_input(day_number, input_type=None):
    if int(day_number) < 10:
        day_number = f"0{day_number}"
    if input_type == "txt":
        with open(f"src/inputs/{str(day_number)}/input.txt") as f:
            inputs = f.read()
    else:   
        with open(f"src/inputs/{str(day_number)}/input.sql") as f:
            inputs = f.read()
    
    return inputs
 
def timer(func):
     def wrapper(*args, **kwargs):
         start_time = time.time()
         result = func(*args, **kwargs)
         end_time = time.time()
         print (f"Execution time: {(end_time - start_time):.4f} seconds")
         return result
     return wrapper
 
def print_results(answer_part_1, answer_part_2=None):
    print(f"The answer for part one: {answer_part_1}")
    if answer_part_2:
        print(f"The answer for part two: {answer_part_2}")
    
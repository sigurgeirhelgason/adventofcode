import time

def read_input(day_number):
    if int(day_number) < 10:
        day_number = f"0{day_number}"
        
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
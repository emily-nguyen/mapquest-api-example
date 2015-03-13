# Project 3: MapQuest API Example

def main():
    inputs = int(input())
    location_list = input_list(inputs)
    outputs = int(input())
    output_list = input_list(outputs)

def input_list(n:int)->list:
    '''Returns a list of n locations taken in as input'''
    result = []
    for i in range(n):
        x = input()
        result.append(x)
    return result 
        
if __name__ == '__main__':
    main() 

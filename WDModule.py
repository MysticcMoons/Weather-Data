# Julia Shannon
import random
import numpy as np



# Task 1: Merge Sort
# Start random seed generator
random.seed(10)
# List of numbers to test
nums = []
# use a while loop to generate a list of 10 random numbers between -20 and 20
while len(nums) != 10:
    nums.append(np.random.randint(-20,20))



def mergeSort(array):
    # Check if it has 0 or 1 element, if it does, it was already sorted
    if len(array) <= 1:
        return array
    # Get the moddle index by dividing the array in half
    middle = len(array) // 2
    # Call the merge sort function to check left and right
    left = mergeSort(array[:middle])
    right = mergeSort(array[middle:])
    # Call merge function to put array back together
    return merge(left, right)


def merge(left, right):
    result = []
    # i for left, j for the right
    i = j = 0
    # compare lengths and pick the smaller one
    while i< len(left) and j< len(right):
        # if the left value at index i is smaller, add it to result
        if left[i] <= right[j]:
            result.append(left[i])
            i+=1
        # if the right was smaller, add the right to result
        else:
            result.append(right[j])
            j+=1
    # Add any remaining values by slicing
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# Task 2: Module and Functions
# Create a dictionary for all of the values, (Key = Month, Value = rainfall (in))
rainDictionary = {1: 133.5, 2: 64.3, 3: 104.4, 4: 86.3, 5: 48.5, 6: 35.4, 7: 55.3, 8: 84.9, 9: 104.5, 10: 104.4, 11: 122.6, 12: 119.5}


def max_Precipitation(rainDictionary):
    # make the first key the first month from the dictionary, but turn it into a list so its easier to grab
    first_key = list(rainDictionary.keys())[0]
    # this makes the max month the first key so it can now be compared
    max_Month = first_key

    # its saying take the month and get me the amount from rain dictionary
    for month, amount in rainDictionary.items():
    # if the amount of precipitation of this month is greater than the precipitation in max month, make it the max month
        if amount > rainDictionary[max_Month]:
            max_Month = month
    return max_Month, rainDictionary[max_Month]

def min_Precipitation(rainDictionary):
    # make key one the first month from the dictionary, but turn it into a list so its easier to grab
    key_one = list(rainDictionary.keys()) [0]
    min_Month = key_one

    # its saying take the month and get me the amount from rain dictionary
    for month, amount in rainDictionary.items():
    # if the amount of precipitation of this month is less than the precipitation in max month, make it the min month
        if amount < rainDictionary[min_Month]:
            min_Month = month
    return min_Month, rainDictionary[min_Month]


def average_Precipitation(rainDictionary):
    # set the total to 0
    total = 0
    
    # loop through the months and values, add each amount each time
    for month, amount in rainDictionary.items():
        total+=amount

    # take the average 
    average = total/len(rainDictionary)
    return average



def above_Mean(rainDictionary):
    # make key one the first month from the dictionary, but turn it into a list so its easier to grab
    k1= list(rainDictionary.keys()) [0]
    # male an empty list for the months above the mean
    months_above = []
    for month, amount in rainDictionary.items():
    # if the amount of precipitation for this month is greater than the average add it to months_above
        if amount > average_Precipitation(rainDictionary):
            months_above.append(month)
    return months_above

# Month names so I can represent the numbers as words instead so it is easier for the user to read
month_names = {1: "January", 2: "February", 3: "March", 4 :"April", 5: "May", 6: "June", 7: "July",
                8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}

def names_in_decending_order(rainDictionary, month_names):
    # empty list of sorted names
    sorted_namse = []
    rain_list = list(rainDictionary.items())
    # get the length of the loop range
    n = len(rain_list)
    # Bubble sort, compare the adjacent rainfall amounts to sort it in decending order from 
    # most precipitation to least precipitation
    for i in range(n):
        for j in range(n - i - 1):
            if rain_list[j][1] < rain_list[j+1][1]:
                rain_list[j], rain_list[j + 1] = rain_list[j + 1], rain_list[j]
    # sorts the numbers to their names to make it easier for the user
    for month_num, amount in rain_list:
        name = month_names[month_num]
        sorted_namse.append(name)
    return sorted_namse















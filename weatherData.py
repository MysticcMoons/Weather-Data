# Julia Shannon
import WDModule as myMod

print('-' * 55)
print('Weather Data  |  Julia Shannon')
print('-' * 55)
print('Task 1: Merge Sort')

# Task 1: Merge Sort
# Print sorted array
print(f"Sorted Array: {myMod.mergeSort(myMod.nums)}")


print('-' * 55)
print('Task 2: Module and Functions')

# Task 2: Module and Functions
# Print max and min
# made max_in and min_in so they can be multiplied by 2.54 for cm easily
myMod.max_Month, max_in = myMod.max_Precipitation(myMod.rainDictionary)
myMod.min_Month, min_in = myMod.min_Precipitation(myMod.rainDictionary)

print(f"Max: {myMod.month_names[myMod.max_Month]} | {max_in * 2.54:.2f}cm")
print(f"Min: {myMod.month_names[myMod.min_Month]}    | {min_in * 2.54:.2f}cm")
print('-' * 35)

# print average precipitation, made avg_in so i can multiply it by 2.54 easily for cm
avg_in = myMod.average_Precipitation(myMod.rainDictionary)
print(f"Average Precipitation: {avg_in * 2.54:.2f}cm")
print('-' * 35)

# print above mean months, above_months takes the number and makes it the word so its easier to read, 
# len(above_months) to say how many months are above the mean
above_months = [myMod.month_names[m] for m in myMod.above_Mean(myMod.rainDictionary)]
print(f"Months Above the Mean: {len(above_months)} Months  |  {above_months}")
print('-' * 110)

# print the names in decneding order from most to least rainfall
print(f"Sorted names from decending order:{myMod.names_in_decending_order(myMod.rainDictionary, myMod.month_names)}")
print('-' * 160)
import sys

class questions():

	# find the median of 2 sorted arrays
	def medianOfArrays(self):
		arr1 = [1,2,3]
		arr2 = [4,5,6]
		arr3 = arr1 + arr2
		# check to see if even
		if(len(arr3)%2 == 0):
			print((arr3[int(len(arr3)/2)]+arr3[(int(len(arr3)/2))-1])/2)
		else:
			print(arr3[int(len(arr3)/2)])

	# given an array, find duplicates that 
	def findDuplicated(self):
		arr=[2,4,5,6,7,2]
		dict = {}
		for i in range(0, len(arr)):
			if arr[i] in dict:
				dict[arr[i]] = dict[arr[1]] + 1
			else:
				dict[arr[i]] = 0

		# counter = 0
		# for i in range(0, len(dict.values())):
		# 	if int(dict.get(i)) > counter:
		# 		counter = dict.get(i)
		# 	elif int(dict.get(i)) == counter:
		# 		print("collision")
		# 	else:
		# 		print("")

		print(dict)


print("Welcome to 50 Interview Questions")
print("here is the implemented list of questions:")
print("_________________________________")
print("1. Median of Arrays")
print("2. 0-1 Knapsack")
print("3. Matrix Product")
print("4. Find Duplicates")
print("5. Consecutive Array")
print("6. Zero Matrix")
print("7. Square Submatrix")
print("8. Merge K Arrays")
print("9. Matrix Search")
print("10.Merge Arrays")
print("11.Zero Sum Subarray")
print("12.Permutations")
print("13.N Stacks")
print("14.Anagrams")
print("15.Build Order")
print("16.Shortest Path")
print("17.Random Binary Tree")
print("18.Lowest Common Ancestor")
print("19.Sum")
print("20.Reverse Stack")
print("21.Tree to Doubly Linked List")
print("22.Longest Consecutive Branch")
print("23.Print Reversed Linked List")
print("24.Balanced Binary Tree")
print("25.Binary Search Tree Verification")
print("26.Smallest Change")
print("27.Inorder Traversal")
print("28.Sort Stacks")
print("29.Stacks from Queues")
print("30.Palindromes")
print("31.Max Stacks")
print("32.Two Missing Numbers")
print("33.Big Int Modules")
print("34.Swap Variables")
print("35.Gray Code")
print("36.Rotate Bits")
print("37.Number of Ones In a Binary Number")
print("38.Linked List Cycles")
print("39.Random Linked List")
print("40.Dedup Linked List")
print("41.Split a Linked List")
print("42.Nth to the Last Element")
print("43.Three Sum")
print("44.Tree Level Order")
print("45.Autocomplete")
print("46.String Deletion")
print("47.Longest Common Substring")
print("48.String Compression")
print("49.Fibonacci Number")
print("50.Priority Queue")
print("51.Kth Most Frequent String")
print("_________________________________")

probNumber = ""
while(probNumber != "0"):
	q = questions()
	probNumber = input("Enter Problem Number: ")

	if(probNumber == "1"):
		q.medianOfArrays()
	elif(probNumber == "4"):
		q.findDuplicated()


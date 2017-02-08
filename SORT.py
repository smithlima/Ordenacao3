import sys


def countSort(list1):
	maximum= max(list1)
	minimum = min(0, min(list1))
	count= [0]*(maximum-minimum+1)

	for i in list1:
		count[i]+=1

	sort_list1=[]
	for i in range(minimum, maximum+1):
		if count[i] > 0:
			for j in range(0,count[i]):
				sort_list1.append(i)
			
	return sort_list1
	

########################################################################
def map(x, in_min, in_max, out_min, out_max):
	return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)
#########################################################################
def bucketSort(list):
	n = len(list)
	max_v = max(list)
	min_v = min(list)
	bucket_range = 1000
	bucket = [[]]* n

	for x in xrange(n):
		
		index = int(map(list[x], min_v, max_v, 0, n-1))
		bucket[index] = bucket[index] + [list[x]]

	for x in xrange(n):
		bucket[x].sort()
	list = []
	for i in xrange(n):
		for j in bucket[i]:
			list.append(j)
	return list
    
########################################################################
def radixSort(list1):
    len_random_list = len(list1)
    modulus = 10
    div = 1
    while True:
        
        new_list = [[], [], [], [], [], [], [], [], [], []]
        for value in list1:
            least_digit = value % modulus
            least_digit /= div
            new_list[least_digit].append(value)
        modulus = modulus * 10
        div = div * 10

        if len(new_list[0]) == len_random_list:
            return new_list[0]

        list1 = []
        rd_list_append = list1.append
        for x in new_list:
            for y in x:
                rd_list_append(y)
########################################################################
def main(argv):
	#print(argv)
	
	size = int(input())
	list1 =[]
	for i in range(size):
		list1.append(int(input()))

	#print(list1)	

	if argv[1]=="1":
		#print("Counting SORT \n")
		
		sort_list1 =countSort(list1)
		print(sort_list1)
	if argv[1]=="2":
		#print("SELECTION SORT \n")
		new_list =bucketSort(list1)
		print(new_list)
	if argv[1]=="3":
		#print("Counting SORT \n")
		radixSort1 = radixSort(list1)
		print(radixSort1)
		
	else:
		#return (print("Valor invalido"))
		pass
	

	
if __name__ == "__main__":

	main(sys.argv)


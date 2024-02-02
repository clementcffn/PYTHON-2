#Exercises - Advanced Syntax - Q.ipynb#

#Exercice 1 
def reverse_string(string1):
    N = len(string1)
    for i in range (N-1, -1, -1):
        yield string1[i]
    
my_generator = reverse_string("Clément")
"".join(my_generator)


#Exercice 2
input_string="SKEMA Business School"

filtered_list = list(filter(lambda x : True if x.lower() in "aeiouy" else False, input_string))
filtered_list

#Exercice 3
list_numbers=[1000,2000,5000,10000,20000]

filtered_list = map(lambda x: x + 2000, filter(lambda x: x < 8000,list_numbers))
print(list(filtered_list))

#Exercice 5
list1 = [1,2,3]
list2 = ['A','B','C']

list3 = list(zip(list1,list2))
my_dict = dict(list3)
print(my_dict)

#Exercice 6
def PutNumbers(n):
    for i in range(n):
        if i%7==0:
            yield i

for x in PutNumbers(100):
    print(x)
    
  

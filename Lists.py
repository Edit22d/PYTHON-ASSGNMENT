# Lists are  mutable, it also  works with index
#items  stored should be the same
StudentName = ['sandra','patricia','Phionah','Anitah']#string
StudentMark = [80,56,78,90]
data =['Sandra',90,'Kamwokya']#mixed
#Access the whole list
print(data,type(data))


#Accessing the whole list
# indexes (positive indexes)
#These are arroys and we use index
print(StudentName [0])#first item
print(StudentName [1])#second item
print(StudentName [2])#third item
print(StudentName [3])#forth item

# indexes (negative indexes)
print(StudentName [-4])#first item
print(StudentName [-3])#second item
print(StudentName [-2])#third item
print(StudentName [-1])#forth 

#adding new item to the list
StudentName.append('Edith')
print(StudentName)
StudentName.remove('patricia')
print(StudentName)

# #At a particular position 
StudentName.insert(1,'faith')
print(StudentName)
# Test 2
# functions 
# lists
# For loops
# Dictionary

# print patricia,Faith and anitah(silicing)
# add mash at the forth position
# update the name phionah to'phionah aladinah'
# Display the length of the student list
# print all the student names using a for loop
# calculate the  total mark for the student mark variable and the answer should be (304)

# answers
#a)
StudentName = ['Patricia','Faith','Anitah']
print(StudentName[0:3])

#b)
StudentName.insert(4,'mash')
print(StudentName)

#c)
StudentName = ['Patricia','Faith','Anitah','phionah']
StudentName [3] = 'phionah Aladinah'
print(StudentName)
# updated_name = StudentName.replace['phiona','phionah Aladinah']
# print(updated_name)

#d)
StudentName = ['Patricia','Faith','Anitah','phionah Aladinah']
for student in StudentName:
    print(f'The lenght of {student} is {len(StudentName)}')
#or
StudentName = ['Patricia','Faith','Anitah','phionah Aladinah']
lenghts = [len(student) for student in student]
print(lenghts)

#e)
StudentName = ['Patricia','Faith','Anitah','phionah Aladinah']
for student in StudentName:
    print(StudentName)
#OR
StudentName = ['Patricia','Faith','Anitah','phionah Aladinah']
print(StudentName[::])

#F)
StudentMark = [80,56,78,90]
TotalMark = sum (StudentMark)
print(f'The TotalMark for the students is: {TotalMark}')


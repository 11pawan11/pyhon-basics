# # a=[1,2,3,4,5]
# # len(a)
# # for i in a


# a='rat cat and rat were playing in the mat and the cat was happy with rat on the mat'
# print len(a)
# print ("sentence occur",a.count('mat'))1
# count=0
# for i in a:
#     count=count+1
# print (count,'>',i)



# a='hell make the'
# count=0
# for char in a:
#     count+=1
#     if (char=='h'):
#         print(count,'found')
#     else:
#         print('donot contain')  
# char=0
# for char in a:
#     if char == 'h' :
#          print("P Found " , char) 
#     else:
#         pass



# a=0
# while a <=100:
#     if (a%2==0):
#         print('even',a)
    
        
#     else:
#         print('odd',a)
#     a=a+1




# # while loop process
# while True:
#     a=raw_input("Enter a name :")
#     if (a=='y'):
#         print 'loop end'
#         break
#     else:
#         print 'name entered'





#function

# def add(x=0,y=10,z=6):
#         return x+y+z
# print 'add is',add()

# def new (z,y,*args):
#     print(len(args))
#     if len(args)>0:
#         total=0
#         for i in args:
#             total=total+i
#         sum=total+z+y
#     else:
#         sum=z+y
# new(10,20)    
# print ('again')
# new(10,20,30,40)


#list

# mixedList_0 = [1,2,3,4,56.7,34.6,"the",'python']
# # if 'a' in mixedList_0:
# #     print 'tu'
# # else:
# #     print 'fal'
# print len(mixedList_0[-1])


# sentence = ["the cat sat on the mat and the cat was playing with rat on the mat"]
# print sentence
# print sentence.reverse()
# print set(sentence)

# mixedList= [1,2,3,4,56.7,34.6,"the",'python']
# tuple_t = (10,20,30,40,55,66,99)
# mixedList.extend(tuple_t)
# print("\n Extended with Tuple : ",mixedList)





# dict_a = {"Nepal":"Kathmandu" ,"Japan":"Tokyo","m":"n"}
# dict_b = {"China":"Beijing", "Russia":"Moscow",'x':'y'}


# print(dict_a.keys())
# print(list(dict_a.keys()))#casting
# #values
# print(dict_b.values())
# print(list(dict_b.values()))#casting
# #merging Kes and Values
# print(list(zip(dict_a.keys(),dict_b.values())))
# print(dict(list(zip(dict_a.keys(),dict_b.values()))))







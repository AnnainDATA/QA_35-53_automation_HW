print('--------------Exercise 1-------------')
def print_list_reverse(lst):
    if lst is None or lst==[] or type(lst)!=list:
        print("Wrong list")
    else:
            print(lst[::-1])
print_list_reverse([1,2,3,4,5])
print_list_reverse([])
print_list_reverse((1,2,3,4,5))
print_list_reverse(None)

print('--------------Exercise 1A-------------')
def print_list_reverse(lst):
    if lst is None or lst==[] or type(lst)!=list:
        print("Wrong list")
    else:
        lst1=[]
        for num in reversed(lst):
            lst1=lst1+list([num])
        print(lst1,end="")
        print()
print_list_reverse([1,2,3,4,5])
print_list_reverse([])
print_list_reverse((1,2,3,4,5))
print_list_reverse(None)

print('--------------Exercise 2-------------')
def is_valid_point(point):
    if point is None or point==():
        return None
    if (type(point)!=tuple or len(point)!=2 or not isinstance(point[0],(float,int))
            or not isinstance(point[1],(float,int))):
        return False
    else:
        return True
res=is_valid_point((3, 5))
res1=is_valid_point((3, "5"))
res2=is_valid_point([3, 5])
res3=is_valid_point((1, 2, 3))
res4=is_valid_point(())
res5=is_valid_point(None)
print(res,res1,res2,res3,res4,res5)

print('--------------Exercise 3-------------')
def print_sublist_reverse(lst,start,finish):
    if lst is None or lst==[] or type(lst)!=list or not isinstance(start,int) or not isinstance(finish,int) or start>finish or start>len(lst)-1 or finish>len(lst)-1:
        print("Wrong args")
    else:
        lst_left=lst[:start]
        lst_right=lst[finish+1:]
        s_middle = lst[start:finish + 1][::-1]
        print(lst_left+s_middle+lst_right)

print_sublist_reverse([10,20,30,40,50,60],1,3)
print_sublist_reverse([1, 2, 3], "0", 2)
print_sublist_reverse([],1,"A")

print('--------------Exercise 4-------------')
def get_students_by_grade(students):
    if students is None or students=={} or type(students)!=dict:
        return {}
    else:
        students_names = students.keys()
        print(students_names)
        students_mark=students.values()
        print(students_mark)
        mark_names = {mark: name for mark, name in zip(students_mark, students_names)}
        print(mark_names)
get_students_by_grade({"Alice": 90, "Bob": 85, "Diana": 90, "Charlie": 85})




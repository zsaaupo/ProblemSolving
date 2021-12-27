"""
Assingment_1
"""
print(__doc__)


from datetime import date, timedelta


# Find max min between 3 number

class max_value():


    def __init__(self, a, b, c):
        
        self.a = a
        self.b = b
        self.c = c


    def max_number(self):

        try:

            if self.a > self.b and self.a > self.c:
                max_num = self.a
            
            elif self.b > self.a and self.b > self.c:
                max_num = self.b
            
            elif self.c > self.b and self.c > self.a:
                max_num = self.c

            elif self.a == self.b == self.c:
                max_num = self.a
        
        except:

            max_num = "Something is wrong"
        
        return max_num




class min_value():


    def __init__(self, a, b, c):
        
        self.a = a
        self.b = b
        self.c = c


    def min_number(self):

        try:

            if self.a < self.b and self.a < self.c:
                min_num = self.a
            
            elif self.b < self.a and self.b < self.c:
                min_num = self.b
            
            elif self.c < self.b and self.c < self.a:
                min_num = self.c

            elif self.a == self.b == self.c:
                min_num = self.a
        
        except:

            min_num = "Something is wrong"
        
        return min_num




# Sum two number which given by user

class sum_number():


    def __init__(self, a, b):

        self.a = a
        self.b = b


    def sum_num(self):

        try:

            return self.a + self.b

        except:

            return "Sonthing is wrong"




# Print Today, Tomorrow and Yesterday

class get_date():


    def present_day(self):

        return date.today()


    def previous_day(self, p):

        return date.today()-timedelta(days= p)


    def future_day(self, f):

        return date.today()+timedelta(days= f)




# Find the odd even in a list

class odd_even():


    def __init__(self, l):

        self.l = l


    def odd_ev(self):

        l_odd = []
        l_evan = []
        
        try:

            for i in self.l:

                int(i)
                
                if i % 2 == 0:

                    l_evan.append(i)

                else:

                    l_odd.append(i)

            return ("odd number = ", l_odd, "even number = ", l_evan)
   
        except:

            return "somthing is wrong!"

    


# Sum the 3 number using class, function and object

class sum_3_number():


    def __init__(self, a, b, c):

        self.a = a
        self.b = b
        self.c = c


    def sum_num(self):

        try:

            return self.a + self.b + self.c

        except:

            return "Sonthing is wrong"




# To Calculate Sum and Average of N Numbers using For Loop and list

class sum_avg():


    def __init__(self, list_n):

        self.list_n = list_n

    
    def sum_and_avg(self):

        sum = 0
        count = 0

        try:

            for i in self.list_n:

                int(i)

                sum = sum + i
                count = count + 1
            
            return "sum is =", sum, "average is =", sum/count

        except:

            return "somthing is wrong!"




# To Calculate Sum and Average of N Numbers using while Loop and list

class sum_avg_wl():


    def __init__(self, list_2):

        self.list_2 = list_2

    
    def sum_and_avg_wl(self):

        try:

            count = 0
            sum = 0

            while count < len(self.list_2):

                value = int(self.list_2[count])
                sum = sum + value
                count = count + 1

            return "sum is =", sum, "average is =", sum/count

        except:

            return "Sonmthing is wrong"



# Find the highest and average values in a list using classes and functions

class high_avg():


    def __init__(self, list_3):
        
        self.list_3 = list_3

    
    def high_and_avg(self):

        h = 0
        sum = 0
        count = 0

        try:

            for i in self.list_3:

                int(i)

                if h < i:
                    h = i

                sum = sum + i
                count = count + 1
            
            return "highest value =", h, "average is =", sum/count

        except:

            return "somthing is wrong!"




# list_value = [1,5,8,9,15,78,45,68,55,99,66,88,1.3,100.5,48,33,60,"test",22,"exam"] sort the list

class sort_list():


    def __init__(self, list_4):

        self.list_4 = list_4


    def sort_l(self):
    
        for i in self.list_4:

            try:

                int(i)

            except:

                self.list_4.remove(i)

        self.list_4.sort()

        return self.list_4




# Using if else calculate a grading system, Notify him, if user gives wrong number

class grad():


    def __init__(self, m):

        self.m = m

    
    def grading_mark(self):

        try:

            if self.m <= 100 and self.m >= 80:

                return "A+"

            elif self.m <= 79 and self.m >= 75:

                return "A"

            elif self.m <= 74 and self.m >= 70:

                return "A-"

            elif self.m <= 69 and self.m >= 65:

                return "B+"

            elif self.m <= 64 and self.m >= 60:

                return "B"

            elif self.m <= 59 and self.m >= 55:

                return "B-"

            elif self.m <= 54 and self.m >= 50:

                return "C+"

            elif self.m <= 49 and self.m >= 45:

                return "C"

            elif self.m <= 44 and self.m >= 40:

                return "D"

            elif self.m <= 39 and self.m >= 0:

                return "F"

            elif self.m <= -1 or self.m > 100:

                return "This mark is not valid"
        
        except:

            return "somthing is wrong!"




if __name__ == "__main__":

    # obj_max = max_value(7,3,5)
    # print(obj_max.max_number())

    # obj_min = min_value(7,5,3)
    # print(obj_min.min_number())


    # input_1 = input("Give frist number = ")
    # input_2 = input("Give second number = ")

    # try:

    #     input_1 = float(input_1)
    #     input_2 = float(input_2)

    #     obj_sum = sum_number(input_1, input_2)
    #     print("sum is = ","%.2f" % obj_sum.sum_num()) # Q_1 only frist 2 f not calculate

    # except:

    #     print("somthing is wrong..!")


    # obj_date = get_date()
    # print(obj_date.present_day())
    # print(obj_date.previous_day(1))
    # print(obj_date.future_day(1))


    # obj_odd_even = odd_even([1,2,5,4,6,8,4,5])
    # print(obj_odd_even.odd_ev())


    # obj_sum_3_num = sum_3_number(3, 2, 1)
    # print(obj_sum_3_num.sum_num())


    # obj_sum_avg = sum_avg([1,5,9,4,8,6,7])
    # print(obj_sum_avg.sum_and_avg())


    # obj_wl = sum_avg_wl([1,5,9,4,8,6,7])
    # print(obj_wl.sum_and_avg_wl())


    # obj_h_avg = high_avg([1, 2, 3])
    # print(obj_h_avg.high_and_avg())


    # obj_sort = sort_list([1,5,8,9,15,78,45,68,55,99,66,88,1.3,100.5,48,33,60,"test",22,"exam"])
    # print(obj_sort.sort_l())
    

    # input_mark = input("Give the mark = ")

    # try:

    #     input_mark = float(input_mark)

    #     obj_grad = grad(input_mark)
    #     print(obj_grad.grading_mark())

    # except:

    #     print("somthing is wrong..!")


    pass

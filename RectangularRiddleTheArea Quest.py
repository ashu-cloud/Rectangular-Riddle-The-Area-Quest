from random import randint
# we are creating a program that generates random rectangle on the coordinate scale and 
# checks whether the give coordinate lies inside it ot not
# so for that i am first creating two classses for poits and rectangle 
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def In_rectangle(self,rectangle):# checks whether the point lies inside the rectangle or not
        if rectangle.lowleft.x<self.x<rectangle.upright.x and rectangle.lowleft.y<self.y<rectangle.upright.y:
            return True
        else:
            return False
    def distance_from(self,point):
        return ((self.x-point.x)**2+(self.y-point.y)**2)**0.5

     
    ...
class Rectangle:
    def __init__(self,lowleft,upright):
        self.lowleft=lowleft
        self.upright=upright
    def area_rect(self):
        return ((self.upright.x-self.lowleft.x)**2+(self.upright.y-self.lowleft.y)**2)/2


rectangle= Rectangle(Point(randint(0,9),randint(0,9)),Point(randint(10,19),randint(10,19)))
print("The Coordinates of the rectangle are: (", rectangle.lowleft.x,",",rectangle.lowleft.y ,")and(",rectangle.upright.x,",",rectangle.upright.y,")")

user_input= Point(float(input("enter x: ")), float(input(" enter y: ")))
print(user_input.In_rectangle(rectangle))
area=float(rectangle.area_rect())

inte=3
print("You have three chances to geuss the correct area of this rectangle.  good Luckkk!!")

while inte>0:
    area_input= float(input(" guess the area of the rectangle: "))

    if(area_input== area):
        print("you geussed was correct :)")
        inte=0
        break
    if(inte==1):
        print("OOPS......")
        print(" Sorry you have used all of the guess chances :(")
        
        print(f"the area of the rectangle is :{rectangle.area_rect()} sqr units.")
    else:
        print(" you've guess incorrect area. ")
        print(f" you still have {inte-1} chances to guess correct value of the area ")


    inte=inte-1


    

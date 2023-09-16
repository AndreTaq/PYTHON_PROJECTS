def hello():
    print("Hello")


def pack(Tom, Jerry, Bob):
    return [1, 2, 3]
    

def eat_lunch(food_list):
    if len(food_list) == 0:
        print("My lunchbox is empty!")
    else:
        for i in range(len(food_list)):
            if i == 0:
                print(f"First I eat {food_list[0]}")
            else:
                print(f"Next I eat {food_list[i]}")



hello()
print(pack("Tom", "Jerry", "Bob"))
eat_lunch([])
eat_lunch(["wings"])
eat_lunch(["tacos", "pizza", "ice cream"])
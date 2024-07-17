#
# Example file for working with loops
# LinkedIn Learning Python course by Joe Marini
# edited by Juan Rodriguez 07/17/24
#


def main():
    x = 0

    # TODO: define a while loop
    while (x < 5):
        print(x)
        x = x + 1
    print(x)

    # TODO: define a for loop
    for x in range(5,10):
        print(x)

    # TODO: use a for loop over a collection
    days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
    for d in days:
        print(d)


    # TODO: use the break and continue statements


    # TODO: using the enumerate() function to get index 
    
  
if __name__ == "__main__":
    main()

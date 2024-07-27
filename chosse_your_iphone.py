def main(answer):
    if answer =='15':
       print("iphone 15 added to the bag.")
    
    elif answer =="14":
        print("iphone 14 added to the bag")
    
    elif answer =="13":
        print("iphone 13 added to the bag")

    
    elif answer =="12":
        print("iphone 12 added to the bag")
    
    elif answer =="11":
        print("iphone 11 added to the bag")
    
    else:
        print("Chosse again.")

if __name__ == "__main__":
    print("Hello fellow customer!")
    print("Please chosse your iphone serie")
    answer= input("chosse between iphone 11 to iphone 15 ")
    main(answer)
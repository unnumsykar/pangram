# import string library
import string

def main():

    string = input("Enter the string:") # Taking input as a string

    lowercaseString = string.lower()    # Converting the string into lowercase
    lowercaseString = lowercaseString.replace(" ","")   # Removing all the spaces in the string

    stringList = set(lowercaseString)   # Converting string into set

    if len(stringList) == 26:           # Checking if the length of string is 26 or not
        print("This is a pangram string")
    else:
        print("This is not a pangram string")



if __name__=='__main__':
    main()




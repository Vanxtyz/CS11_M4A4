def option1():
    art = """
              .--~~,__
:-....,-------`~~'._.'
 `-,,,  ,_      ;'~U'
  _,-' ,'`-__; '--.
 (_/'~~      ''''(;
"""
    print(art)

def option2():
    art = """
  _._     _,-'""`-._
 (,-.`._,'(       |\\`-/|
     `-.-' \\ )-`( , o o)
           `-    \\`_`"'-
"""
    print(art)

def main():
    print("Would you like to see a dog or cat:")
    print("1. dog")
    print("2. cat")

    choice = input("Enter 1 or 2: ").strip()

    if choice == "1":
        option1()
    elif choice == "2":
        option2()
    else:
        print("Please pick 1 or 2 no other number is supported.")

if __name__ == "__main__":
    main()
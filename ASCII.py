# ASCII Art with Option Selection (fixed)

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
    print("Choose an option:")
    print("1. Image One")
    print("2. Image Two")

    choice = input("Enter 1 or 2: ").strip()

    if choice == "1":
        option1()
    elif choice == "2":
        option2()
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
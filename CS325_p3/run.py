
# Import functions from the three modules
from module1.some_name1 import function_module1
from module2.some_name2 import function_module2
from module3.some_name3 import function_module3

def main():
    # module functions
    result1 = function_module1()
    result2 = function_module2()
    result3 = function_module3()

    # results
    print("Module1:", result1)
    print("Module2:", result2)
    print("Module3:", result3)

if __name__ == "__main__":
    main()

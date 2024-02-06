import argparse

def main():
    parser = argparse.ArgumentParser()
    
    # Using help, dest, and type
    parser.add_argument('--input_str', help='Enter a string', dest='input_str', type=str)
    parser.add_argument('--input_int', help='Enter an integer', dest='input_int', type=int)
    parser.add_argument('--input_float', help='Enter a float', dest='input_float', type=float)
    
    args = parser.parse_args()

    # Accessing variables using dest names
    input_str = args.input_str
    input_int = args.input_int
    input_float = args.input_float

    # Displaying values
    print("String:", input_str)
    print("Int:", input_int)
    print("Float:", input_float)

if __name__ == '__main__':
    main()

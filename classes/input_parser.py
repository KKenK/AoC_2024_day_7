class InputParser():

    def __init__(self, input_path):
        
        input = []

        with open(input_path) as f:
            input = f.read()
        
        self.parsed_input = self._parse_input(input)
    
    def _parse_input(self, input):

        lines = [(int(x[0]), [int(num) for num in x[1].split(" ") if num]) for x in [line.split(":") for line in input.split("\n")]]
        
        return lines

if __name__ == "__main__":

    input_parser = InputParser(r"C:\Users\kylek\Documents\code\Advent_of_code\2024\Day_7\test.txt")

    #print(input_parser.parsed_input)
    print(input_parser.parsed_input)

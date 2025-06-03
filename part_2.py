from classes import input_parser

class Equation():
    
    def __init__(self, line):
        self.target = line[0]
        self.numbers = line[1]

    def calculate_solution(self, operators):

        solution = self.numbers[0]

        i = 0

        if len(self.numbers) < 3:
            return solution
        
        for num_index in range(1, len(self.numbers)):
    
            solution = self._perform_operation(solution, self.numbers[num_index], operators[i])    

            i += 1

        return solution
    
    def _perform_operation(self, a, b, operator):

            if operator == "+":
                return a + b
            
            elif operator == "*":
                return a * b
       
            elif operator == "c":
                return int(str(a) + str(b))
            
    def print_equation_parts(self):
        print(f"Target: {self.target}; Numbers: {self.numbers}")

def operator_combination_calculator(numbers_count):

    if numbers_count == 1 :
        return [""]

    operator_combinations_strings = [combination + recursive_combination_string for recursive_combination_string in operator_combination_calculator(numbers_count - 1)
                    for combination in ["+", "*", "c"]]

    return operator_combinations_strings


parsed_input = input_parser.InputParser(r"C:\Users\kylek\Documents\code\Advent_of_code\2024\Day_7\input.txt").parsed_input

equations = [Equation(line) for line in parsed_input]

total_calibration_result = 0

for equation in equations:
    equation_operator_combinations = operator_combination_calculator(len(equation.numbers))

    for operator_combination in equation_operator_combinations:

        if equation.calculate_solution(operator_combination) != equation.target:
            continue
        
        total_calibration_result += equation.target

        break
        
print(total_calibration_result)
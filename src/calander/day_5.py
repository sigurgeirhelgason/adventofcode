from utils import timer, read_input, print_results
from copy import deepcopy

NUM_SLOTS = 4
NUM_COLUMNS = 3


def split_command_stacks(input_lines):
    split_index = input_lines.index("")
    return input_lines[:split_index], input_lines[split_index + 1 :]


def create_stack_lists(stacks: list) -> list[list]:
    stack_numbers = stacks[-1].split()
    new_stacks = [[] for _ in stack_numbers]

    for stack in stacks:
        for i, char in enumerate(stack):
            if char.isalpha():
                new_stacks[(i - 1) // NUM_SLOTS].append(char)

    for stack in new_stacks:
        stack.reverse()

    return new_stacks


def proceed_single(command: str, stack: list) -> list:
    how_many, from_where, to_where = map(int, filter(str.isdigit, command.split()))

    for _ in range(how_many):
        container_to_move = stack[from_where - 1].pop()
        stack[to_where - 1].append(container_to_move)



def proceed_multi(command: str, stack: list) -> list:
    how_many, from_where, to_where = map(int, filter(str.isdigit, command.split()))
    to_be_moved = stack[from_where - 1][-how_many:]
    stack[to_where - 1].extend(to_be_moved)
    stack[from_where - 1] = stack[from_where - 1][:-how_many]


def print_stacks(stack):
    max_length = max(len(sublist) for sublist in stack)

    for i in reversed(range(max_length)):
        for sublist in stack:
            if i < len(sublist):
                print(f"[{sublist[i]:^}]", end=" ")
            else:
                print("   ", end=" ")
        print()

    for i in range(1, len(stack) + 1):
        print(f"{i:^{NUM_COLUMNS}}", end=" ")


def proceed_commands(commands, stacks, multi=False, debug=False):
    stacks_copy = deepcopy(stacks)
    
    if multi:
        for command in commands:
            proceed_multi(command, stacks_copy)
    else:
        for command in commands:
            proceed_single(command, stacks_copy)
    
    return stacks_copy


@timer
def main():
    # input handling
    input_lines = read_input(day_number=5, input_type="txt").split("\n")[:-1]
    stacks_string, commands = split_command_stacks(input_lines)
    stacks_lists = create_stack_lists(stacks_string)


    # result 1
    stacks_1 = proceed_commands(commands, stacks_lists)
    result_1 = "".join(([stack[-1] for stack in stacks_1]))

    # result 2
    stacks_2 = proceed_commands(commands=commands, stacks=stacks_lists, multi=True, debug=False)
    result_2 = ''.join(([stack[-1] for stack in stacks_2]))

    # print results
    print_results(result_1, result_2)


if __name__ == "__main__":
    main()

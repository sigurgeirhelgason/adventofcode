from utils import timer, read_input, print_results


def check_interception(range_1, range_2, full_interception=False):
    start_1, end_1 = map(int, range_1.split("-"))
    start_2, end_2 = map(int, range_2.split("-"))
    if full_interception:
        return (
            (start_1 in range(start_2, end_2 + 1)
            and end_1 in range(start_2, end_2 + 1))
            or 
            (start_2 in range(start_1, end_1 + 1)
            and end_2 in range(start_1, end_1 + 1))
        )
    else:
        return (
            (start_1 in range(start_2, end_2 + 1)
            or end_1 in range(start_2, end_2 + 1))
            or 
            (start_2 in range(start_1, end_1 + 1)
            or end_2 in range(start_1, end_1 + 1))
        )


def count_interceptions(input_lines, full_interception=False):
    interceptions_count = 0

    for line in input_lines:
        range_1, range_2 = line.split(",")
        
        interceptions_count += check_interception(range_1, range_2, full_interception)

    return interceptions_count


@timer
def main():
    input_lines = read_input(4).split("\n")[:-1]
    

    full_interception_count = count_interceptions(input_lines, full_interception=True)
    part_interception_count = count_interceptions(input_lines)

    print_results(answer_part_1=full_interception_count, answer_part_2=part_interception_count)


if __name__ == "__main__":
    main()
from utils import timer, read_input, print_results


def check_pairs(text, buffer_len):
    i = 0
    for _ in text:
        if len(set(text[i : i+buffer_len])) == buffer_len:
            return i+buffer_len
        i+=1




@timer
def main():
    input_lines = read_input(day_number=6, input_type="txt").split("\n")[:-1][0]

    result_1 = check_pairs(input_lines, 4)
    result_2 = check_pairs(input_lines, 14)

    print_results(result_1, result_2)

if __name__ == "__main__":
    main()

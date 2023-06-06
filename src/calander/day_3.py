from utils import timer, read_input


def find_priority(line: str) -> int:
    mid = len(line) // 2
    common_chars = set(line[:mid]) & set(line[mid:])
    priority_value = sum(calculate_priority(char) for char in common_chars)
    return priority_value


def calculate_priority(char: str) -> int:
    if char.isupper():
        return ord(char) - 38
    else:
        return ord(char) - 96


def calculate_badge_sum(input_lines: str) -> int:
    def find_common_char(lines: list[str, str, str]) -> str:
        common_char = set(lines[0]) & set(lines[1]) & set(lines[2])
        if common_char:
            return common_char.pop()
        

    input_lines_iter = iter(input_lines)
    return sum(
        map(
            calculate_priority,
            (
                map(
                    find_common_char,
                    zip(input_lines_iter, input_lines_iter, input_lines_iter),
                )
            ),
        )
    )


@timer
def main():
    input_lines = read_input(3).split("\n")
    input_lines.pop()

    # Part 1
    priority_sum = sum(map(find_priority, input_lines))
    print(f"Part 1: {priority_sum}")

    # Part 2
    badge_sum = calculate_badge_sum(input_lines=input_lines)
    print(f"Part 2: {badge_sum}")


if __name__ == "__main__":
    main()

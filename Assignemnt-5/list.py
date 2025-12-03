numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def list_operations(numbers: list[int]) -> None:
    print(f"Original list: {numbers}")

    extracted_list: list[int] = numbers[:5]
    print(f"Extracted first five elements : {extracted_list}")

    print(f"Reversed extracted list: {list(reversed(extracted_list))}")


list_operations(numbers)

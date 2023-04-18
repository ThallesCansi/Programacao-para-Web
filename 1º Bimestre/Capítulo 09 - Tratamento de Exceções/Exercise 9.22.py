class EmptyListError(Exception):
    pass

def calculate_average(numbers):
    if len(numbers) == 0:
        raise EmptyListError("Cannot calculate average of an empty list.")
    else:
        return sum(numbers) / len(numbers)
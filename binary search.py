# TODO: Given a sorted list of grades in a class, implement Binary Search on this list
grades = [35, 42, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]

# TODO: Implement the Loop-based Binary Search function without recursion
def binary_search(data, target):
    high = len(data)
    low = 0
    while high - low >= 1:
        mid = (low + high) // 2
        if target < data[mid]:
            high = mid
        elif target > data[mid]:
            low = mid
        else:
            return mid
    return low if target == data[low] else None

# TODO: Set a query for a student's grade for your search
student_grade = 60

# TODO: Invoke the Binary Search function. If you find the grade, print the position in the grade list; if not, print a not found message.
result = binary_search(grades, student_grade)
if result is not None:
    print(f"The student grade whichh is {student_grade} is at the position {result}")
else:
    print(f"The student grade, {student_grade}, not in the list")

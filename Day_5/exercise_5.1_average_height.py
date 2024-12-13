student_heights = input("Input a list of students heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

total_height = 0
# for n in range(0, len(student_heights)):
#     total_height += student_heights[n]
for height in student_heights:
    total_height += height

average_height = round(total_height / len(student_heights))
print(f"The average height is: {average_height}")

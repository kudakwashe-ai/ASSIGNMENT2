math = float(input("Enter Math score: "))
science = float(input("Enter Science score: "))
english = float(input("Enter English score: "))

average_score = (math + science + english) / 3

if average_score > 75:
    print("You passed!")
elif math > 100 or science > 100 or english > 100:
    print("You passed!")
elif (math < 70 and science >= 70 and english >= 70) or \
     (math >= 70 and science < 70 and english >= 70) or \
     (math >= 70 and science >= 70 and english < 70):
    print("You passed!")
else:
    print("You failed.")

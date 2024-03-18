start = 5
end = 20

if start < end:
    print(f"Gerade Zahlen zwischen {start} und {end}: ", end=" ")
    for i in range(start, end+1, 1):
        if i % 2 == 0:
            print(i, end=", ")
else:
    print("Error")

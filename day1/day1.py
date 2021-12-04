last = 0
count = 0
values = [int(line.strip()) for line in open("day1input.txt")]
print(len([i for i in range(len(values)-1) if values[i+1] > values[i]]))
print(len([i for i in range(len(values)-3) if values[i+1]+values[i+2]+values[i+3] > values[i]+values[i+1]+values[i+2]]))

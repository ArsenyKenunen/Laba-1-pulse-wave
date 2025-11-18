import matplotlib.pyplot as plt


averages = list()
real_values = (40, 80, 120, 160)
for num in real_values:
    with open(f"calibrations_{num}.csv") as f:
        all_lines = f.readlines()
        averages.append(sum(list(map(lambda s: float(s.split(',')[1]), all_lines))) / len(all_lines))
print(averages)

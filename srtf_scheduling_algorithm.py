n = int(input("Enter number of processes: "))

at = []
bt = []

print("Enter arrival times:")
for i in range(n):
    at.append(int(input()))

print("Enter burst times:")
for i in range(n):
    bt.append(int(input()))

rt = bt[:]
ct = [0]*n
wt = [0]*n
tat = [0]*n

complete = 0
t = 0

while complete != n:
    minm = 10**9
    short = -1

    for i in range(n):
        if at[i] <= t and rt[i] > 0 and rt[i] < minm:
            minm = rt[i]
            short = i

    if short == -1:
        t += 1
        continue

    rt[short] -= 1

    if rt[short] == 0:
        complete += 1
        finish_time = t + 1
        ct[short] = finish_time
        wt[short] = finish_time - bt[short] - at[short]
        if wt[short] < 0:
            wt[short] = 0

    t += 1

for i in range(n):
    tat[i] = bt[i] + wt[i]

print("\nProcess  AT  BT  CT  WT  TAT")
for i in range(n):
    print(f"P{i+1}\t {at[i]}   {bt[i]}   {ct[i]}   {wt[i]}   {tat[i]}")

print("\nAverage Waiting Time =", sum(wt)/n)
print("Average Turnaround Time =", sum(tat)/n)

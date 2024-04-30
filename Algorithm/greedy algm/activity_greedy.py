def activity_greedy(time):
    time.sort(key = lambda x:x[1])
    res = []
    for time_taken in range(len(time)):
        if time_taken == 0:
            res.append(time[time_taken])
            temp = time[time_taken][1]
        else:
            if temp <= time[time_taken][0]:
                res.append(time[time_taken])
                temp = time[time_taken][1]
    return res
arr=[[3,4],[0,6],[1,2],[5,7],[8,9],[5,9]]
result = activity_greedy(arr)
print("Activity",result)
print("Max_activity",len(result))    
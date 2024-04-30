wt=[3,4,6,5]
pf=[2,3,1,4]
knapsac_weight=8

lst=[[0]*(knapsac_weight+1) for _ in range(len(wt)+1)]

for row in range(1,len(lst)):
    for column in range(knapsac_weight+1):
        # if row == 0:
        #     continue
        if wt[row-1] <= column:
            lst[row][column] = max(pf[row-1]+lst[row-1][column-wt[row-1]],lst[row-1][column])
        else:
            lst[row][column] = lst[row-1][column]
            
print(lst)
            

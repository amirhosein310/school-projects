import numpy as np
import time

start_time = time.time()



truck_data = np.array([150,20,40,30])  #  max weight, x , y , z

volumes = np.array([[1,10,11,25], #  code, x , y ,z
                    [2,10,15,100],
                    [3,10,12,250]])

box_data = np.array([[1,150,9.75,11], #  volume code, value, weight, code
                     [2,250,11.75,14],
                     [2,220,10.75,15],
                     [1,200,200.75,10],
                     [3,2050,70.75,17],
                     [1,215,11.75,25],
                     [1,5,20.75,27]])

def group_split(box, groups):
    split_list  = []
    group_codes = groups[::,0]
    for i in group_codes:
        g = np.where(box[::,0] == i)
        splits = box[g]
        split_list.append(splits)
    return split_list


def group_score(group, truck,box):
    vscore_list = []
    tscore_list = []
    truck_area = truck[1]*truck[2]*truck[3]
    group_codes = group[::,0]
    for i in group_codes:
        ind = np.where(group[::,0] == i)
        group_data = group[ind]
        group_volume = group_data[0][1]*group_data[0][2]*group_data[0][3]
        score = [(group_volume/truck_area)*100+1,i,group_volume]
        vscore_list.append(score)
    for i in range(0,len(box)):
        score1 = box[i][1]/box[i][2]

        for j in range(0,len(vscore_list)):

            if vscore_list[j][1] == box[i][0]:

                score2 = [score1/vscore_list[j][0],vscore_list[j][2],box[i][1],box[i][2],box[i][3],group_data[0][1],group_data[0][2],group_data[0][3]]
                tscore_list.append(score2)
    return sorted(tscore_list,reverse=True)

#print(group_score(volumes,truck_data,box_data))

def choose(score , truck_arr):
    layer = 0
    space_mat = np.zeros([truck_arr[1],truck_arr[2],truck_arr[3]])
    i = 0
    chosen = []
    used_space = 0
    x_used = 0
    y_used = 0
    z_used = 0
    used_weight = 0
    total_value = 0
    truck_area = truck_arr[1] * truck_arr[2] * truck_arr[3]
    max_weight = truck_arr[0]
    while used_weight < max_weight and used_space < truck_area and i<len(score):
        if score[i][3]+used_weight <= max_weight and used_space+score[i][1] <= truck_area:
            if x_used >= truck_arr[1]:
                layer +=1
                x_used=0
                y_used=0
                space_mat[x_used:score[i][5], y_used:score[i][6], layer] = score[i][4]
            else:
                space_mat[x_used:score[i][5],y_used:score[i][6],layer] = score[i][4]
            x_used += score[i][5]
            y_used += score[i][6]
            chosen.append(score[i])
            used_space += score[i][1]
            used_weight += score[i][3]
            total_value += score[i][2]
        i+=1


    print('*'*80,'\nTotal value: ',total_value)
    print('\nChoosen items: [score, volume, value, code ]')
    print(chosen)
    print('\n',space_mat[::,::,::])

scoret = group_score(volumes,truck_data,box_data)
choose(scoret , truck_data)

print ('\nExecution time: ',time.time() - start_time, "seconds")


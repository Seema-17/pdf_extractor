def func(delta_x,delta_y,c1,c2,c3,c4,d1,d2,d3,d4):
    list_1=[(c1+delta_x,c1+delta_y),(c2-delta_x,c2+delta_y),(c3-delta_x,c3-delta_y),(c4+delta_x,c4-delta_y)]
    list_2=[(c1-delta_x,c1-delta_y),(c2+delta_x,c2-delta_y),(c3+delta_x,c3+delta_y),(c4-delta_x,c4+delta_y)]
    if not ((d1[0] >=list_1[0][0]) & (d1[0]<=list_2[0][0])) :
        return False
    if not ((d1[1] >=list_1[0][1]) & (d1[1]<=list_2[0][1])) :
        return False
    if not ((d2[0] >=list_1[1][0]) & (d2[0]<=list_2[1][0])) :
        return False
    if not ((d2[1] >=list_1[1][1]) & (d2[1]<=list_2[1][1])) :
        return False
    if not ((d3[0] >=list_1[2][0]) & (d3[0]<=list_2[2][0])) :
        return False
    if not ((d3[1] >=list_1[2][1]) & (d3[1]<=list_2[2][1])) :
        return False
    if not ((d4[0] >=list_1[3][0]) & (d4[0]<=list_2[3][0])) :
        return False
    if not ((d4[1] >=list_1[3][1]) & (d4[1]<=list_2[3][1])) :
        return False
    
    return True
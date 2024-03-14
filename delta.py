import json
def func(c1,c2,c3,c4,d1,d2,d3,d4):
    # print(c1,c2,c3,c4)
    # print(d1,d2,d3,d4)
    delta_x = (c3[0]-c4[0])*0.10
    delta_y = (c4[1]-c1[1])*0.02
    list_1=[(c1[0]+delta_x,c1[1]+delta_y),(c2[0]-delta_x,c2[1]+delta_y),(c3[0]-delta_x,c3[1]-delta_y),(c4[0]+delta_x,c4[1]-delta_y)]
    list_2=[(c1[0]-delta_x,c1[1]-delta_y),(c2[0]+delta_x,c2[1]-delta_y),(c3[0]+delta_x,c3[1]+delta_y),(c4[0]-delta_x,c4[1]+delta_y)]
    ans = True
    ans = ans and ((d1[0] <= list_1[0][0]) and (d1[0] >= list_2[0][0]))
    ans = ans and ((d1[1] <= list_1[0][1]) and (d1[1] >= list_2[0][1]))
    ans = ans and ((d2[0] >= list_1[1][0]) and (d2[0] <= list_2[1][0]))
    ans = ans and ((d2[1] <= list_1[1][1]) and (d2[1] >= list_2[1][1]))
    ans = ans and ((d3[0] >= list_1[2][0]) and (d3[0] <= list_2[2][0]))
    ans = ans and ((d3[1] >= list_1[2][1]) and (d3[1] <=list_2[2][1]))
    ans = ans and ((d3[1] >= list_1[2][1]) and (d3[1] <= list_2[2][1]))
    ans = ans and ((d4[0] <= list_1[3][0]) and (d4[0] >= list_2[3][0]))
    ans = ans and ((d4[1] >= list_1[3][1]) and (d4[1] <= list_2[3][1]))
    return ans


# account number, invoice number, invoice date, total amount

account_number_coords = {
    "c_1": [
        140.0,
        416.0
    ],
    "c_2": [
        562.0,
        419.0
    ],
    "c_3": [
        562.0,
        475.0
    ],
    "c_4": [
        140.0,
        472.0
    ],
    "var_name": "296664039561"
}

invoice_number_coords = {
    "c_1": [
        2139.0,
        465.0
    ],
    "c_2": [
        2292.0,
        465.0
    ],
    "c_3": [
        2292.0,
        502.0
    ],
    "c_4": [
        2139.0,
        502.0
    ],
    "var_name": "42183017"
}

invoice_date_coords = {
    "c_1": [
        2052.0,
        512.0
    ],
    "c_2": [
        2291.0,
        504.0
    ],
    "c_3": [
        2292.0,
        551.0
    ],
    "c_4": [
        2053.0,
        558.0
    ],
    "var_name": "August 3 , 2014"
}

total_amount = {
    "c_1": [
        2175.0,
        571.0
    ],
    "c_2": [
        2288.0,
        571.0
    ],
    "c_3": [
        2288.0,
        620.0
    ],
    "c_4": [
        2175.0,
        620.0
    ],
    "var_name": "$4.11"
}

with open('tests/output/AmazonWebServices3.json') as data_file:    
    data = json.load(data_file)
    # print(len(data["page_1"]))
    numElements = len(data["page_1"]) - 1
    for i in range(numElements):
        d = data["page_1"][str(i)]
        print("hi")
        if(func(account_number_coords["c_1"], account_number_coords["c_2"], account_number_coords["c_3"], account_number_coords["c_4"], d["c_1"], d["c_2"], d["c_3"], d["c_4"])):
            acc_num = d["var_name"]
            print(f"Account number: {acc_num}")
        if(func(invoice_number_coords["c_1"], invoice_number_coords["c_2"], invoice_number_coords["c_3"], invoice_number_coords["c_4"], d["c_1"], d["c_2"], d["c_3"], d["c_4"])):
            invoice_num = d["var_name"]
            print(f"Invoice number: {invoice_num}")
        if(func(invoice_date_coords["c_1"], invoice_date_coords["c_2"], invoice_date_coords["c_3"], invoice_date_coords["c_4"], d["c_1"], d["c_2"], d["c_3"], d["c_4"])):
            invoice_date = d["var_name"]
            print(f"Invoice date: {invoice_date}")
        if(func(total_amount["c_1"], total_amount["c_2"], total_amount["c_3"], total_amount["c_4"], d["c_1"], d["c_2"], d["c_3"], d["c_4"])):
            ttl_amount = d["var_name"]
            print(f"Total amount: {ttl_amount}")
        
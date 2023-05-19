# n = input("Enter your mobile number: ")
# str = sorted(n)
# if len(str) == 10 :
#     print("+91-"+"".join(str))
# else:
#     print("Enter the proper mobile number that consist of 10 digits")

def standar_mobile_no(*mob_nums):
    res = []
    for mob_num in mob_nums:
        mob_num = sorted(mob_num, reverse= True)
        # i.insert(0,i.pop())
        mob_num = "".join(mob_num)
        res.append(f'+91  {mob_num}')
    return res

mob_nums = [i for i in input("Enter the mobile Numbers: ").split()]
print(standar_mobile_no(*mob_nums))


# Input: Enter the mobile Numbers: 9739223665  123456789 987654321 3445566779
# Out_put: ['+91  9976653322', '+91  987654321', '+91  987654321', '+91  9776655443']
# written by Yuchen YAN for comp9021 lab2

'''
Write a program multiplication.py that decodes all multiplications of the form
the sum of all digits in all 4 columns is constant.
'''



if __name__ == '__main__':
    for times in range(1,3):
        if times == 1:
            multiplier_1a = [0, 4, 1, 1]
            multiplier_1b = [0, 0, 1, 3]
        elif times == 2:
            multiplier_1a = [0, 4, 2, 5]
            multiplier_1b = [0, 0, 2, 3]

        
        transfer_1a = [0]*4
        transfer_1b = [0]*4
        sum_1 = [0]*4
        carry_1 = 0
        carry_2 = 0
        transfer_1b[3] = 0
        
        for i in range(3,1,-1):
            for j in range(3,0,-1):
                if i==3:
                    transfer_1a[j] = (multiplier_1b[i]*multiplier_1a[j]) % 10 + carry_1
                    carry_1 = (multiplier_1b[i]*multiplier_1a[j]) // 10
                    if j == 1:
                        transfer_1a[0] = carry_1
                elif i==2:
                    transfer_1b[j-1] = (multiplier_1b[i]*multiplier_1a[j]) % 10 + carry_2
                    carry_2 = (multiplier_1b[i]*multiplier_1a[j]) // 10
        
        for k in range(0,4):
            sum_1[k] = transfer_1a[k]+transfer_1b[k]
        adding_up = multiplier_1a[0] + multiplier_1b[0] + transfer_1a[0] + transfer_1b[0] + sum_1[0]
        number_1 = multiplier_1a[3] + multiplier_1a[2]*10 + multiplier_1a[1]*100
        number_2 = multiplier_1b[3] + multiplier_1b[2]*10
        answer = sum_1[3] +sum_1[2]*10 +sum_1[1]*100 +sum_1[0]*1000
    
        print(f'{number_1} * {number_2} = {answer}, all columns adding up to {adding_up}.')




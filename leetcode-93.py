
'''
leetcode系列：题号-93
Description:Given a string containing only digits, restore it by returning all possible valid IP address combinations.
Author:worthurlove
Date:2019.5.14
'''
s = '010010'


def str2ip(s):

    ip_address = []
    n = len(s)
    i_flag = 1
    j_flag = 1
    k_flag = 1
    l_flag = 1
    for i in range(1,min(4,n - 2)):
            for j in range(i + 1,min(n - 1,i + 4)):
                    for k in range(j + 1,min(j + 4,n)):
                        if int(s[0:i]) <= 255 and int(s[i:j]) <= 255 and int(s[j:k]) <= 255 and int(s[k:n])<=255:

                                if i > 1 and s[0] == '0':
                                   i_flag = 0

                                if j - i > 1 and s[i] == '0':
                                    j_flag = 0

                                if  k - j > 1 and s[j] == '0':
                                    k_flag = 0

                                if n - k > 1 and s[k] == '0':
                                    l_flag = 0
                                    

                                if i_flag and j_flag and k_flag and l_flag:
                                    newIP = s[0:i]+'.'+s[i:j]+'.'+s[j:k]+'.'+s[k:n]
                                    ip_address.append(newIP)

                                i_flag = 1
                                j_flag = 1
                                k_flag = 1
                                l_flag = 1

    #print(ip_address)
    return ip_address

str2ip(s)
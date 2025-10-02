# import time
# starttime = time.time()
# v1 = "python-pure-functions"
# v2 =v1[::-1]
# print(v2)
# print(starttime - time.time())
def string_reversal(str):
    if len(str) == 0:
        return str
    else:
        return string_reversal(str[1:])+ str[0]
str = "oderamarkbash"
reversed = string_reversal(str)
print(reversed)
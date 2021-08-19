n= input()
s = input()
t = input()
lst = list(zip(s,t))
days = 0
dict = {'A':'1','B':'2','C':'3','D':'4','E':'5','F':'6','G':'7','H':'8','I':'9','J':'10','K':'11','L':'12','M':'13','N':'14','O':'15','P':'16','Q':'17','R':'18','S':'19','T':'20','U':'21','V':'22','W':'23','X':'24','Y':'25','Z':'26'}
for i in lst:
    s_val = dict[i[0]]
    t_val = dict[i[1]]
    if int(t_val) < int(s_val):
        end_count = int(dict['Z']) - int(s_val)
        before_count = int(t_val) - int(dict['A']) 
        lengthy = abs(end_count + before_count)+1
    else:
        lengthy = abs(int(s_val)-int(t_val))
    if lengthy<13:
        days += lengthy
    else:
        days += lengthy//13
        days += lengthy%13
print(days)
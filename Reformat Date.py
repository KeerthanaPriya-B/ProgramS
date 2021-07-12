from datetime import datetime
d=input()
a=datetime.strptime(d,"%dth %b %Y")
print(str(a).strip('00:00:00'))
from datetime import datetime        
d=input().replace('#',' ')
a=datetime.strptime(d,'%d %m %Y')

print(a.strftime('%A'))
#functions

ip = '10.10.10.10'
def attack(i):
    print(i)

attack(ip)

def attack1(i,d):
    print(f"ip is: {i} and domain is : {d}")

attack1('10.10.10.01','example.com')

ip_ = '10.10.10.02'
domian = 'one.com'
attack1(ip,domian)
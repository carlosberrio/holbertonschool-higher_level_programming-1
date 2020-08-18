# 0x10. Python - Network #0


SSH access: ssh 9914d125a5ef@879dfdd1.hbtn-cod.io
Password: 71b217593295cf6cd37e

curl -s -o /dev/null -D 0.0.0.0:5000/route_4

curl -s -I 0.0.0.0:5000/route_4  | grep "Allow" | cut -d ":"  -f2

curl -s -I 0.0.0.0:5000/route_4  | grep "Allow" | sed 's/Allow: //g'


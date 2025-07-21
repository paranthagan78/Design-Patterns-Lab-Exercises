#serializing multiple objects using JSON

import json

ball_1={'color':'blue','radius':5,'weight':100,'plasticball':True,'owner':None}
ball_2={'color':'Yellow','radius':15,'weight':200,'plasticball':True,'owner':None}

print(type(ball_1))

#serializing json string
json_str=json.dumps([ball_1,ball_2])


print(type(json_str))


#serializing json file
with open('file2.json','w') as f2:
    json.dump([ball_1,ball_2],f2, indent=4)

with open('file2.json','r') as f2:
    a=json.load(f2)
    
print(a)


"""#pickling
import pickle  

data=[
    {'name': 'Yogesh',
    'age': 19,
    'city': 'Thiruvarur'},
    {'name': 'Lashika',
    'age': 19,
    'city': 'Chennai'}
    ]

with open("file1.txt","wb") as f1:
    pickle.dump(data,f1)

with open("file1.txt","rb") as f1:
    loaded_file1=pickle.load(f1)
    print(loaded_file1)
"""


"""
#Serialization of a single object using JSON
import json
ball={'color':'blue','radius':5,'weight':100,'plasticball':True,'owner':None}
ball1={'color':'red','radius':51,'weight':1001,'plasticball':True,'owner':None}
#serializing json string
json_str=json.dumps(ball,indent=4)
print(json_str)
print(type(json_str))

#serializing json file
with open('file2.json','w') as f2:
    json.dumps([ball,ball1],f2, indent=4)
with open('file2.json','r') as f2:
    ball_new=json.loads(f2)

print(ball_new)
#print('color is',ball_new['color'])
# for k,v in ball_new.items():
#     print('{}:{}'.format(k,v))
#print(ball_new)
"""

#Need to install pyyaml 
import yaml
with open('patient.yml','r') as f:
    file_1=yaml.safe_load(f)

print(type(file_1))
print(file_1)
print(file_1['patient_details']['phone'])   
with open('student.yml','r') as f:
    files=yaml.safe_load_all(f)
    for each_file in files:
        print(each_file)


#YAML to JSON
import yaml
import json
with open('patient.yml', 'r') as file:
    yml_file = yaml.safe_load(file) #reads from unreliable and untrusted sources

with open('patient_new.json', 'w') as json_file:
    json.dump(yml_file, json_file,indent=2)
    
with open('patient_new.json', 'r') as json_file:
    patient_json=json.load(json_file)

print(patient_json)



"""
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
print(a)"""
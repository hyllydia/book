import json

with open('states.json','r') as f:
  state_data= json.load(f)
print(state_data)

for state in state_data['states']:
  del state['area_codes']

with open('new_states.json', 'w') as f:
    json.dump(state_data,f,indent=2)
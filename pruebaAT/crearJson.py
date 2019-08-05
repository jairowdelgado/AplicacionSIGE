import json
data = {}
data['horarios'] = []
data['horarios'].append({
    'hora1':'7',
    'sala':'salon 226 FIET',
    'dia':'1'})
data['horarios'].append({
    'hora1':'9',
    'sala':'salon 224 FIET',
    'dia':'2'})
data['horarios'].append({
    'hora1':'11',
    'sala':'sala 4 FIET',
    'dia':'4'})
with open('horarioSalons.json', 'w') as file:
    json.dump(data, file, indent=4)
import json

new_data = open("stereo_data.txt", "w")


with open('dev.json') as d:
    data = json.load(d)
    # print(len(data['data'].keys()))
    # print(data['data'].keys())
    # print(len(data['data']['intrasentence']))
    count = 0
    for s in data['data']['intersentence']:
        if(s['bias_type'] == 'gender'):
            count += 1
            print(s['context'])
            new_data.write(s['context'] + '\n')
    print(count)

import json
import os
from argparse import ArgumentParser
import csv
import pandas as pd

parser = ArgumentParser()
parser.add_argument('-i', '--input', required=True)
parser.add_argument('-o', '--output', required=False)
args = parser.parse_args()

if args.output is None:
    output = "batch_info_{}.csv".format(args.input.replace("/",""))
else:
    output = args.output

columns = ['name', 'age', 'audioFilename', 'deviceId', 'gender', 'location', 'noiseCondition', 'participantId',
           'phrase', 'phraseId', 'recordingId', 'program']
# df = pd.DataFrame(columns=columns)
fp = open(output, 'w')
writer = csv.writer(fp)
writer.writerow(columns)

def create_batch_info(filepath):
    global df
    with open(filepath, 'r', encoding='utf8') as fp:
        data = json.load(fp)

        for dic in data:
            out_list = [dic["name"], dic["age"],
                        dic["audioFilename"],
                        dic["deviceId"],
                        dic["gender"],
                        dic["location"],
                        dic["noiseConditions"],
                        dic["participantId"],
                        dic["phrase"],
                        dic["phraseId"],
                        dic["recordingId"],
                        dic["program"]]
            writer.writerow(out_list)


for path, subdirs, files in os.walk(args.input):
    for name in files:
        filepath = os.path.join(path, name)
        if os.path.basename(filepath) != 'data.json':
            continue
        create_batch_info(filepath)

# df.to_csv(output)
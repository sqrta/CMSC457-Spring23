import json

from datetime import datetime

f = open("metadata.json")
data = json.load(f)
now = datetime.strptime(data["created_at"], "%Y-%m-%dT%H:%M:%S.%f%z")
previous = data['previous_submissions'][0]['submission_time']
print(previous)

previous_time = datetime.strptime(previous, "%Y-%m-%dT%H:%M:%S.%f%z")
gap = now-previous_time
print(gap.total_seconds())
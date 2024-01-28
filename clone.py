import json

with open('How-To-Use-Clone-Shields_clone.json', 'r') as fh: now = json.load(fh)
with open('How-To-Use-Clone-Shields_clone_before.json', 'r') as fh: before = json.load(fh)

latest = dict(before)

if 'count_past_to_last_2_weeks_ago' not in latest.keys(): latest['count_past_to_last_2_weeks_ago'] = 0
if 'uniques_past_to_last_2_weeks_ago' not in latest.keys(): latest['uniques_past_to_last_2_weeks_ago'] = 0
if 'count_total' not in latest.keys(): latest['count_total'] = 0
if 'uniques_total' not in latest.keys(): latest['uniques_total'] = 0 

timestamps = {latest['clones'][i]['timestamp']: i for i in range(len(latest['clones']))} # 具有唯一性

for i in range(len(now['clones'])): 
    timestamp = now['clones'][i]['timestamp'] # 從最新抓取訊息中的時間戳來判斷該筆是否存在過去的資料當中
    if timestamp in timestamps: latest['clones'][timestamps[timestamp]] = now['clones'][i] # 若在裡面，更新資料
    else: latest['clones'].append(now['clones'][i]) # 不在裡面，新增該筆資料

if len(latest["clones"]) > 14:
    temp_list = latest["clones"][:-14]
    latest["clones"] = latest["clones"][-14:]
    for i in temp_list:
        latest['count_past_to_last_2_weeks_ago'] += i['count']
        latest['uniques_past_to_last_2_weeks_ago'] += i['uniques']

# 如此一來，根據 20-25 行的過濾判斷，加總的內容也就只局限於最近2周(14天)的內容 # 避免時間一拉長，json 紀錄過龐大
latest['count'] = sum(map(lambda x: int(x['count']), latest['clones']))
latest['uniques'] = sum(map(lambda x: int(x['uniques']), latest['clones']))
latest['count_total'] = latest['count_past_to_last_2_weeks_ago'] + latest['count']
latest['uniques_total'] = latest['uniques_past_to_last_2_weeks_ago'] + latest['uniques']
with open('How-To-Use-Clone-Shields_clone.json', 'w', encoding='utf-8') as fh: json.dump(latest, fh, ensure_ascii=False, indent=4)
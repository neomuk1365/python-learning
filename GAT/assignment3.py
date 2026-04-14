logs = [
{'user': 'Ravi', 'msg': 'Started ML'}, {'user': 'Ravi', 'msg': 'Fixed Bug'}
]
#{'Ravi': ['Started ML', 'Fixed Bug']}
#topdown 
#dailylogstopdown={'Ravi':[]}
for log in logs:
    key_user=log.get('user','na')
    dailylogstopdown={key_user:[]}
for log in logs:
    dailylogstopdown[log.get('user','na')].append(log.get('msg','na'))
print(dailylogstopdown)

daily_logs={}
for log in logs:
    key_daily_logs=log.get('user','na')
    if key_daily_logs not in daily_logs:
        daily_logs[key_daily_logs]=[]
    # if  not in daily_logs:
    daily_logs[key_daily_logs].append(log.get('msg','na'))
print(daily_logs)


import datetime

def get_nday_list(n):
    before_n_days = []
    for i in range(1, n + 1)[::-1]:
        before_n_days.append(time.strptime(datetime.date.today() - datetime.timedelta(days=i), , "%Y%m%d"))
    return before_n_days

a = get_nday_list(7)
print(a)

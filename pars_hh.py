import requests
import csv
job_name = 'data'
def pars(period=1):
    ''' Парсим вакансии с hh.ru по направлению Data в словарь {работодатель : вакансии} '''
    job_dict = {}
    for i in range(40):
        params = {
            'text': f'NAME:{job_name}',
            'period': period,
            'per_page': 50,
            'page': i
        }
        url = 'https://api.hh.ru/vacancies'
        r = requests.get(url, params=params)
        vakancy = r.json()
        for i in vakancy['items']:
            job_dict.setdefault(i['employer']['name'], []).append(i['name'])
    return job_dict



jobs = {}
for i, j in pars(7).items():
    jobs[i] = len(j)
list_job = list(jobs.items())
list_job.sort(key=lambda x: x[1], reverse=True)
print(f'Топ 7 компаний с вакансиями {job_name}: {list_job[:5]}')

with open('vacansy.csv', 'w', newline="", encoding='UTF-8') as file:
    writer = csv.writer(file)
    writer.writerows(list_job[:7])

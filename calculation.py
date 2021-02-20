import pandas as pd

main_data = pd.read_csv('DATABASE_FINAL.csv')
unemploymentT = pd.read_csv('UNEMPLOYMENT_TOTAL.csv')
unemploymentM = pd.read_csv('UNEMPLOYMENT_MEN.csv')
unemploymentW = pd.read_csv('UNEMPLOYMENT_WOMEN.csv')

def find_agegroup(age):
    if age < 16:
        return 'T1' #general age
    elif age < 18:
        return 'a1'
    elif age < 20:
        return 'a2'
    elif age < 25:
        return 'B'
    elif age < 35:
        return 'c1'
    elif age < 45:
        return 'c2'
    elif age < 55:
        return 'c3'
    elif age < 65:
        return 'D'
    else:
        return 'T5'

def get_unemployment(gender,age,race):
    age_group=find_agegroup(age)
    if gender == 'F':
        data = unemploymentW
    else:
        data = unemploymentM
    target = data.loc[data['CODE']==age_group]
    global unemployment_rate
    ur = target[race].tolist()
    unemployment_rate = float(ur[0])

def check_job(job):
    for i in main_data['OCCUPATION']:
        if (job==i):
            return True
    return False

def computerisation(job):
    target = main_data.loc[main_data['OCCUPATION']==job] # 'Recreational Therapists'
    global p0
    global rank
    global soc_code
    p=target['PROBABILITY'].tolist()
    r=target['RANK'].tolist()
    s=target['SOC_CODE'].tolist()
    p0=float(p[0])
    rank=r[0]
    soc_code=s[0]

def get_jobs():
    return main_data['OCCUPATION'].tolist()

def get_computerisation(job):
    computerisation(job)
    return round(p0*100,2)

def get_gender(gender):
    if gender == 'F':
        return -3
    else:
        return 3

def get_race(race):
    target = unemploymentT.loc[unemploymentT['CODE']=='T1']
    ur = target[race].tolist()
    p = float(ur[0])
    return int((p-6.5)/6.5*100)

def get_age(age):
    age_group = find_agegroup(age)
    target = unemploymentT.loc[unemploymentT['CODE']==age_group]
    ur = target['TOTAL'].tolist()
    p = float(ur[0])
    return int((p-6.5)/6.5*100)
    
def main(gender, age, race, job):
    computerisation(job) #p0, rank, soc_code
    get_unemployment(gender, age, race) #unemployement_rate
    percent = unemployment_rate/6.5
    p_final = percent*p0
    if p_final>0.99:
        p_final=0.99
    return round(p_final*100)


def function(job):
    get_computerisation(job)
    print(p0)
    print(rank)
    print(soc_code)
    
    
#get_possibility('Recreational Therapists')

#def gender_factor(gender):
#    if gender="N":
#        return 1
#    elif gender="":
#        return 1.2
#    else:
#        return 0.8

#def age_rance_factor(age, race):

#def main():

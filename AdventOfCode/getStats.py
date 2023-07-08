import os

years = {}

f = open('README.md', 'w+')
f.write('## Advent of Code - Personal Stats\n')

meaning = {
    'Solved': 2,
    'Part 2 Remains': 1,
    'Not Attempted': 0,
}

def printYear(year):
    days = years[year]
    stars = str(int(sum(days)))
    f.write('### ' + year + ' - ' + stars + ' / 50\n')
    f.write('```\n')
    for m in meaning:
        daysWithMeaning = [idx + 1 for idx, day in enumerate(days) if day == meaning[m]]
        if len(daysWithMeaning):
            f.write('\t' + m + ': ' + str(len(daysWithMeaning)) 
                    # + '\n\t\t' + str(daysWithMeaning)  
                    + '\n')
    f.write('```\n')

total_stars = 0
for year in os.listdir():
    if year .__len__() != 4:
        continue
    days = [0 for _ in range(25)]
    for day in os.listdir(year):
        toks = day[3:].split()
        id = int(toks[0])
        val = 2
        if len(toks) == 2: val = 0
        if len(toks) == 4: val = 1
        days[id - 1] = val    
    years[year] = days
    printYear(year)
    total_stars += int(sum(years[year]))
f.write('Total stars: ' + str(total_stars) + '/' + str(years.__len__() * 50) + '\n')    

f.close()

import subprocess

subprocess.call(['cat', 'README.md'])

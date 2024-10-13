from bs4 import BeautifulSoup
import datetime

outputfile = open(input('Outputfile: ' )+'.csv', 'w')

html = ""
with open(input("Inputfile: "), 'r') as f:
    html = f.read()
outputfile.write('Subject, Start Date, Start Time, End Date, End Time, Location, Description \n')
eventname = 'STO - Einführung in die Informatik'

basedate = datetime.datetime(2024, 10, 14)

soup = BeautifulSoup(html, 'html.parser')
#print(soup.find_all('td', {'class': 'question'}))
for tr in soup.find_all('tr'):
    q = tr.find_all('td', {'class': 'question'})
    e = tr.find_all('td', {'class': 'element'})
    if len(q) == 0:
        continue
    assert(len(e) > 0)
    assert (len(q) == 1)
    e = e[0].text
    q = q[0].text
    #print(q)
    #print(e)
    uu = e.split(' ')
    day = uu[0].removesuffix(',')
    time = uu[2].split('-')
    group = q
    place = uu[6]
    if (len(uu) > 7):
        place += ' ' + uu[7]
    subject = q + ' ' + eventname

    dayoffs = 0
    match day:
        case 'Montag':
            dayoffs = datetime.timedelta(days=0)
        case 'Dienstag':
            dayoffs = datetime.timedelta(days=1)
        case 'Mittwoch':
            dayoffs = datetime.timedelta(days=2)
        case 'Donnerstag':
            dayoffs = datetime.timedelta(days=3)
        case 'Freitag':
            dayoffs = datetime.timedelta(days=4)
        case 'Samstag':
            dayoffs = datetime.timedelta(days=5)
        case 'Sonntag':
            dayoffs = datetime.timedelta(days=6)
    startt = time[0].split(':')
    endt = time[1].split(':')
    startdate = basedate + dayoffs + datetime.timedelta(hours=int(startt[0]), minutes=int(startt[1]))
    enddate = basedate + dayoffs + datetime.timedelta(hours=int(endt[0]), minutes=int(endt[1]))

    #print(day)
    print(startdate, enddate)
    print(place)
    outputfile.write(f'{subject},{startdate.strftime('%m/%d/%Y')},{startdate.strftime('%H:%M')},{enddate.strftime('%m/%d/%Y')},{enddate.strftime('%H:%M')},{place},\n')

outputfile.close()
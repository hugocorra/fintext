import datetime
import uuid

def strdate_to_date(strdate):
    if strdate.lower() in ('today', 'hoje', 'h'):
        return datetime.date.today()
    else:
        return datetime.datetime.strptime(strdate, "%Y%m%d").date()


def parser(command):
    args = command.split(' ')

    d = {
        'category': args[0],
        'date': strdate_to_date(args[1]),
        'value': args[2],
        'account': args[3],
        'description': ' '.join(args[4:]),
        'uuid': str(uuid.uuid4()),
    }

    return d
    

if __name__ == '__main__':
    j = parser('almoco hoje -33 nubank -l restaurante xyz -d pato assado no molho de laranja')
    print(j)

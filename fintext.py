import sys
import json

import uuid

if __name__ == '__main__':
    args = sys.argv[1:]

    d = {
        'category': args[0],
        'date': args[1],
        'value': args[2],
        'account': args[3],
        'description': ' '.join(args[4:]),
        'uuid': str(uuid.uuid4()),
    }

    print(d)

    try:
        with open('database.json') as database:
            data = json.load(database)

            if data is None:
                data = [d]
            else:
                data.append(d)
    except FileNotFoundError:
        data = [d]
        print('exception')
    finally:
        with open('database.json', 'w') as database:
            json.dump(data, database)
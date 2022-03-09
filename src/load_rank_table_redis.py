import os, sys, redis, math

REDIS_HOST = os.environ['REDIS_HOST']
REDIS_PORT = os.environ['REDIS_PORT']

TOTAL_HANDS = math.comb(52, 5)

try:
    client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, charset='utf-8', decode_responses=True)
except Exception as e:
    print(e)
    exit(1)

if client.dbsize() >= TOTAL_HANDS:
    print('db already populated')
    exit(0)

print('populating')
f = open(sys.argv[1], 'r')
for line in f:
    split_line = line.split(':')
    if len(split_line) == 2:
        index = split_line[0].strip().replace('"', '')
        value = int(split_line[1].strip().replace(',', ''))
        client.set(index, value)
print('populating finished')

exit(0)
import urllib.request
import datetime
from multiprocessing.dummy import Pool

urls = [
    'http://www.python.org',
    'http://www.python.org/about/',
    'http://www.onlamp.com/pub/a/python/2003/04/17/metaclasses.html',
    'http://www.python.org/doc/',
    'http://www.python.org/download/',
    'http://www.python.org/getit/',
    'http://www.python.org/community/',
    'https://wiki.python.org/moin/',
    'http://planet.python.org/',
    'https://wiki.python.org/moin/LocalUserGroups',
    'http://www.python.org/psf/',
    'http://docs.python.org/devguide/',
    'http://www.python.org/community/awards/'
    # etc..
]

# use multiprocessing.dummy
# Make the Pool of workers
pool = Pool()

# Open the urls in their own threads and return the results
start = datetime.datetime.now()
results = pool.map(urllib.request.urlopen, urls)
# close the pool and wait for the work to finish
pool.close()
pool.join()
print(results)

print("use {0} seconds".format(datetime.datetime.now() - start))


# compare
results = []
start = datetime.datetime.now()
for url in urls:
    results.append(urllib.request.urlopen(url))

print(results)
print("use {0} seconds".format(datetime.datetime.now() - start))

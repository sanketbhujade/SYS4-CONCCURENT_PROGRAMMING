#prime or not with concurrent execution to get optimal time
#gathering of processes
from math import sqrt
import asyncio

def isprime(n):     # for prime numbers
    if(n<2):
          return False
    for i in range(2, int(sqrt(n)+1)  ):
              if(n%i==0):
                 return False
    return True

async def check(n):
    if isprime(n):
        print(f"{n} is prime")
    else:
        print(f"{n} is not prime")

async def main():
    t0=552264455225
    t1=157
    t2=423567
    await asyncio.gather(
        check(t0),
        check(t1),
        check(t2)
        
    # await asyncio.sleep(3)
)
loop =asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
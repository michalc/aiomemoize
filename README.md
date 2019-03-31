# aiomemoize [![CircleCI](https://circleci.com/gh/michalc/aiomemoize.svg?style=svg)](https://circleci.com/gh/michalc/aiomemoize) [![Test Coverage](https://api.codeclimate.com/v1/badges/82f9a346683c411b08a6/test_coverage)](https://codeclimate.com/github/michalc/aiomemoize/test_coverage)

Memoize asyncio Python calls. Invalidation is manual/explicit for each set of arguments, although exceptions raised are _not_ cached. This can be used for coroutines, and functions that return a promise.


## Installation

```base
pip install aiomemoize
```


## Usage

For a coroutine whose arguments are hashable, you can create a _memoized_ version by passing it to `memoize`. This returns a tuple of the memoized function, and a function to invalidate the cache on a per-item basis.

For example, the below

```python
import asyncio
from aiomemoize import memoize

async def main():
    memoized, invalidate = memoize(coro)
    results = await asyncio.gather(*[
        memoized('a'),
        memoized('a'),
        memoized('b'),
    ])
    print(results)

    invalidate('a')
    results = await asyncio.gather(*[
        memoized('a'),
        memoized('a'),
        memoized('b'),
    ])
    print(results)

    await memoized('a')

async def coro(value):
    print('Inside coro', value)
    await asyncio.sleep(1)
    return value

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
```

will output

```
Inside coro a
Inside coro b
['a', 'a', 'b']
Inside coro a
['a', 'a', 'b']
```

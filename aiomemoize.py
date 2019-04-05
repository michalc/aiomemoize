import asyncio


def memoize(func):

    cache = {}

    async def cached(*args, **kwargs):
        key = (args, tuple(kwargs.items()))

        if key in cache:
            future = cache[key]
        else:
            future = asyncio.Future()
            cache[key] = future

            try:
                result = await func(*args, **kwargs)
            except BaseException as exception:
                del cache[key]
                future.set_exception(exception)
            else:
                future.set_result(result)

        return await future

    def invalidate(*args, **kwargs):
        key = (args, tuple(kwargs.items()))
        del cache[key]

    return cached, invalidate

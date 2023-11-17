import asyncio
from exceptions import HTTPException
from app.utils.logging import AppLogger
from starlette.status import HTTP_401_UNAUTHORIZED


logger = AppLogger.__call__().get_logger()


def capche_retry(max_retry=5):
    def wrapper(func):
        async def wrapper_call(*args, **kwargs):
            if "trycount" in kwargs:
                trycount = kwargs.pop("trycount")
            else:
                trycount = 0

            if trycount >= max_retry:
                logger.info("验证码错误，达到最大重试次数[%s]", func.__name__)
                raise HTTPException(
                    status_code=HTTP_401_UNAUTHORIZED,
                    detail="验证码错误，达到最大重试次数[{}]".format(func.__name__),
                )

            try:
                return await func(*args, **kwargs)
            except CapcheError:
                kwargs["trycount"] = trycount + 1
                logger.info("验证码错误[%s]", func.__name__)
                await asyncio.sleep(1)
                return await wrapper_call(*args, **kwargs)

        return wrapper_call

    return wrapper

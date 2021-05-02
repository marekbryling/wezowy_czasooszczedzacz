import os


async def app(scope, receive, send):
    assert scope['type'] == 'http'
    env_version = os.environ.get("RUN_ENV", 'unset')

    await send({
        'type': 'http.response.start',
        'status': 200,
        'headers': [
            [b'content-type', b'text/plain'],
        ],
    })
    await send({
        'type': 'http.response.body',
        'body': f'Hello, world!\nOn "{env_version}" enviroment'.encode(),
    })

import asyncio

from data import config
from utils.db_api import quick_commands as commands
from utils.db_api.db_gino import db


async def db_test():
    await db.set_bind(config.POSTGRES_URI)
    await db.gino.drop_all()
    await db.gino.create_all()

    await commands.add_user(1, 'Daniil', 'tes')
    await commands.add_user(2, 'Nikita', 'test')
    await commands.add_user(3, 'test_2', '432')
    await commands.add_user(4, 'test_3', 'trw')
    await commands.add_user(5, 'test_4', '4234234')

    users = await commands.select_all_users()
    print(users)

    count = await commands.count_users()
    print(count)

    user = await commands.select_user(1)
    print(user)

    await commands.update_user_name(1, 'New Daniil')

    user = await commands.select_user(1)
    print(user)


loop = asyncio.get_event_loop()
loop.run_until_complete(db_test())

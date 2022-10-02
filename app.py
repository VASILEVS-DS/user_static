from flask import Flask, render_template
from utils.db_api.schemas.user import User
from data import config
from utils.db_api.db_gino import db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

app = Flask(__name__)
#engine = create_engine(config.POSTGRES_URI)
#session = Session(engine)
# async def all_users():
#     users = session.execute('select * from user').fetchall()
#     return [user for user in users]


@app.route('/', methods=['GET'])
async def all_users():
    await db.set_bind(config.POSTGRES_URI)
    users = await User.query.gino.all()
    return [user.to_dict() for user in users]

if __name__ == '__main__':
    app.run(debug=True)


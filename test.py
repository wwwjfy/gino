import asyncio
import trio
import trio_asyncio

from gino import Gino

db = Gino()


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.BigInteger(), primary_key=True)
    nickname = db.Column('nickname', db.Unicode(), default='noname')

    def __repr__(self):
        return f'<{self.id}>{self.nickname}'


# class Parent(db.Model):
#     __tablename__ = 'parents'
#
#     id = db.Column(db.BigInteger(), primary_key=True)
#
#     def __init__(self, **kw):
#         super().__init__(**kw)
#         self._c1s = []
#         self._c2s = []
#
#     @property
#     def c1s(self):
#         return self._c1s
#
#     @c1s.setter
#     def add_c1(self, c1):
#         self._c1s.append(c1)
#
#     @property
#     def c2s(self):
#         return self._c2s
#
#     @c2s.setter
#     def add_c2(self, c2):
#         self._c2s.append(c2)

# class Child1(db.Model):
#     __tablename__ = 'childones'
#
#     id = db.Column(db.BigInteger(), primary_key=True)
#     parent_id = db.Column(db.BigInteger, db.ForeignKey('parents.id', ondelete='CASCADE'), index=True)
#
# class Child2(db.Model):
#     __tablename__ = 'childtwos'
#
#     id = db.Column(db.BigInteger(), primary_key=True)
#     parent_id = db.Column(db.BigInteger, db.ForeignKey('parents.id', ondelete='CASCADE'), index=True)


async def main():
    await db.set_bind('postgresql://localhost/gino')
    # query = Parent.outerjoin(Child1).select()
    # result = await query.gino.load(Parent
    #                                .distinct(Child1.id)
    #                                .load(add_c1=Child1)).all()
    print(await User.query.gino.all())
    # query = Child1.outerjoin(Parent).select()
    # parents = await query.gino.load(
    #     Parent.distinct(Parent.id).load(add_child=Child1)).all()
    # print(parents)
    # print(len(all_users))


# asyncio.get_event_loop().run_until_complete(main())
from trio_asyncio import loop
trio_asyncio.run(main)
# trio.run(main)

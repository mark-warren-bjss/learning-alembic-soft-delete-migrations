from sqlalchemy import select

from app.db.session import Session
from app.models.appeal import Appeal


def action1_remove():
    """soft-delete an appeal"""
    with Session.begin() as session:
        appeal = session.execute(
            select(Appeal).where(Appeal.name == 'hamster')
        ).scalars().first()

        appeal.deleted = True

        print(appeal)


def show(s):
    print(f"***\n*** {s}\n***")
    with Session.begin() as session:
        appeals = session.execute(select(Appeal)).scalars().all()
        for appeal in appeals:
            print(f"- {appeal.name}{appeal.deleted and ' <== DELETED' or ''}")


if __name__ == '__main__':
    show("before removal")
    action1_remove()
    show("after removal")

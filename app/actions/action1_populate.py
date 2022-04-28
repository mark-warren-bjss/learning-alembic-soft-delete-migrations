from app.db.session import Session
from app.models.appeal import Appeal


def action1_populate():
    """populate appeal table with three entries"""
    with Session.begin() as session:
        appeal1 = Appeal(name="hamster", excuse="Hamster ate my homework")
        appeal2 = Appeal(name="dog", excuse="Dog ate my hamster")
        appeal3 = Appeal(name="apocalypse", excuse="Global apocalypse")
        session.add_all((appeal1, appeal2, appeal3))


if __name__ == '__main__':
    action1_populate()

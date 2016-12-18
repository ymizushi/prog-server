from datetime import datetime
import pickle


class Session:
    def __init__(self, id, env):
        self.id = id
        self.env = env

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    @classmethod
    def create(cls, seed, env):
        session_id = cls.make_session_id(seed)
        return cls(session_id, env)

    @classmethod
    def make_session_id(cls, seed):
        time = str(datetime.now())
        target = time + seed
        return 10

    def serialize(self):
        dic = {}
        dic["id"] = self.id
        dic["env"] = self.env
        return pickle.dumps(dic)

    @classmethod
    def deserialize(cls, raw_session):
        dic = pickle.loads(raw_session)
        print(dic)
        return cls(dic["id"], dic["env"])


class SessionRepository:
    def __init__(self, client):
        self._client = client

    def save(self, session):
        self._client.set(session.id, session.serialize())

    def delete(self, session_id):
        self._client.delete(session_id)

    def get(self, session_id):
        raw_session = self._client.get(session_id)
        if raw_session:
            return Session.deserialize(raw_session)
        else:
            return None


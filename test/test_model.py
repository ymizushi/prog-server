import redis
from model.session import SessionRepository, Session
from model import RedisClient
from lang import Env

pool = redis.ConnectionPool(host='localhost', port='6380', db='1')
original_client = redis.Redis(connection_pool=pool)
redis_client = RedisClient(original_client)


def test_redis_client():
    redis_client.set("hoge", b"1")
    result = redis_client.get("hoge")
    assert result == b'1'


def test_session_repository():
    session_repo = SessionRepository(redis_client)
    outer_env = Env()
    env = Env(outer_env)
    seed = "hoge"
    session = Session.create(seed, env)
    session_repo.save(session)
    assert session == session_repo.get(session.id)

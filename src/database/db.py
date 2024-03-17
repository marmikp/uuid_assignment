import getpass
from contextlib import contextmanager
from urllib.parse import quote_plus

from cryptography.fernet import Fernet
from sqlalchemy import create_engine, orm
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker, declarative_base

from database.models import USA273, create_table

Base = declarative_base()


def decrypt_data(encrypted_data, key):
    print(key, type(key))
    cipher_suite = Fernet(key)
    decrypted_data = cipher_suite.decrypt(encrypted_data).decode()
    return decrypted_data


def decrypt_values(value, key):
    decrypted_value = decrypt_data(value, key)
    return decrypted_value


def get_mysql_url(user, password, host, db):
    return f'mysql+mysqlconnector://{user}:{quote_plus(password)}@{host}:3306/{db}'


class Database:

    def __init__(self, user, password, host, db) -> None:
        self.key = getpass.getpass()
        self.user = decrypt_values(user, self.key)
        self.password = decrypt_values(password, self.key)
        self.host = decrypt_values(host, self.key)
        self.db = decrypt_values(db, self.key)
        self._engine = create_engine(get_mysql_url(self.user, self.password, self.host, self.db), echo=False)
        self._session_factory = orm.scoped_session(
            orm.sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=self._engine,
            ),
        )

    def create_database(self) -> None:
        Base.metadata.create_all(self._engine)

    @contextmanager
    def session(self):
        session = self._session_factory()
        try:
            yield session
        except Exception:
            # logger.exception("Session rollback because of exception")
            session.rollback()
            raise
        finally:
            session.close()

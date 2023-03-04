import unittest
from unittest.mock import patch
from sqlalchemy.orm import sessionmaker, declarative_base


class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.engine_mock = patch('sqlalchemy.create_engine').start()
        self.addCleanup(self.engine_mock.stop)
        self.Engine = self.engine_mock.return_value
        self.Session = sessionmaker(bind=self.Engine)
        self.Base = declarative_base()

    def test_engine(self):
        self.assertIsNotNone(self.Engine)

    def test_session(self):
        session = self.Session()
        self.assertIsNotNone(session)
        session.close()

    def test_base(self):
        self.assertIsNotNone(self.Base)
        self.assertIsNotNone(self.Base.metadata)
        self.assertIsInstance(self.Base.metadata, object)

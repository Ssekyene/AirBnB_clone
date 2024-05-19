#!/usr/bin/python3
"""
Tests class BaseModel
"""


import unittest
import os
import os.path
import uuid
from datetime import datetime as dt
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    """ Tests for class BaseModel"""

    def __init__(self, *args, **kwargs):
        """ Initializes models to test """

        super().__init__(*args, **kwargs)
        self.test_class = BaseModel
        self.test_name = "BaseModel"

    def test_id(self):
        """ Tests id is properly created """

        base = self.test_class()
        with self.subTest(msg="id is str uuid"):
            self.assertIsInstance(base.id, str)
            self.assertIsInstance(uuid.UUID(base.id), uuid.UUID)

    def test_create_datetime(self):
        """ Tests datetime """

        base = self.test_class()
        now = dt.now()
        self.assertIsInstance(base.created_at, dt)
        self.assertIsInstance(base.updated_at, dt)
        self.assertTrue(0 <= (now - base.created_at).total_seconds() < 1)
        self.assertTrue(0 <= (now - base.updated_at).total_seconds() < 1)

    def test_update_datetime(self):
        """ Tests update datetime """

        base = self.test_class()
        now = dt.now()
        self.assertIsInstance(base.updated_at, dt)
        base.updated_at = dt.now()
        self.assertNotEqual(now, base.updated_at)

    def test_to_dict(self):
        """ Tests to_dict """

        base = self.test_class()
        _dict = base.to_dict()
        with self.subTest(msg="contains attributes"):
            set1 = set(_dict.keys())
            set2 = set(base.__dict__.keys())
            self.assertTrue(set2.issubset(set1))
        with self.subTest(msg="__class__ added to dict"):
            self.assertTrue("__class__" in _dict.keys())
            self.assertEqual(_dict['__class__'], self.test_name)
        with self.subTest(msg='created ast is str'):
            self.assertIsInstance(_dict['created_at'], str)
            self.assertEqual(_dict['created_at'], base.created_at.isoformat())
        with self.subTest(msg='updated at is str'):
            self.assertIsInstance(_dict['updated_at'], str)
            self.assertEqual(_dict['updated_at'], base.updated_at.isoformat())

    def test_to_str(self):
        """ Tests __str__ """

        base = self.test_class()
        _pass = '[' + self.test_name + '] ({}) {}'.format(
                base.id, str(base.__dict__))
        self.assertEqual(str(base), _pass)

    def test_save_load(self):
        """ Tests save and reload """

        if os.path.exists('save.json'):
            os.remove('save.json')
        _save = FileStorage()
        _save.reload()
        _object = self.test_class()
        self.assertTrue(self.test_name + '.' + _object.id in _save.all())

    def test_from_dict(self):
        """ Tests calling from dictionary """
        pass


if __name__ == "__main__":
    unittest.main()

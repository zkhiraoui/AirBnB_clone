#!/usr/bin/python3
"""
Initialize the package models.
This module will link to the file storage system.
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()

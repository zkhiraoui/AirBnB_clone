#!/usr/bin/python3
"""
This module initializes the models package.
It creates an instance of FileStorage and calls reload()
to deserialize any previously saved objects into the current session.
"""

from .engine.file_storage import FileStorage

# Create a FileStorage instance for the application.
storage = FileStorage()
storage.reload()


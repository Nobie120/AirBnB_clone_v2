#!/usr/bin/python3



class DBStorage:
    """ Creating tables if engine is DBstorage """
    __engine = None
    __session = None

    def __init__(self):


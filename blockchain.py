# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 21:32:59 2019

@author: Arun Arvindh
"""

import datetime
import hashlib
import json
from flask import Flask, jsonify
#part 1- building a blockchain
class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(proof = 1,previous_hash='0')
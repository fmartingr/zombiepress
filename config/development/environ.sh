#!/bin/bash

THIS=`pwd`

export DEBUG=True
export DATABASE_URL="sqlite:////$PWD/test.sqlite3"

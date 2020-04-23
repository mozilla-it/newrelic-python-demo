#!/bin/bash

export NEW_RELIC_CONFIG_FILE=newrelic.ini

sed -i "s|@LICENSE@|$LICENSE|g" $NEW_RELIC_CONFIG_FILE

newrelic-admin run-program gunicorn --bind 0.0.0.0:8000 main:app



from os import name
import yaml
import pymysql
import logging


def connectMysql() :
    with open('./conf/db_conf.yml', 'r', encoding='utf-8') as f:
        file_content = f.read()
    content = yaml.load(file_content, yaml.FullLoader)
    db = pymysql.connect(host=content["mysql"]["host"], port=content["mysql"]["port"], user=content["mysql"]["username"], password=content["mysql"]["password"], database=content["mysql"]["dbname"],charset="utf8mb4")
    logging.info("mysql connected success")
    
    

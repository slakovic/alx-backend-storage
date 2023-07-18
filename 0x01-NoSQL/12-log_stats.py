#!/usr/bin/env python3
"""
script that provides some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_logs = client.logs.nginx
    # get number of documents in collection
    docs_num = nginx_logs.count()
    get_num = nginx_logs.find({'method': 'GET'}).count()
    post_num = nginx_logs.find({'method': 'POST'}).count()
    put_num = nginx_logs.find({'method': 'PUT'}).count()
    patch_num = nginx_logs.find({'method': 'PATCH'}).count()
    delete_num = nginx_logs.find({'method': 'DELETE'}).count()
    get_status = nginx_logs.find({'method': 'GET', 'path': '/status'}).count()
    
    print("{} logs".format(docs_num))
    print("Methods:")
    print("\tmethod GET: {}".format(get_num))
    print("\tmethod POST: {}".format(post_num))
    print("\tmethod PUT: {}".format(put_num))
    print("\tmethod PATCH: {}".format(patch_num))
    print("\tmethod DELETE: {}".format(delete_num))
    print("{} status check".format(get_status))

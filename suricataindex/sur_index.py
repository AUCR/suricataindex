# coding=utf-8
from udatetime import utcnow, utcnow_to_string
from ujson import loads
from subprocess import check_call
from os import mkdir
from uuid import uuid4
from shutil import rmtree
from dataparserlib.dictionary import flatten_dictionary
from elasticsearch import Elasticsearch, helpers
from logging import error, info


def get_data(index_value, output_dir):
    with open(str(output_dir + "eve.json"), 'r') as eve_json:
        raw_data = eve_json.readlines()
        for item in raw_data:
            data = loads(item)
            flat_data_dictionary = flatten_dictionary(data)
            flat_data_dictionary["report"]["process_time"] = utcnow()
            if '{"index"' not in item:
                if "timestamp" in flat_data_dictionary["report"]:
                    new_time_index = str(flat_data_dictionary['report']['timestamp'])[:10].lower()
                    new_index_value = f"{index_value}{new_time_index}"
                else:
                    new_index_value = f"{index_value}{utcnow_to_string[:10].lower()}"
                yield {
                    "_index": new_index_value,
                    "_id": uuid4(),
                    "_source": flat_data_dictionary["report"]
                }
            else:
                yield {
                    "_index": index_value,
                    "_id": uuid4(),
                    "_source": flat_data_dictionary["report"]
                }


def index_to_es(index_value, es_url, output_dir):
    es = Elasticsearch(es_url)
    try:
        # make the bulk call, and get a response
        response = helpers.bulk(es, get_data(index_value, output_dir))
        info("\nRESPONSE:", response)
    except Exception as e:
        error("\nERROR:", e)
    rmtree(output_dir)
    # Remove log directory
    mkdir(output_dir)


def process_pcap_data(logs_dir, output_dir, suricata_config):
    args = ["suricata",
            "-k", "none",
            "-l", output_dir,
            "-r", logs_dir]
    if suricata_config:
        args.append("-c")
        args.append(suricata_config)
    check_call(args)


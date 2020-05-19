# suricataindex


## What is suricataindex?

It's a simply python cli/package to easily ingest pcap data into elasticsearch.

## How to install

### Install local with python

        git clone https://github.com/aucr/suricataindex/
        cd suricataindex
        pip install -r requirements.txt    
        python setup.py install        

 

         sur_cli.py --help
            Usage: sur_cli.py [OPTIONS]
            
              suricataindex Command line interface.
            
            Options:
              -f, --input_directory TEXT   The PCAP input directory.
              -o, --output_directory TEXT  Suricata output log directory.
              -c, --config_file TEXT       Output file directory.
              -e, --elastic_url TEXT       Elasticsearch URL value
              -i, --elastic_index TEXT     Elasticsearch URL value
              --help                       Show this message and exit.


### Install with Docker

        git clone https://github.com/aucr/suricataindex/
        cd suricataindex
        docker build . -t suricataindex

#### Run CLI with docker

        docker run -v /local/path/to/pcaps/:/opt/pcaps/ -it suricataindex -e http://elasticsearchurl:9200        

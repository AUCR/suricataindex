"""The suricataindex cli python package."""
# coding=utf-8
import click
from logging import DEBUG, ERROR, basicConfig
from suricataindex import __version__
from suricataindex.sur_index import process_pcap_data, index_to_es


def value_check(value, ctx):
    """Return boolean result from ctx parsing."""
    if not value or ctx.resilient_parsing:
        return True
    return False


def cli(ctx, param, debug):
    """Set command line debug level output to stdout."""
    if value_check(debug, ctx):
        return
    click.echo('Debug mode is %s' % ('on' if debug else 'off'))
    if debug:
        logging_level = DEBUG
        log_format = 'Process Time: %(asctime)s | %(message)s'
    else:
        logging_level = ERROR
        log_format = '%(message)s'
    basicConfig(level=logging_level, format=log_format, datefmt='%Y-%m-%d %H:%M:%S')


def print_version(ctx, param, value):
    """Print suricataindex version to stdout."""
    if value_check(value, ctx):
        return
    click.echo(str(__version__))
    ctx.exit()


@click.command()
@click.option("--input_directory", "-f",
              help="The PCAP input directory.",
              envvar='INPUT_DIRECTORY',
              default="/opt/pcaps")
@click.option("--output_directory", "-o",
              help="Suricata output log directory.",
              default="/opt/output/",
              envvar='OUTPUT_DIRECTORY')
@click.option("--config_file", "-c",
              help="Output file directory.",
              envvar='SURICATA_CONFIG_YAML')
@click.option("--elastic_url", "-e",
              help="Elasticsearch URL value",
              default="http://127.0.0.1:9200",
              envvar='ELASTICSEARCH_URL')
@click.option("--elastic_index", "-i",
              help="Elasticsearch URL value",
              default="suricata-",
              envvar='ELASTICSEARCH_INDEX')
def suricataindex_cli(input_directory, output_directory, config_file, elastic_url, elastic_index):
    """suricataindex Command line interface."""
    process_pcap_data(input_directory, output_directory, config_file)
    index_to_es(elastic_index, elastic_url, output_directory)


if __name__ == '__main__':
    suricataindex_cli()

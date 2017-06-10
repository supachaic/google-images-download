#!/usr/bin/env python3
import click
import os
from .google_images_download import main as gi_download
from .gi_from_file import search as search_from_file


@click.group()
def cli():
    pass


def validate_postiive_int(ctx, param, value):
    try:
        assert value >= 0
        return value
    except Exception as e:
        raise click.BadParameter('Error {}. Input must be positive integer.'.format(e))


@cli.command()
@click.argument('search-keywords', nargs=-1)
@click.option('--keywords', multiple=True, help='Additional keyword input.')
@click.option(
    '-nc', '--no-clobber', is_flag=True,
    help='Skip downloads that would download to existing files (overwriting them)')
@click.option(
    '--download-limit', type=int, default=1, callback=validate_postiive_int,
    help='Download limit. set 0 for no limit.')
@click.option(
    '--requests-delay', type=int, default=0, callback=validate_postiive_int,
    help='Delay between requests(seconds). set 0 for no delay')
@click.option(
    '--path', type=str, default=None,
    help='Directory to save download file.')

def download(search_keywords, keywords, download_limit, requests_delay, no_clobber, path):
    gi_download(search_keywords, keywords, download_limit, requests_delay, no_clobber, path)


@cli.command()
@click.argument('filepath', type=click.Path(exists=True))
def search(filepath):
    search_from_file(filepath)

#!/usr/bin/env python

import click
from dblib.querydb import querydb

#build a click group
@click.group()
def cli():
    """A simple CLI to query a SQL from Walmart database"""

#build a click command
@cli.command()
@click.option("--query", default="SELECT * FROM default.Walmart LIMIT 2", help="SQL query to execute")
def cli_query(query):
    """Execute a SQL query from Walmart database"""
    querydb(query)
  
  #run the CLI
if __name__ == "__main__":
    cli()


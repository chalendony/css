"""
Extracts text from the Phino web site to create an MVP catalog. The catalog is in json formatted
"""
import jsonlines

from selector.phineo.catalog import Catalog
import logging
import json
if __name__ == "__main__":
    catalog = Catalog(log_level=logging.INFO)
    cat = catalog.build()
    filename = '/Users/stewarta/repos/css/data/phineo.json'
    with open(filename, 'w') as f:
        f.write(json.dumps(cat))




"""
Extracts text from the Phino web site to create an MVP catalog. The catalog is in json formatted
"""


from selector.phineo.catalog import Catalog
import logging

if __name__ == "__main__":
    catalog = Catalog(log_level=logging.INFO)
    catalog.build()

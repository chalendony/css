# Crawls the Phineo web page produces json file containing metadata about social project

## Social Project Information

Name: Phineo

Web: https://www.phineo.org/projekte/

Language: German
 
## Schema 

The type and name of the metadata collected is as follows:

* id : string: unique identifier for the project
* name: string: name of the project
* tagline: string: one-liner statement about the project
* mission: string: first few sentences of the full text project description 
* location: string: city where the project is located
* geo_reach: sting: geographic locations serves by the project
* category : list : keywords describing the subject of the project 
* rating :  dictionary : Phineo-defined category and rating values assessing aspects of trustworthyness of project
NOTE: some not all rating captured by the crawler are correct. 
This metadata will be properly implemented in a future version of the code l 
 
   
* key_visual : string : action photo to highlight the project
* target_group: list: for whom the project is relevant
* home_page : string : the url for the project 
                
## Loading Catalog     
```buildoutcfg
 import json
 with open(filename) as json_file:
        data = json.load(json_file)
         .... 
```          
   
## TODOs

* read rating image with stars when all rating categories are not present 
* read rating image for bar char


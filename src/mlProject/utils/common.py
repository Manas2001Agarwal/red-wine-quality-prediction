import os
from box.exceptions import BoxValueError # type: ignore
import yaml
from mlProject import logger
import json
import joblib
from ensure import ensure_annotations # type: ignore
from box import ConfigBox # type: ignore
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml:Path) -> ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file {path_to_yaml} uploaded successfully")
            return content
    except BoxValueError:    
        raise ValueError("yaml_file_empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directory:list,verbose=True):
    for path in path_to_directory:
        os.makedirs(path,exist_ok=True)
        
        if verbose:
            logger.info(f"created directory at: {path}")
            
@ensure_annotations
def save_json(path:Path,data:dict):
    
    with open(path,"w") as f:
        json.dump(data,f,indent=4)
        
    logger.info(f"Data saved as json at path {path}")   
    
@ensure_annotations
def load_json(path:Path) -> ConfigBox:
    with open(path) as f:
         content = json.load(f)
         
    logger.info(f"json data at path {path} loaded") 
    return ConfigBox(content)

@ensure_annotations
def save_bin(data:Any,path:Path):
    joblib.dump(value=data,filename=path)
    logger.info(f"binary file saved at {path}")
    
@ensure_annotations
def load_bin(path:Path) -> Any:
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data


@ensure_annotations
def get_size(path: Path) -> str:
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"
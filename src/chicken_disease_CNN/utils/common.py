import os
import yaml
from src.chicken_disease_CNN.logging import logger
from src.chicken_disease_CNN.exception import CustomExeption
import json
import joblib
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64
import sys


def read_yaml(path_to_yaml: Path) -> ConfigBox:
    '''
    Read yaml file and returns
    
    Args:
        path to yaml file
    
    Raises:
        Custom exception

    Returns:
        ConfigBox- Config Box Type
        
    '''

    try:
        with open(path_to_yaml,'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f'yaml file: {yaml_file} loaded successfully')
            return ConfigBox(content)
        
    except Exception as e:
        raise CustomExeption(e,sys)


def create_directories(path_to_directories: list, verbose=True):
    
    '''
    create list of directories

    Args:
        path_to_directories list - list of path directories
        ignore_log (bool, optional) - ignore if multiple directories to be created, defalut to false
    '''
    
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f'Created directory at : {path}')



def get_size(path:Path) -> str:

    '''
    get size of file in KB

    Agrs:
        path(Path) : Path of File

    Returns:
        str: size in KB        
    '''
    size_in_kb = round(os.path.getsize(path)/1024)
    return f'~ {size_in_kb} KB'


def save_json(path: Path, data: dict):
    '''save json data
    
    Args:
        path(Path) - path to json file
        data(dict) - data to save in json file
    '''

    with open(path,'r') as f:
        json.dump(data,f,indent = 4)

    logger.info(f'json file save at {path}')


def load_json(path: Path) -> ConfigBox:
    """load json files data

    Args:
        path (Path): path to json file

    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file loaded succesfully from: {path}")
    return ConfigBox(content)



def save_bin(data: Any, path: Path):
    """save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")



def load_bin(path: Path) -> Any:
    """load binary data

    Args:
        path (Path): path to binary file

    Returns:
        Any: object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data


def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())    
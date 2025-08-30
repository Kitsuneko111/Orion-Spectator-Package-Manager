from typing import TypedDict, List, Optional, Dict, Union, Literal


class Repository(TypedDict):
    type: str
    url: str


class CameraPackage(TypedDict):
    name: str
    displayName: str
    version: str
    description: str
    main: str
    keywords: List[str]
    author: str
    defaultKeybind: str
    type: Optional[Literal["Camera", "Package"]]
    repository: Optional[Repository]
    license: Optional[str]
    dependencies: Optional[Dict[str, str]]
    optionalDependencies: Optional[Dict[str, str]]
    injectableDependencies: Optional[Dict[str, str]]
    devDependencies: Optional[Dict[str, str]]


class Package(TypedDict):
    name: str
    version: str
    description: str
    main: str
    keywords: List[str]
    author: str
    type: Optional[Literal["Camera", "Package"]]
    types: Optional[str]
    repository: Optional[Repository]
    license: Optional[str]
    dependencies: Optional[Dict[str, str]]
    optionalDependencies: Optional[Dict[str, str]]
    injectableDependencies: Optional[Dict[str, str]]
    devDependencies: Optional[Dict[str, str]]

from typing import TypedDict, List, Optional, Dict


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
    repository: Optional[Repository]
    license: Optional[str]
    dependencies: Optional[Dict[str, str]]
    devDependencies: Optional[Dict[str, str]]


class Package(TypedDict):
    name: str
    version: str
    description: str
    main: str
    keywords: List[str]
    author: str
    types: Optional[str]
    repository: Optional[Repository]
    license: Optional[str]
    dependencies: Optional[Dict[str, str]]
    devDependencies: Optional[Dict[str, str]]

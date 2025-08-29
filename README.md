# Orion Spectator Package Manager
An NPM and pip inspired package manager for the Orion Drift spectator package system

# Creating a Package

## Important Notes
The package implementation in Orion Drift only works downwards and by design prohibits overriding the directory with common methods such as `../` and `C:/...`.

This creates a safe environment, but requires developers to consider the restriction of being unable to import files from higher level directories.
```
example-package.luau   # Can be required
ExamplePackage/
├─ init.luau           # Can be required by example-package.luau
├─ main.luau           # Can be required by init.luau
├─ MySuperClass.luau   # CANNOT be required by MyClass.luau
└─ Utils/
   └─ MyClass.luau     # Can be required by main.luau
```
This also means that if multiple dependencies have duplicate dependencies it is impossible to de-dupe them currently.
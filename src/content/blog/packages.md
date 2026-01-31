---
title: "Packages in Julia"
date: 2024-05-22T19:59:56+02:00
draft: false
---

# Packages in Julia

When experimenting and writing new code a package structure seems to be an overkill, but as a project matures the package structure provides some advantages (imho).

First let us look how a package `MyPackage` looks like in Julia
```sh
> ls MyPackage
.git
.github/workflows
docs
src
test
.gitignore
LICENSE
Project.toml
Manifest.toml
README.md
```
### /src
```julia
ls /src
MyPackage.jl
```
its the folder where your code will live. In a newly initiallized package there will be always the file `MyPackage.jl`. This is the base file where the code lives or you import the code that lives in different files.
### /docs
the folder where the documentation will be generated automatically from the docstrings written in your code.
### /test
```sh
ls /test
runtests.jl
```
folder containing the tests of your code. Tests are snippets of code meant to *test* your functions. The basic file here is called `runtests.jl`, this is the file that will be executed by the CI. 
For example, say you have the following function in your package
```julia
function f(a, b)
    return a + b
end
```
then in `/test/runtests.jl`
```julia
using Test
using MyPackage

@test f(1, 1) == 2
@test f(1.0, 1.0) == 2.0
```
Tests are very important when you develop code. You can run them locally once you have activated your package environment with `]test`.

### /.github/workflows
this file will be generated for you automatically from `PkgTemplates.jl`. This will instruct GitHub (or any other git website) to run your tests in `/test` everytime you push a new version of your code.

### Project.toml & Manifest.toml
This project file together with `Manifest.toml` are central for the package manager of Julia (Pkg.jl). Project.toml describes your package on a high level, such as the author, the name, the version of the package, its depencencies and compatibility constraints. Moreover, it uses `uuid`'s (universally unique identifiers) for the project and dependencies. 

With this file the package dependencies are fully covered and whoever has this can run your code in a new environment without a problem (compare this to the package-hell of python). when you add a new package dependency with `]add NewPackage`, Julia updates these two files automatically.
Read more on these two files [here](https://pkgdocs.julialang.org/v1/toml-files/). 

### Activating your Package
Having all your code under a common roof enables you to use julia's builtin virtual environments which will allow julia to take care of package dependencies for you automatically. You can activate the environmet by doing
in the REPL
```sh
> cd MyPackage
> julia

(push "]")

(@v1.10) pkg> activate .
 Activating project at `path`
(MyPackage) pkg>

(push backspace)

>
```
(*when you push the button "]" the Julia REPL changes into Pkg mode*)
## Creating a Package
Usually the workflow of creating a package would be very tedious if you had to write the CI files yourself yadayada. But! There exists a package that does everything for you, `PkgTemplates.jl`. Add it in your Julia REPL and then do
```julia
using PkgTemplates
t=Template(;
           user="svretina", #username
           dir="/home/svretina/Codes/PhD/", # directory where your package will be
           authors="Stamatis Vretinaris", # your name
           julia=v"1.10", # julia version
           plugins=[
               !CompatHelper,
               License(; name="GPL-3.0+"), # choose a License you like
               Git(; manifest=true, ssh=true), # This choise is for Github
               GitHubActions(; # this will enable CI
                   destination="CI.yml", 
                   linux=true,
                   osx=false,
                   windows=false,
                   x64=true,
                   x86=false,
                   coverage=true,
                   extra_versions=["1.10", "nightly"]),
               Codecov(), # coverage of your code for tests
               Documenter{GitHubActions}(),
               Develop(),
           ],
       )
t("MyPackage")
```
Now in your `dir` you should have a folder named `MyPackage`
```sh
> ls dir/MyPackage
drwxr-xr-x. 24 svretina svretina 4.0K May 25 19:43 ..
-rw-r--r--.  1 svretina svretina   62 May 25 19:43 .gitignore
drwxr-xr-x.  3 svretina svretina 4.0K May 25 19:43 .github
-rw-r--r--.  1 svretina svretina  35K May 25 19:43 LICENSE
-rw-r--r--.  1 svretina svretina  574 May 25 19:43 README.md
drwxr-xr-x.  2 svretina svretina 4.0K May 25 19:43 src
drwxr-xr-x.  2 svretina svretina 4.0K May 25 19:43 test
-rw-r--r--.  1 svretina svretina  231 May 25 19:43 Project.toml
-rw-r--r--.  1 svretina svretina  186 May 25 19:44 Manifest.toml
drwxr-xr-x.  7 svretina svretina 4.0K May 25 19:44 .
drwxr-xr-x.  3 svretina svretina 4.0K May 25 19:44 docs
drwxr-xr-x.  7 svretina svretina 4.0K May 25 19:44 .git
```
Great success! (*preferably read in Borat voice*)

```sh
> cat src/MyPackage.jl
module MyPackage

# Write your package code here.

end

> cat Project.toml
name = "MyPackage"
uuid = "d8d250fd-c730-497c-b513-464b22078937"
authors = ["Stamatis Vretinaris"]
version = "1.0.0-DEV"

[compat]
julia = "1.10"

[extras]
Test = "8dfed614-e22c-5e08-85e1-65c5234f0b40"

[targets]
test = ["Test"]
```



## Connecting your Package to GitHub
You need to create a new repo in GitHub online. Make sure to not forget to add `.jl` to the name of your package, or make sure you have the same name in your local folder and in your git repo online.

Usually you would have to do
```sh
> git init
> git commit -m "first commit"
> git branch -M master
> git remote add origin git@github.com:svretina/MyPackage.git
```
but this has been taken care for you by `PkgTemplates.jl`. 
```sh 
> git config --get remote.origin.url
git@github.com:svretina/MyPackage.jl.git
```
It's already configured! You only need to push your files to the repo@GitHub!
```sh
> git push -u origin master
Enumerating objects: 23, done.
Counting objects: 100% (23/23), done.
Delta compression using up to 8 threads
Compressing objects: 100% (19/19), done.
Writing objects: 100% (23/23), 15.73 KiB | 2.25 MiB/s, done.
Total 23 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To github.com:svretina/MyPackage.jl.git
 * [new branch]      master -> master
branch 'master' set up to track 'origin/master'.
```

## Some Git shugah
When you browse all of these cool libraries they have these nice colorfull buttons saying `docs|stable` or `docs|dev` or `CI|passing` etc. `PkgTemplates.jl` gots your back and you automatically have these nice thingies in your README.md file that was generated.

# MyPackage

[![Stable](https://img.shields.io/badge/docs-stable-blue.svg)](https://svretina.github.io/MyPackage.jl/stable/)
[![Dev](https://img.shields.io/badge/docs-dev-blue.svg)](https://svretina.github.io/MyPackage.jl/dev/)
[![Build Status](https://github.com/svretina/MyPackage.jl/actions/workflows/CI.yml/badge.svg?branch=master)](https://github.com/svretina/MyPackage.jl/actions/workflows/CI.yml?query=branch%3Amaster)
[![Coverage](https://codecov.io/gh/svretina/MyPackage.jl/branch/master/graph/badge.svg)](https://codecov.io/gh/svretina/MyPackage.jl)

More on namespaces and code tips for julia and packages in the next post.

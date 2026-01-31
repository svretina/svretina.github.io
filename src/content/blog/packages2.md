---
title: "Packages2"
date: 2024-06-01T20:30:29-04:00
draft: false
---

...now that we created our first package, let's discover some 
of the neat things you can do with them, that would be impossible
otherwise.

Let's recall what your workflow would look like if one would use scripts.
Say you wrote some functions (you should write functions and not just code in your 
files, because the compiler cannot optimize your code) in a file called `script.jl`.

```julia
> include("script.jl")
```
This will evaluate the contents of your script in the global scope on `Main`. Now you can 
call the functions you wrote in `script.jl` as
```julia
script.func()
```
Now you found a bug in your function `func` and you update your script, you hit save, you 
execute again `func`, but nothing changed! Bummer... you need to hit again the `include` command.
Obviously this easily gets annoying when you develop your code. Brace yourself, there is a solution!
Some holy person ([Tim](https://github.com/timholy)), wrote a package so that you don't have to re`include` your stuff all the time,
it's called [`Revise.jl`](https://timholy.github.io/Revise.jl/stable/).

```julia
using Revise
includet("script.jl")
```
and now your changes are being tracked by `Revise.jl` and whenever you update your code, it is automatically
updated in your REPL session. 

The nice feature of `Revise.jl` is that if you activate a package environment, it automatically tracks all
the changes that happen in all of your `.jl` files! Revise is powerful but it also has its [limitations](https://timholy.github.io/Revise.jl/stable/limitations/), for example
you cannot redefine global constants or types. Since it is so essential to our workflow, let's add it
to our `startup.jl` so that you don't have to manually import it in every REPL session. 

Open the file `.julia/config/startup.jl` and add
```julia
try
    @eval using Revise
catch e
    @warn "Error initializing Revise" exception=(e, catch_backtrace())
end
```
This will increase the initial time to start your REPL by a fraction, but by default, Revise will be loaded
and you only have to activate your package environment and you are ready to work.


Let's go back to our package `MyPackage.jl` and explore the package manager of julia.
```julia
(@v1.10) pkg> activate .
(MyPackage) pkg> 
## backspace
> using MyPackage
> 
```
obviously nothing happened since the package is empty. Note that we used `using`, there is another option, `import`. 
We will discuss their differences in the next post about namespaces.

```julia
(MyPackage) pkg> status
Project MyPackage v1.0.0-DEV
Status `~/Codes/PhD/MyPackage/Project.toml` (empty project)
(MyPackage) pkg> add LinearAlgebra
    Updating registry at `~/.julia/registries/General.toml`
   Resolving package versions...
    Updating `~/Codes/PhD/MyPackage/Project.toml`
  [37e2e46d] + LinearAlgebra
    Updating `~/Codes/PhD/MyPackage/Manifest.toml`
  [56f22d72] + Artifacts
  [8f399da3] + Libdl
  [37e2e46d] + LinearAlgebra
  [e66e0078] + CompilerSupportLibraries_jll v1.1.1+0
  [4536629a] + OpenBLAS_jll v0.3.23+4
  [8e850b90] + libblastrampoline_jll v5.8.0+1
```
with `add` you can add packages that are listed in the General Registry. You can install packages from a git repo by doing
```julia
(MyPackage) pkg> add https://github.com/JuliaArrays/StaticArrays.jl.git
     Cloning git-repo `https://github.com/JuliaArrays/StaticArrays.jl.git`
    Updating git-repo `https://github.com/JuliaArrays/StaticArrays.jl.git`
   Resolving package versions...
    Updating `~/Codes/PhD/MyPackage/Project.toml`
  [90137ffa] + StaticArrays v1.9.4 `https://github.com/JuliaArrays/StaticArrays.jl.git#master`
    Updating `~/Codes/PhD/MyPackage/Manifest.toml`
  [aea7be01] + PrecompileTools v1.2.1
  [21216c6a] + Preferences v1.4.3
  [90137ffa] + StaticArrays v1.9.4 `https://github.com/JuliaArrays/StaticArrays.jl.git#master`
  [1e83bf80] + StaticArraysCore v1.4.2
  [ade2ca70] + Dates
  [de0858da] + Printf
  [9a3f8284] + Random
  [ea8e919c] + SHA v0.7.0
  [fa267f1f] + TOML v1.0.3
  [4ec0a83e] + Unicode
```
and if you want the bleading edge version of a library that is already listed in the General Registry, then simply do
```julia
(MyPackage) pkg> add PkgName#master
    Updating git-repo `https://github.com/JuliaSIMD/Polyester.jl.git`
   Resolving package versions...
    Updating `~/Codes/PhD/MyPackage/Project.toml`
 ...
```
```julia
(MyPackage) pkg> st
Project MyPackage v1.0.0-DEV
Status `~/Codes/PhD/MyPackage/Project.toml`
  [f517fe37] Polyester v0.7.14 `https://github.com/JuliaSIMD/Polyester.jl.git#master`
  [90137ffa] StaticArrays v1.9.4 `https://github.com/JuliaArrays/StaticArrays.jl.git#master`
  [37e2e46d] LinearAlgebra
```
everytime you will add a package, Julia will resolve the versions. You can update your packages with
```julia
(MyPackage) pkg> up
    Updating registry at `~/.julia/registries/General.toml`
    Updating git-repo `https://github.com/JuliaArrays/StaticArrays.jl.git`
    Updating git-repo `https://github.com/JuliaSIMD/Polyester.jl.git`
  No Changes to `~/Codes/PhD/MyPackage/Project.toml`
  No Changes to `~/Codes/PhD/MyPackage/Manifest.toml`
        Info We haven't cleaned this depot up for a bit, running Pkg.gc()...
      Active manifest files: 37 found
      Active artifact files: 281 found
      Active scratchspaces: 6 found
     Deleted 70 package installations (52.213 MiB)
     Deleted 7 artifact installations (457.237 MiB)
     Deleted 2 scratchspaces (5.855 KiB)
```
and if you don't need anymore a dependecy, you can remove it with
```julia
(MyPackage) pkg> rm Polyester
    Updating `~/Codes/PhD/MyPackage/Project.toml`
  [f517fe37] - Polyester v0.7.14 `https://github.com/JuliaSIMD/Polyester.jl.git#master`
    Updating `~/Codes/PhD/MyPackage/Manifest.toml`
  [79e6a3ab] - Adapt v4.0.4
  [4fba245c] - ArrayInterface v7.10.0
  [62783981] - BitTwiddlingConvenienceFunctions v0.1.5
  [2a0fbf3d] - CPUSummary v0.2.5
  [fb6a15b2] - CloseOpenIntervals v0.1.12
  [34da2185] - Compat v4.15.0
  [adafc99b] - CpuId v0.3.1
  [615f187c] - IfElse v0.1.1
  [10f19ff3] - LayoutPointers v0.1.15
  [d125e4d3] - ManualMemory v0.1.8
  [f517fe37] - Polyester v0.7.14 `https://github.com/JuliaSIMD/Polyester.jl.git#master`
  [1d0040c9] - PolyesterWeave v0.2.1
  [ae029012] - Requires v1.3.0
  [94e857df] - SIMDTypes v0.1.0
  [aedffcd0] - Static v0.8.10
  [0d7ed370] - StaticArrayInterface v1.5.0
  [7792a7ef] - StrideArraysCore v0.5.6
  [8290d209] - ThreadingUtilities v0.5.2
  [2a0f44e3] - Base64
  [d6f4376e] - Markdown
  [9e88b42a] - Serialization
  [2f01184e] - SparseArrays v1.10.0
  [4607b0f0] - SuiteSparse
  [cf7118a7] - UUIDs
  [bea87d4a] - SuiteSparse_jll v7.2.1+1
(MyPackage) pkg> st
Project MyPackage v1.0.0-DEV
Status `~/Codes/PhD/MyPackage/Project.toml`
  [90137ffa] StaticArrays v1.9.4 `https://github.com/JuliaArrays/StaticArrays.jl.git#master`
  [37e2e46d] LinearAlgebra
```


Next stop, namespaces and some code organizing

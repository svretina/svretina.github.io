---
title: "Introduction to SIMD in Julia"
date: 2024-01-01T19:59:56+02:00
draft: false
---

## SIMD instructions in Julia

[SIMD](https://en.wikipedia.org/wiki/Single_instruction,_multiple_data) stands for “single instruction, multiple data” and is a class of parallel computers in Flynn's taxonomy. It describes computers with multiple processing elements that perform the same operation on multiple data points simultaneously.

In order to take advantage of the modern CPU's potential it is essential to utilize SIMD instructions. Lets check if our CPU supports these features. On a UNIX machine 

```sh
lscpu | grep avx
lscpu | grep sse
```

```julia
function func 
    return 0
end
```

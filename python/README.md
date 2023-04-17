# README

## add module **calculator**

```
bazel test --enable_bzlmod //calculator/...
```

## Add third party module **python_web**

Add requirement **Flask** by:

- create `requirement.in`
- create an empty file `requirement_lock.txt` (used in `pip.parse` in `MODULE.bazel`)
- load pip rule `compile_pip_requirements`
- use `compile_pip_requirements` to generate `requirement_lock.txt` from `requirement.in` (see command below)

```
bazel run --enable_bzlmod //third_party:requirements.update
```

## Add module **python_web** based on **calculator** and **Flask**

Specify the visibility of **calculator** for **python_web**.

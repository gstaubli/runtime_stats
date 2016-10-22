# Runtime Stats for Functions
Python decorator function to track runtime stats on function calls

# Example
```
@runtime_stats()
def self_mult(n):
    sleep(0.2)
    return n*n

print(self_mult(10)) # => 100
print(self_mult(7)) # => 49
print(self_mult.get_func_runtime_stats()) # => {'total_time': 401.668, 'avg': 200.834, 'func_uid': 4302206808, 'func_name': 'self_mult', 'min': 200.445, 'max': 201.223, 'total_calls': 2}
```

# Usage
Decorate a function with `@runtime_stats()` to keep track of that function's runtime (min, max, avg, total_calls, and total_time)

# Compatibility
Tested compatible with Py2.7 and Py3, but this code is provided as is with no warranty or guarantee, implied or explicit.

# More Information
Please see my blog post here: http://garrens.com/blog/2016/10/21/runtime-stats-for-functions-python-decorator/
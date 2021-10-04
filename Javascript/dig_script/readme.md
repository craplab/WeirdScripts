Gets the target value in a nested JSON object, based on the given key.

- Use the `in` operator to check if `target` exists in `obj`.
- If found, return the value of `obj[target]`.
- Otherwise use `Object.values(obj)` and `Array.prototype.reduce()` to recursively call `dig` on each nested object until the first matching key/value pair is found.

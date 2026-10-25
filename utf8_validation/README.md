# UTF-8 Validation

`validUTF8(data)` returns `True` if a list of integers (one byte each, only
the 8 least significant bits are used) is a valid UTF-8 encoding, else
`False`.

A UTF-8 character is 1 to 4 bytes long:

| Bytes | Leading byte | Continuation bytes |
|-------|--------------|--------------------|
| 1     | `0xxxxxxx`   | none               |
| 2     | `110xxxxx`   | 1 × `10xxxxxx`     |
| 3     | `1110xxxx`   | 2 × `10xxxxxx`     |
| 4     | `11110xxx`   | 3 × `10xxxxxx`     |

## Files

- `0-validate_utf8.py`: the `validUTF8(data)` function
- `0-main.py`: test file

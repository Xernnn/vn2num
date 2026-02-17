# Vietnamese Number Converter

This simple Python script converts Vietnamese number strings (text) into actual integer values. It's designed to be lightweight, fast, and 100% accurate for standard Vietnamese numbers.

## What it does

It takes a string like `"một tỷ hai trăm triệu"` and turns it into `1200000000`.

I built it using a recursive parser, so it handles:
- **Standard numbers**: `hai mươi mốt` (21), `năm trăm` (500)
- **Special words**: Correctly handles `mốt`, `tư`, `lăm`, `linh/lẻ`
- **Large numbers**: Supports unlimited magnitude (e.g., `tỷ tỷ` - quintillions)
- **Robustness**: Handles extra spaces and capitalization automatically

## How to use it

I kept it super simple. Just import the function and use it:

```python
from num import tonum

print(tonum("một trăm hai mươi ba")) 
# Output: 123

print(tonum("hai mươi ba tỷ tám trăm sáu mươi triệu bảy mươi ba nghìn tám trăm lẻ sáu"))
# Output: 23860073806
```

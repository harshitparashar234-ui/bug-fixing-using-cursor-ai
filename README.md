# bug-fixing-using-cursor-ai
Identifying and fixing Python programming errors with assistance from Cursor AI.

# Bug Fixing Using Cursor AI

## Overview
This project demonstrates how a Python bug can be identified and corrected with assistance from Cursor AI.

## Files
- `buggy_program.py` - Contains an incorrect loop boundary that causes an IndexError.
- `fixed_program.py` - Contains the corrected program.

## Bug Identified
The original loop uses `range(len(numbers) + 1)`. This attempts to access an index beyond the end of the list.

## Solution
The corrected program iterates directly over the list values. This avoids invalid index access and calculates the average correctly.

## Expected Output
Average: 30.0

## Technologies Used
- Python 3
- Cursor AI (AI-assisted debugging)

## How to Run
```bash
python buggy_program.py
python fixed_program.py
```

Note: The buggy file is expected to raise an IndexError. Run the fixed file to see the correct output.

## Author
Harshit parashar


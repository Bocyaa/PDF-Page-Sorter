# PDF Page Sorter

A Python script to reorder pages in a PDF file based on a specified order.

## Requirements

- Python 3.x
- PyPDF2 library

## Installation

1. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
```

2. Install required package:

```bash
pip install PyPDF2
```

## Usage

1. Place your PDF file in the same directory as the script
2. Modify the `mixed_order` list in `script.py` to match your PDF's page order
3. Run the script:

```bash
python script.py
```

### Example

```python
mixed_order = [1, 47, 48, 53]  # Represents current page numbers in your PDF
sort_pdf("input.pdf", "output.pdf", mixed_order)
```

This will:

- Take pages from `input.pdf`
- Reorder them based on the numbers in `mixed_order`
- Save the sorted result to `output.pdf`

## Features

- Maintains original order for duplicate page numbers
- Handles PDFs with non-sequential page ordering
- Creates a new PDF file without modifying the original

## Use Cases

- Fixing incorrectly scanned documents
- Reorganizing PDF chapters or sections
- Restoring proper page sequence in merged PDFs
- Creating custom page arrangements for printing

## Notes

- Page numbers in `mixed_order` start from 1
- The script preserves the original PDF quality
- Make sure you have enough disk space for both input and output files

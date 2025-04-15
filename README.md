# PDF Page Sorter

A Python script to reorder pages in a PDF file based on a specified order.

## 🧠 Why This Script Exists (aka The Origin Story No One Asked For)

I had to buy access to the learning app from my driving school in Germany €100 a year (considering it’s basically just a PowerPoint with some buttons).
So I took a bunch of screenshots of the material pages and turned them into a PDF. But the pages ended up in the wrong order, which made studying kind of impossible.
Instead of manually fixing it (because I have other things to procrastinate with), I wrote this script. 
It lets you reorder PDF pages however you want. Now it’s reusable, fast, and saves you from scrolling through a mess.
It’s not fancy, but it works. Like a used Toyota.

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

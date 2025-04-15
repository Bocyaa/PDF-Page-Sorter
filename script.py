from PyPDF2 import PdfReader, PdfWriter

def sort_pdf(input_pdf, output_pdf, order):
    """
    Reorders the pages of input_pdf based on the ascending order
    of the provided list 'order'. Each element in 'order' corresponds
    to a page in the original PDF (where index 0 is the first page).
    
    For duplicate page numbers, the original order is maintained.
    """
    # Create a list of indices and sort them by their corresponding page number.
    indices = list(range(len(order)))
    indices_sorted = sorted(indices, key=lambda x: (order[x], x))
    
    reader = PdfReader(input_pdf)
    writer = PdfWriter()
    
    # Add pages to the writer in the sorted order.
    for idx in indices_sorted:
        writer.add_page(reader.pages[idx])
    
    # Write out the sorted PDF.
    with open(output_pdf, 'wb') as f:
        writer.write(f)

if __name__ == '__main__':
    # This list represents the actual (mixed) order of page numbers in target.pdf.
    # To reuse the script with another PDF, simply adjust this list.
    mixed_order = [
        1, 47, 48, 53, 76, 74, 78, 64, 72, 73, 60, 70, 63, 65, 64,
        59, 62, 71, 61, 56, 61, 58, 57, 75, 68, 54, 69, 55, 86, 111, 108, 103
    ]
    
    sort_pdf("target.pdf", "target-sorted.pdf", mixed_order)

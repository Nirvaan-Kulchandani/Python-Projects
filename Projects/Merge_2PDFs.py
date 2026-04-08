# 7️⃣ PDF Merger	         PyPDF2	                Merge multiple PDF files

import PyPDF2


def merge_Pdf(pdf_files, merged_file):
    '''Merge multiple PDF files into one PDF file.'''

    pdf_writer = PyPDF2.PdfWriter()

    for file in pdf_files:
        try:
            pdf_reader = PyPDF2.PdfReader(file)
            for page in range(len(pdf_reader.pages)):
                pdf_writer.add_page(pdf_reader.pages[page])

        except Exception:
            print(f"Error while reading {file}. Please check if the file exists and is a valid PDF.")
    try:
        with open(merged_file, 'wb') as mf:
            pdf_writer.write(mf)

        print(f"Successfully merged {len(pdf_files)} PDF files into {merged_file}.")
    
    except Exception:
        print(f"Error while writing to {merged_file}. Please check if you have write permissions.")


# pdf_files = ['file1.pdf', 'file2.pdf']
# merge_Pdf(pdf_files, 'merged.pdf')

#pdfsort
##Pre-alpha

###Generate a new pdf based on a list of pages from an input pdf
`pdfsort generate input_pdf, output_pdf, pages`

###Split a pdf from start_page to end_page by an increment and create an output pdf.
####This has helped me split large pdfs of canvassing data.
`pdfsort split input_pdf, output_pdf, first_page, last_page, increment`

###Rotate all pages in a pdf by 180 degrees and create an output pdf. Can optionally specify degrees.
`pdfsort rotate_all input_pdf, output_pdf [, degrees]``

###Rotate a given list of pages and create an output pdf.
`pdfsort rotate_pages input_pdf, output_pdf, pages, degrees`

# pdfsort
## Pre-alpha

#### Installation in a python virtual environment
Run in a virtualenv
1. clone this repo
1. `cd pdfsort`
1. `virtualenv venv`
1. `. venv/bin/activate`
1. `pip install --editable .`

To turn off virtualenv
1. `deactivate`

#### Generate a new pdf based on a list of pages from an input pdf

`pdfsort generate input_pdf, output_pdf, pages`

#### Split a pdf from start_page to end_page by an increment and create an output pdf.
This has helped me split large pdfs of canvassing data.

`pdfsort split input_pdf, output_pdf, first_page, last_page, increment`

Note: This currently relies on `pdfjam`. This will be changed in the near future.

#### Rotate all pages in a pdf by 180 degrees and create an output pdf. Can optionally specify degrees.

`pdfsort rotate_all input_pdf, output_pdf [, degrees]`

#### Rotate a given list of pages and create an output pdf.

`pdfsort rotate_pages input_pdf, output_pdf, pages, degrees`

#### KED sort
`pdfsort kedsort --input file.pdf --tracker_pages 1,2,3 --sign_in_pages 24,25,26 --canvass_pages 4-23 --increment 4`

This will create

* [input file name]-tracker.pdf (if you use the --tracker_pages option)
* [input file name]-sign_in.pdf (if you use the --sign_in_pages option)
* [input file name]-canvass.pdf (if you use the --canvass_pages option)
* 1-[input file name]-canvass.pdf (if you use the --increment option)

# This file is part of pylabels, a Python library to create PDFs for printing
# labels.
# Copyright (C) 2012, 2013, 2014 Blair Bonnett
#
# pylabels is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# pylabels is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# pylabels.  If not, see <http://www.gnu.org/licenses/>.

# Very basic test script to generate labels, based on the PyLabels library.

import labels
from reportlab.lib.units import mm
from reportlab.graphics import shapes
from reportlab.graphics.barcode import qr

# Create a portrait label for use with Zebra LP 2844 (101.6mm x 101.6mm) sheets with 1 columns and 1 row of
# labels. Each label is 90mm x 25mm with a 1mm rounded corner. The margins are
# automatically calculated.
specs = labels.Specification(101.6, 101.6, 1, 1, 100, 100, corner_radius=1)

# Create a function to draw each label. This will be given the ReportLab drawing
# object to draw on, the dimensions (NB. these will be in points, the unit
# ReportLab uses) of the label, and the object to render.
def draw_label(label, width, height, obj):
    # Just convert the object to a string and print this at the bottom left of
    # the label.
    label.add(shapes.String(5, 260, "MK Makerspace Project", fontName="Helvetica", fontSize=20))
    label.add(shapes.String(5, 240, "Inventory & Storage System", fontName="Helvetica", fontSize=20))
    label.add(shapes.String(5, 215, "Owner: Alan Hacker", fontName="Helvetica", fontSize=15))
    label.add(shapes.String(5, 200, "Removal date: 31/12/2099", fontName="Helvetica", fontSize=15))
    label.add(shapes.String(5, 185, "Approved By: Hackerman Jones", fontName="Helvetica", fontSize=15))
    qr_code = qr.QrCodeWidget("https://data.mkmakerspace.co.uk", barLevel = 'H', 
    	barHeight = 200, barWidth = 200)
    label.add(qr_code)

# Create the sheet.
sheet = labels.Sheet(specs, draw_label, border=False)

# We can embed URLs in the QR codes too
sheet.add_label("")


# Save the file and we are done.
sheet.save('label.pdf')
print("{0:d} label(s) output on {1:d} page(s).".format(sheet.label_count, sheet.page_count))
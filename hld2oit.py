#!/usr/bin/python
# hld2oit.py:
#
# Description: 	Tool intended to convert HLD format files to OIT format
#
#
# Input Parameters:
#		HLD File: Location to the HLD excel file
#
# Output: OIT excel file
#
# Example:
#		hld2oit.py "HLD_USC_AFF_vMCC_V.1.0.2.xls"
#
# Database:	N/A
#
# Created by : Daniel Jaramillo
# Creation Date: 04/01/2019
# Modified by:     Date:
# All rights(C) reserved to Teoco
###########################################################################
import sys
import os
import pandas as pd
from openpyxl import load_workbook
from LoggerInit import LoggerInit




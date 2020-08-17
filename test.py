"""Outputs allowable building height & number of stories
   above grade plane, and allowable area factor"""

# from pyrevit import revit, DB
# from pyrevit import forms
# from pyrevit import script
from IBC import allowable_height, allowable_stories, allowable_area
import sys

# logger = script.get_logger()
# output = script.get_output()

print("Python version:")
print(sys.version)

max_height = allowable_height('A', '1', 'NS', 'V-B')
print("Max height for Group A-1, NS, Type V-B: " + str(max_height))

max_height = allowable_height('I', '4', 'S', 'IV-HT')
print("Max height for Group I-4, S, Type IV-HT: " + str(max_height))

max_stories = allowable_stories('A', '1', 'NS', 'V-B')
print("Max stories for Group A-1, NS, Type V-B: " + str(max_stories))

max_stories = allowable_stories('I', '4', 'S', 'IV-HT')
print("Max stories for Group I-4, S, Type IV-HT: " + str(max_stories))

max_area = allowable_area('A', '1', 'NS', 'V-B')
print("Max area for Group A-1, NS, Type V-B: " + str(max_stories))

# Check that 1 Condition and 1 Condition 2 are translated properly
max_area = allowable_area('I', '1 Condition 1', 'S1', 'V-A')
print("Max area for Group I-1 Condition 1, S, Type IV-HT: " + str(max_stories))
max_area = allowable_area('I', '1 Condition 2', 'S1', 'V-A')
print("Max area for Group I-1 Condition 2, S, Type IV-HT: " + str(max_stories))

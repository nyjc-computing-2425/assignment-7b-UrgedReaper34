# Built-in imports
import math

# Your code below
GRADE = {}
GRADEinit = {
  "70": "A",
  "60": "B",
  "55": "C",
  "50": "D",
  "45": "E",
  "40": "S", 
}
GRADEinit_items = list(GRADEinit.keys())

currentGrade = "U"
i = 0
while(i <= 100):
  if GRADEinit_items.count(str(i)) == 1:
    currentGrade = GRADEinit[str(i)]
  GRADE[i] = currentGrade
  i += 1
  
def read_testscores(filename):
  with open(filename, "r") as f:
    studentdata = []
    rawdata = f.readlines()
    headers = rawdata.pop(0)
    headers = headers.rstrip("\n").split(",")
    for row in rawdata:
      rowDict = {}
      row = row.rstrip("\n").split(",")
      
      # Remove the first 2  elements, while storing them as class and name
      rowDict["class"] = row.pop(0)
      rowDict["name"] = row.pop(0)
      # We are now left with only scores, convert all scores to iints
      row = list(map(int, row))
      # Let's calculate the overall score now
      overall = (row[0]/30 * 15) + (row[1]/40 * 30) + (row[2]/80 * 35) + (row[3]/30 * 20)

      rowDict["overall"] = math.ceil(overall)
      rowDict["grade"] = GRADE[rowDict["overall"]]
      studentdata.append(rowDict)
    return studentdata

def analyze_grades(studentdata):
  """
    Returns a dict representing the count of each grade for each class, i.e. how many A, B, C, D, E, S and U each class has.

    Parameters:
      studentdata: nested list
        a list of dicts with student data
    Returns:
      analysis: nested dict
        a dict of dicts with corresponding grades
  """
  analysis = {}
  for student in studentdata:
    studentClass = analysis.setdefault(student["class"], {
      "A": 0,
      "B": 0,
      "C": 0,
      "D": 0,
      "E": 0,
      "S": 0,
      "U": 0,
    })
    analysis[student["class"]][student["grade"]] += 1
    
  return analysis

# print(analyze_grades(read_testscores("testscores.csv")))

#!/usr/bin/env python
import jinja2

class Emp: pass

with open("resume.html.in") as f:
    temp = jinja2.Template(f.read())




contact_lines = [
    "16234 SW O'Neill Court",
    "Tigard, OR 97223",
    "(503) 720-6499",
    "charlesrymal@gmail.com"]

emp0 = Emp()
emp0.title = "Graduate Research Assistant"
emp0.duration = "September 2012 to September 2014"
emp0.employer  = "Oregon State University"
emp0.location = "Corvallis, OR"

emp0.desc_cs = [
        "Title of research - Numerical Design of a High-Flux Microchannel Solar Receiver",
        "Worked with faculty and other students to design microchannel solar receivers",
        "Project was funded by the DOE SunShot Initiative",
        "Performed numerical simulations of heat transfer and fluid flow using commercial software",
        "Used C, Java, Python, Bash scripts, Make, and Tcl for automation, customization, and data analysis of numerical simulations",
        ]

emp0.desc_me = [
"Title of research - Numerical Design of a High-Flux Microchannel Solar Receiver",
#"Project was funded by the US Dept. of Energy SunShot Initiative",
"Worked with faculty and other students to design microchannel receivers for "
"solar thermal power production",
"Performed numerical simulations of heat transfer and fluid flow using "
"commercial software: Ansys Fluent and StarCCM+",
"Assessed pressure drop, thermal efficiency, structural integrity and flow distribution",
"Published two conference papers for the ASME conference on Energy Sustainability",
]

emp1 = Emp()
emp1.title = "MECOP Intern"
emp1.duration = "March 2011 to September 2011"
emp1.employer = "Allied Systems Company"
emp1.location = "Sherwood, OR"

emp1.desc_cs = [
"Managed several plant-wide manufacturing engineering projects with significant benefit for the company",
"Designed various tooling, particularly welding fixtures, with consideration "
"for ease of use and manufacturability",
"Worked extensively with design engineers, manufacturing engineers, machinists, welders, and many others",
]

emp1.desc_me = emp1.desc_cs
       
emp2 = Emp()
emp2.title = "MECOP Intern"
emp2.duration = "March 2010 to September 2010"
emp2.employer = "ATI Wah Chang"
emp2.location = "Albany, OR"

emp2.desc_cs = [
        "Designed material handling equipment for various applications",
        "Performed stress analysis calculations as well as FEA analysis on equipment designs",
        "Designed creative mechanical solutions to issues with existing machinery",
        "Worked with area operators, supervisors, mechanical engineers, and outside fabrication contractors",
        ]
emp2.desc_me = emp2.desc_cs


with open("resume.html","w") as f:
    f.write(temp.render(contact_lines=contact_lines, emp=[emp0,emp1,emp2]))



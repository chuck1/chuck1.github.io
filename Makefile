
all:
	python generator/resume_to_source.py $(GIT_HOME)/personal/resume1/resume.txt
	
	python generator/main.py


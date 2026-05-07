from pyscript import document  # type: ignore

# list of classmates
classmates = [
    "Ashley Kirsten Y. Santos from Topaz and my favorite subject is Science",
    "Marley Summer R. Manese from Topaz and my favorite subject is Social Studies",
    "Riso P. Salapunen from Topaz and my favorite subject is Music",
    "Vic Carlo Gorom from Topaz and my favorite subject is Math",
  
]

def add_classmate(event=None):
    output = document.getElementById("classmatefav")

    if output.innerText == "":
        names = ""
        for classmate in classmates:
            names += classmate + "\n"
        output.innerText = names
    else:
        output.innerText = ""  

def add_you(e):
    name = document.getElementById("classmateInput").value
    section = document.getElementById("classmateInput1").value
    subject = document.getElementById("classmateInput2").value

    if name and section and subject:
        classmates.append(f"{name} from {section} and my favorite subject is {subject}")
        document.getElementById("classmateInput").value = "" 
        document.getElementById("classmateInput1").value = ""
        document.getElementById("classmateInput2").value = ""

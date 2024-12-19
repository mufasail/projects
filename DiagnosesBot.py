welcome_prompt = """Welcome doctor, what would you like to do today?\n
- To list all patients, press 1\n
- To run a new diagnosis, press 2\n
- To quit, press q\n"""

name_prompt = "What is the patient's name?\n"
appearance_prompt = "How is the patient's general appearance?\n - 1: Normal appearance\n - 2: Irritable or lethargic\n"

eye_prompt = "How is the patient's eyes?\n - 1: Eyes normal or slightly sunken \n - 2: Eyes very sunken\n"
skin_prompt = "How is the patient's skin?\n - 1: Skin normal or slightly sunken \n - 2: Skin very sunken\n"

severe_dehydration = "Severe dehydration"
some_dehydration = "Some dehydration"
no_dehydration = "No dehydration"

patients_and_diagnosis = [
    "Mike: Severe dehydration",
    "Alon: No dehydration",
    "Taylor: Some dehydration"
]


def list_patients():
    for patient in patients_and_diagnosis:
        print(patient)


def save_new_diagnosis(name, diagnosis):
    final_diagnosis = name + ": " + diagnosis
    patients_and_diagnosis.append(final_diagnosis)
    print("Final Diagnosis: ", final_diagnosis, "\n")


def assess_eyes(eyes):
    if eyes == "1":
        return no_dehydration
    elif eyes == "2":
        return severe_dehydration


def assess_skin(skin):
    if skin == "1":
        return some_dehydration
    elif skin == "2":
        return severe_dehydration


def assess_appearance():
    appearance = input(appearance_prompt)
    if appearance == "1":
        eyes = input(eye_prompt)
        return assess_eyes(eyes)
    elif appearance == "2":
        skin = input(skin_prompt)
        return assess_skin(skin)


def start_new_diagnosis():
    name = input(name_prompt)
    diagnosis = assess_appearance()
    save_new_diagnosis(name, diagnosis)


def main():
    while True:
        selection = input(welcome_prompt)
        if selection == "1":
            list_patients()
        elif selection == "2":
            start_new_diagnosis()
        elif selection == "q":
            return


main()

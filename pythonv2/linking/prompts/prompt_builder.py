def final_prompt_RQ1_H1(reqs, prompt_code, class_name):
    prompt_reqs = ""
    req_template = (
        "Requirement Document: {document_name}\n"
        "Content:\n{req_content}\n\n"
    )

    for req in reqs:
        prompt_reqs += req_template.format(
            document_name=req["name"],
            req_content=req["content"]
        )

    prompt_class = (
        f"Java Class: {class_name}\n"
        f"Class Details (methods, constructors, variables):\n{prompt_code}\n\n"
    )

    final_prompt = (
        f"{prompt_class}"
        f"The following is a list of related requirements retrieved from a RAG system:\n"
        f"{prompt_reqs}"
        f"Each Java class may be linked to zero, one, two or three requirement.\n"
        f"Please analyze the class and the requirements, and determine if there is a relevant link.\n"
        f"Respond strictly using the following format:\n"
        f"{class_name}.java -> RequirementName.txt\n"
        f"or, if there is no match:\n"
        f"{class_name}.java -> None\n"
        f"\nReturn only the links in the required format. Do not include explanations."
    )

    print(f"Prompt for class {class_name}:\n{final_prompt}\n")

    return final_prompt

def final_prompt_RQ1_H2(reqs, prompt_code, class_name):
    prompt_reqs = ""
    req_template = (
        "Requirement Document: {document_name}\n"
        "Content:\n{req_content}\n\n"
    )

    for req in reqs:
        prompt_reqs += req_template.format(
            document_name=req["name"],
            req_content=req["content"]
        )

    prompt_class = (
        f"Java Class: {class_name}\n"
        f"Class Comments Only (methods and constructors):\n{prompt_code}\n\n"
    )

    final_prompt = (
        f"{prompt_class}"
        f"The following is a list of related requirements retrieved from a RAG system:\n"
        f"{prompt_reqs}"
        f"Each Java class may be linked to zero, one, two, or three requirements.\n"
        f"Please analyze the class and the requirements, and determine if there is a relevant link.\n"
        f"Respond strictly using the following format:\n"
        f"{class_name}.java -> RequirementName.txt\n"
        f"or, if there is no match:\n"
        f"{class_name}.java -> None\n"
        f"\nReturn only the links in the required format. Do not include explanations."
    )

    print(f"Prompt for class {class_name}:\n{final_prompt}\n")

    return final_prompt

def final_prompt_RQ1_H3(reqs, prompt_code, class_name):
    prompt_reqs = ""
    req_template = (
        "Requirement Document: {document_name}\n"
        "Content:\n{req_content}\n\n"
    )

    for req in reqs:
        prompt_reqs += req_template.format(
            document_name=req["name"],
            req_content=req["content"]
        )

    prompt_class = (
        f"Java Class: {class_name}\n"
        f"Class Description (methods, constructors and a general description):\n{prompt_code}\n\n"
    )

    final_prompt = (
        f"{prompt_class}"
        f"The following is a list of related requirements retrieved from a RAG system:\n"
        f"{prompt_reqs}"
        f"Each Java class may be linked to zero, one, two, or three requirements.\n"
        f"Please analyze the class and the requirements, and determine if there is a relevant link.\n"
        f"Respond strictly using the following format (requirement ID can be UC12.txt,...):\n"
        f"RequirementID.txt -> {class_name}.java\n"
        f"or, if there is no match:\n"
        f"{class_name}.java -> None\n"
        f"\nReturn only the links in the required format. Do not include explanations."
    )

    print(f"Prompt for class {class_name}:\n{final_prompt}\n")

    return final_prompt

def final_prompt_RQ1_H4(reqs, prompt_code, class_name):
    prompt_reqs = ""
    req_template = (
        "Requirement Document: {document_name}\n"
        "Content:\n{req_content}\n\n"
    )

    for req in reqs:
        prompt_reqs += req_template.format(
            document_name=req["name"],
            req_content=req["content"]
        )

    prompt_class = (
        f"Java Class: {class_name}\n"
        f"Class Description :\n{prompt_code}\n\n"
    )

    final_prompt = (
        f"{prompt_class}"
        f"The following is a list of related requirements retrieved from a RAG system:\n"
        f"{prompt_reqs}"
        f"Each Java class may be linked to zero, one, two, or three requirements.\n"
        f"Please analyze the class and the requirements, and determine if there is a relevant link.\n"
        f"Respond strictly using the following format (requirement ID can be UC12.txt,...):\n"
        f"RequirementID.txt -> {class_name}.java\n"
        f"or, if there is no match:\n"
        f"{class_name}.java -> None\n"
        f"\nReturn only the links in the required format. Do not include explanations."
    )

    return final_prompt

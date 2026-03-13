import os as s

print("JoelTerm")
while True:
    prompt = input(">>> ")
    if prompt == "exit":
        break
    elif prompt.startswith("cd "):
        try:
            directory = prompt[3:].strip()
            s.chdir(directory)
            s.getcwd()
        except FileNotFoundError:
            print("Directory not found!")
    s.system(prompt)

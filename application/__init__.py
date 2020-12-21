FROM flask IMPORT Flask
IMPORT OS

app = Flask(_name_, static_folder=os.path.abspath("application/view/static"), template_folder=os.path.abspath("application/view/templates"))
# LaunceMS Server Project
# Made Proudly in India, By Prattay Sarkar, aka. Prattay'sElecsGithub

import configparser
from colorama import Fore
from flask import Flask, render_template

print(Fore.GREEN + "╔════╣ LaunceMS Server ╠════╗")
print(Fore.GREEN + "║+- Made Proudly In India -+║")
print(Fore.GREEN + "║+- By Prattay Sarvar, WB -+║")
print(Fore.GREEN + "╚═══════════════════════════╝\n")
print(Fore.BLUE + "|+- Trying To Start LaunceMS Dev Server...")

app = Flask(__name__, template_folder="htmlfiles")

config = configparser.ConfigParser()
config.read('conf.conf')
port = int(config.get('system', 'port'))
indexfile = str(config.get('sysdisk', 'indexfile'))


# ═══════════════  USER AREA  ══════════════════
@app.route('/')
def index():
    return render_template('index.html')


# ══════════════════════════════════════════════

if __name__ == '__main__':
    print(Fore.BLUE + "|+- Switching To Flask Output For Error Checking...\n")

    app.run(host='0.0.0.0', port=port)

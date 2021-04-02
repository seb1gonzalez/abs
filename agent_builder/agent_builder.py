import json
import re

agent = open("agent.txt", "a")
agent.write("import pyautogui\n")
agent.write('import time\n')
agent.write('time.sleep(2)\n')
agent.write("pyautogui.hotkey('ctrl', 'alt', 't')\n")

hotkeys_pattern = re.compile(r"\[(.*?)\]")

with open('events.json') as f:
    data = json.load(f)

proc_data = {"event":[], "cmd":[], "hotkey":[], "hotkey_instances":[]}

for i in data['events']:
    #print("Event: ", i['content'])
    proc_data["event"].append(i['content'])
    match = hotkeys_pattern.search(i['content'])    #finds the hotkey
    #print("Number of hotkey instances:",len(re.findall(hotkeys_pattern, i['content'])))
    proc_data["hotkey_instances"].append(len(re.findall(hotkeys_pattern, i['content'])))
    hotkey = match.group(0) #stores hotkey
    proc_data["hotkey"].append(hotkey)
    #print(match.group(0))   #prints hotkey
    stripped = i['content'].replace(str(hotkey), '')
    #print("Stripped: ", stripped)
    proc_data["cmd"].append(stripped)

for i in range(len(proc_data)):
    for key in proc_data:
        print(key, '->', proc_data[key][i])
        if key=="cmd":
            agent.write("pyautogui.typewrite('{cmd}')\n".format(cmd=str(proc_data[key][i])))
            agent.write("time.sleep(1)\n")
            agent.write("pyautogui.typewrite(['Enter'])\n")
            agent.write("time.sleep(1)\n")
    print("-------------")






    
        



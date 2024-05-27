# How to write a NFC tag (.nfc file) dumped from Flipper Zero with a Proxmark

## 1.Prerequisites

1.1) `pm3` must be already installed. Depending on your OS, it's more or less annoying but that's not the subject of this file.

1.2) You must have some basic knowledge in using a proxmark and differences between GEN 1, GEN 2 and GEN 3 tags (UID, CUID, FUID). In certain cases, malfunctions may come from a poor understanding of these tags.

1.3) A `.nfc` dump on your computer, copied from a Flipper Zero.

## 2. Convert .nfc to .eml

2.1) Paste the `.nfc` file content on this [Cyberchef recipe](https://gchq.github.io/CyberChef/#recipe=Regular_expression('User%20defined','Block%20%5C%5Cd*:%20(.*)',true,true,false,false,false,false,'List%20capture%20groups')Find_/_Replace(%7B'option':'Regex','string':'%20'%7D,'',true,false,true,false))

2.2) Copy result (bottom right box) in a `.eml` file on your computer. (ex : `myfile.eml`)

## 3. Generate commands to write the tag

3.1) Download the file `eml_to_pm3.py` on this repo.

3.2) Replace `DEFAULT_PASSWORD` (write key) and `FILENAME`. In my case, AliExpress tags came with "FFFFFFFFFFFF" as default password.

3.3) Execute the python script. A list of 64 commands is printed. Copy these commands.

## 4. Execute the commands

4.1) Plug your `Proxmark` and launch `pm3`

4.2) Set down the tag your want to write on your Proxmark

4.3) Execute the previously copied commands one after the other starting from number 0 to number 63. ⚠️ I advise you **not to copy/paste everything at once**, I briked an NFC tag like that ⚠️

## 5. Enjoy 🎉



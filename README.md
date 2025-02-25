# DogAgeCalculator
 Calculates dog's age from their Date of Birth
 (made in python)

1) CLI Version (main-cli.py, DogAgeCalculator-CLI.exe)
2) GUI Version (main-ui.pyw, DogAgeCalculator-UI.exe)
3) GUI Version with save file (main-ui-save.pyw, DogAgeCalculator-UI-save.exe) (saves dob of dog to dob.pkl so you dont have to type it each time)

Binaries are available in the Releases section.

# NOTE: Based on aging of small breeds like lhasa apso

To compile .py files to exe, Run:
```
pyinstaller --onefile --no-console main-ui.pyw
pyinstaller --onefile --no-console main-ui-save.pyw
pyinstaller --onefile main-cli.py
```

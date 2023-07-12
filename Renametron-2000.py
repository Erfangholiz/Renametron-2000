import os
import re

while True:
    parent_dir = input('Input the address of the parent directory: ')
    if not os.path.isdir(fr'{parent_dir}'): 
        print('Address is invalid or doesn\'t exist, try again!')
        continue
    elif parent_dir.count('\\') < 3:
        print('You have to be at least three directories deep in a drive for this program to work, this is a built-in feature to prevent accidental data corruption.')
        continue
    print('\nParent address input successful!\n')
    break

while True:
    target_pattern = input('Input the target pattern you want to change (WARNING: this program changes EVERY SINGLE match it finds in ANY of the file names in the subdirectories and that includes FILE EXTENSIONS. It\'s also NOT case-sensitive): ')
    if any(x in '[.^$*+?{}[]\\|()]' for x in target_pattern):
        print('\nThe pattern should not contain REGEX metacharacters such as . ^ $ * + ? { } [ ] \ | ( ) \nWARNING: If you don\'t know REGEX then you can\'t change this specific pattern with this program, this is a built-in feature to prevent users from harming their data!')
        decision = input('If you do understand REGEX and want to submit a pattern, type "Proceed": ')
        if decision.lower() == "proceed":
            print('\nTarget pattern input successful!\n')
            break
        print('\nTarget pattern input unsuccessful, try again!\n')
        continue
    print(target_pattern)
    print('\nTarget pattern input successful!\n')
    break


replacement = input('Input the replacement (if you just want to remove the target patterns leave this empty): ')
sure = input('Are you sure? (n/y) ')

if sure.lower() == 'n':
    quit()
elif sure.lower() == 'y':
    for root, dirs, files in os.walk(parent_dir):
        for file in files:
            if re.search(target_pattern, file):
                old_path = os.path.join(root, file)
                new_file = re.sub(target_pattern, replacement, file)
                new_path = os.path.join(root, new_file)
                try:
                    os.rename(old_path, new_path)
                except PermissionError:
                    print(fr'The file located at {old_path} is open in another program.')
                else:        
                    print(fr"Renamed {old_path} to {new_path}")








'Final program for Individual Programming Assignment #3 Pt. 2'
userFile = input('File for upload (paste file path): ')                                                                 			# User specified vocab list file to upload
x = len(userFile)
filePath = userFile[1:x - 1]                                                                                            			# Removes added quotation marks from file path string
vocabFile = open(filePath, 'r')
vocabLst = vocabFile.readlines()[1:]                                                                                    			# Pulls all lines, excluding header (first line/row of user specified text file)
vocabFile.close()

d = {}
for line in vocabLst:                                                                                                   			# Creates dictionary using the existing definitions from user specified file
    (term, definition) = line.split('\t')                                                                                   			# term = key in dict 'd'; definition = value in dict 'd'
    d[term] = definition
    d.update({term: definition})

AddTerms = input('There are ' + str(len(d)) + ' terms in this vocabulary list. Would you like to add more (Y/N)? ')   			# Returns number of terms currently in dictionary and asks user if they want to add more terms/definitions
if (bool(AddTerms.capitalize() == 'Y') is False) and (bool(AddTerms.capitalize() == 'N') is False):                     # If initial user-input for (Y/N) question causes an error, this loop will run
    while (bool(AddTerms.capitalize() == 'Y') is False) and (bool(AddTerms.capitalize() == 'N') is False):					# While Loop 1: test's (Y/N) user input for errors
        print('Error: Please ONLY enter either \'Y\' or \'N\'')  # Prompts user to specify 'Y' or 'N' ONLY
        AddTerms = input('There are ' + str(len(d)) + ' terms in this vocabulary list. Would you like to add more (Y/N)? ')
        if (bool(AddTerms.capitalize() == 'Y') is False) and (bool(AddTerms.capitalize() == 'N') is False):
            continue
        elif bool(AddTerms.capitalize() == 'Y') is True:
            numTerms = int(input(
                'How many would you like to add (enter an int)? '))  # Following while loop will run the number of times specified by user
            i = 1  # Variable for following while loop
            while i <= numTerms:  # While Loop 3: iterated the user specified number of time (numTerms = number of While Loop 3 iterations); all terms+defs will be added to dict, 'd'
                term = input('Term #' + str(i) + ': ')  # User specifies term to be added to dictionary, 'd'
                definition = input(
                    'Definition #' + str(i) + ': ')  # User specifies definition to be added to dictionary, 'd'
                d.update({term: definition})  # Add term (as key) and definition (as value) to dictionary, 'd'
                i += 1
            AddTerms = input('There are ' + str(
                len(d)) + ' terms in this vocabulary list. Would you like to add more (Y/N)? ')  # Asks user if they want to add more terms after initial terms specified are added
            if bool(AddTerms.capitalize() == 'Y') is True:
                continue
            elif bool(AddTerms.capitalize() == 'N') is True:  # While Loop 2 will break if
                break
            elif (bool(AddTerms.capitalize() == 'Y') is False) and (
                    bool(AddTerms.capitalize() == 'N') is False):  # Re-prompts (Y/N) question if Y or N is not entered for
                while (bool(AddTerms.capitalize() == 'Y') is False) and (bool(AddTerms.capitalize() == 'N') is False):
                    print('Error: Please ONLY enter either \'Y\' or \'N\'')  # Prompts user to specify 'Y' or 'N' ONLY
                    AddTerms = input('There are ' + str(
                        len(d)) + ' terms in this vocabulary list. Would you like to add more (Y/N)? ')
                    if (bool(AddTerms.capitalize() == 'Y') is False) or (bool(AddTerms.capitalize() == 'N') is False):
                        continue
                    elif bool(AddTerms.capitalize() == 'Y') is True:
                        AddTerms = input('There are ' + str(
                            len(d)) + ' terms in this vocabulary list. Would you like to add more (Y/N)? ')
                        break
                    elif bool(AddTerms.capitalize() == 'N') is True:
                        break
                continue
        elif bool(AddTerms.capitalize() == 'N') is True:
            break
elif (bool(AddTerms.capitalize() == 'Y') is True) or (bool(AddTerms.capitalize() == 'N') is True):                      # If no user-input occurs for (Y/N) question, this loop will run
    while bool(AddTerms.capitalize() == 'Y') is True or bool(AddTerms.capitalize() == 'N') is True:						# While Loop 2:
        if bool(AddTerms.capitalize() == 'Y') is True:
            numTerms = int(input('How many would you like to add (enter an int)? '))  								# Following while loop will run the number of times specified by user
            i = 1  # Variable for following while loop
            while i <= numTerms:  																# While Loop 3: iterated the user specified number of time (numTerms = number of While Loop 3 iterations); all terms+defs will be added to dict, 'd'
                term = input('Term #' + str(i) + ': ')  # User specifies term to be added to dictionary, 'd'
                definition = input('Definition #' + str(i) + ': ')  # User specifies definition to be added to dictionary, 'd'
                d.update({term: definition})  # Add term (as key) and definition (as value) to dictionary, 'd'
                i += 1
            AddTerms = input('There are ' + str(len(d)) + ' terms in this vocabulary list. Would you like to add more (Y/N)? ')		# Asks user if they want to add more terms after initial terms specified are added
            if bool(AddTerms.capitalize() == 'Y') is True:
                continue
            elif bool(AddTerms.capitalize() == 'N') is True:												# While Loop 2 will break if
                break
            elif (bool(AddTerms.capitalize() == 'Y') is False) and (bool(AddTerms.capitalize() == 'N') is False):				# Re-prompts (Y/N) question if Y or N is not entered for
                while (bool(AddTerms.capitalize() == 'Y') is False) and (bool(AddTerms.capitalize() == 'N') is False):
                    print('Error: Please ONLY enter either \'Y\' or \'N\'')  # Prompts user to specify 'Y' or 'N' ONLY
                    AddTerms = input('There are ' + str(len(d)) + ' terms in this vocabulary list. Would you like to add more (Y/N)? ')
                    if (bool(AddTerms.capitalize() == 'Y') is False) or (bool(AddTerms.capitalize() == 'N') is False):
                        continue
                    elif bool(AddTerms.capitalize() == 'Y') is True:
                        AddTerms = input('There are ' + str(len(d)) + ' terms in this vocabulary list. Would you like to add more (Y/N)? ')
                        break
                    elif bool(AddTerms.capitalize() == 'N') is True:
                        break
                continue
        elif bool(AddTerms.capitalize() == 'N') is True:
            break

print('There are ' + str(len(d)) + ' terms in the new vocabulary list.\n')

for k in d:                                                                                                             			# Prints dictionary d's terms and definitions once all terms/defs have been added
    print(k, d[k].strip('\n'), sep=' - ')

newFileName = input('What would you like to save the file as? ')                                                        			# User specifies file name
newPath = str(filePath[0:(int(filePath.rfind('\\'))+1)]) + newFileName                                                  			# Concatenate original file's path with new file name specified above

if newPath[int(len(newPath)-4):int(len(newPath))] != '.txt':                                                            			# Ensures outfile is saved as a text file (.txt)
    newPath += '.txt'

if str(newPath[(int(newPath.rfind('\\'))+1):(int(len(newPath)))]) != str(filePath[(int(filePath.rfind('\\'))+1):(int(len(filePath)))]):  # Creates new file named, newFileSaved, if that user doesn't specify original file name (userFile)
    newFileSaved = open(newPath, 'w')
    newFileSaved.write('term\tdefinition\n')                                                                            				# Adds header for key and value columns
    newFileSaved.close()
    newFileSaved = open(newPath, 'a')                                                                                  				# Adds all terms, existing and new, to the newFileSaved
    for term, definition in d.items():
        newFileSaved.write('%s\t%s' % (term, definition))                                                               				# Format text file (term = key, definition = value)
    newFileSaved.close()
else:																				# Saves over original user file specified (userFile)
    orgUserFile = open(str(filePath), 'w')
    orgUserFile.write('term\tdefinition\n')                                                                             				# Adds header for key and value columns
    orgUserFile.close()
    orgUserFile = open(str(filePath), 'a')                                                                              				# Add all terms, existing and new, to the orgUserFile (i.e., the original user file (userFile))
    for term, definition in d.items():
        orgUserFile.write('%s\t%s' % (term, definition))                                                                				# Format text file (term = key, definition = value)
    orgUserFile.close()

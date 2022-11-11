# getting a list of all embedded assets in legacy wiki
Sat Oct 15 2022 11:30am - 11:31pm
### synopsis i guess
I did this pretty easily through vscode's find and search and some manual work, and figured it might be a nice starter project to get back into using python. 
That has got to be the fucking understatement of the year. Anyway, I'm going to give up now and go cry about the day I wasted on this. :D
I did learn a lot though... maybe i'll rewrite this again once I've gotten more experience...

### what each dataset represents
- Dataset 1 was the original sample
- Dataset 2 was a sample of Dataset 1 with instances of the 4 substring types (none, 1, 1+ in file, 1+ in line)
- Dataset 3 was a sample of Dataset 2 with instances of 2 substring types (1+ in file, 1+ in line)
- Dataset 4 was a sample of Dataset 2 with instances of 2 substring types (none, 1)

### goals i had going into this
- [x] 1 cd into dataset1
- [x] 2 read through all files
      - [x] 2a loop through every .md file
      - [x] 2b read every file
- [x] 3 search for ![
      - 3.1 couldn't I just search for .png and .jpeg extensions? - nah too many extensions
      - 3.2 what about http and https? - how would you tell apart from references
      - [x] 3.3 what if there are multiple matches in a file
      - [ ] 3.4 what if there are multiple matches in a line
              - 3.4.1 v2 if (find != rfind) then seek(find) then read(rfind) then...
              - 3.4.2 v1 if (find != rfind) then write "\n" to (rfind_position - 1) now that they are on separate lines repeat until (find == rfind) for every line in file
- [x] 4 print file path and if match was found or not
- [ ] 5 print list of: * \n in ( * )

# getting a list of all embedded assets in legacy wiki
*wait, is this a project post-mortem? :O*
Sat Oct 15 2022 11:30am - 11:31pm

### synopsis i guess
Okay, so basically the plan was to go through 300 or documents from my really old wiki, and extract every reference to an embedded attachment but here the best part. 
Even though I had done this fairly easily through a combination of VSCode find and replace, and a pinch of manually editing outputs. 
I came up with the *brilliant* idea to try and automate it with python, and deluded myself into thinking how much fun it would be and how much I'd learn.
Little did I know how quickly and severely I would come to regret this mini-project. Anywho, I'm gonna go give up now and go cry about wasting my day :D 
On the other hand, atleast I managed to learn a lot... maybe I'll rewrite this with when I've learn more programming. 

### what each dataset represents
*yeah, i have no clue what this was supposed to mean either given that I may have deleted the datasets and didn't bother to write down what they actually were*
- Dataset 1 was the original sample
- Dataset 2 was a sample of Dataset 1 with instances of the 4 substring types (none, 1, 1+ in file, 1+ in line)
- Dataset 3 was a sample of Dataset 2 with instances of 2 substring types (1+ in file, 1+ in line)
- Dataset 4 was a sample of Dataset 2 with instances of 2 substring types (none, 1)

### goals i had going into this
- [x] 1 cd into dataset1
- [x] 2 read through all files
- [x] 2a loop through every `.md` file
- [x] 2b read every file
- [x] 3 search for "!["
- 3.1 couldn't I just search for `.png` and `.jpeg` extensions? *nah too many possible extensions*
- 3.2 what about http and https? - how would you tell apart from references?
- [x] 3.3 what if there are multiple matches in a file
- [ ] 3.4 what if there are multiple matches in a line
- *i have no clue what i'm looking at now that it's been ~~a couple months~~ 20 days lol*
- 3.4.1 v2 if (find != rfind) then seek(find) then read(rfind) then...
- 3.4.2 v1 if (find != rfind) then write "\n" to (rfind_position - 1) now that they are on separate lines repeat until (find == rfind) for every line in file
- [x] 4 print file path and if match was found or not
- [ ] 5 print list of: * \n in ( * )

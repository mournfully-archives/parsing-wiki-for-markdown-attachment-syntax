import os
from mmap import mmap, ACCESS_COPY


# ==================================================================================================================
# v3 - workspace
# https://gist.github.com/rqelibari/d2ab0edc56e25e5b1d86a782b26403d4
# https://cppsecrets.com/users/1330010911110410511610711710997114504848504950504864103109971051084699111109/Python-mmap-Program-to-Replace-a-Text.php
# https://www.tutorialspoint.com/memory-mapped-file-support-in-python-mmap
# https://docs.python.org/3/library/mmap.html
def mmap_stuff(relative_path, string_counter):
    first_index = mm.find(b'![')  # find index of first substring in string
    last_index = mm.rfind(b'![')  # find index of last substring in string
    # https://www.freecodecamp.org/news/python-do-while-loop-example/
    while True:
        if first_index != -1 and last_index != -1:  # > 0 substring in string
            if str(first_index) == str(last_index):  # 1 substring in string
                original_string_start = mm.rfind(b'![')
                original_string_end = mm.find(b') ')
                mm.seek(original_string_start)

                new_string_start = mm.find(b'(')
                new_string_end = mm.find(b')')
                new_byte_difference = new_string_end - new_string_start
                mm.seek(new_string_start)

                print(str(mm.read(new_byte_difference+1)))
                status_output = 'found a match in'
                # https://www.programiz.com/python-programming/break-continue
                break  # terminates containing loop it. if in nested loop terminate innermost loop
            if str(first_index) != str(last_index):  # > 1 substring in string
                # TODO: BROKEN AND IDK HOW TO FIX IT :C - everything else works though :D
                string_counter += 1
                embed_last = mm.rfind(b'![')
                mm.seek(embed_last)
                new_line_first = mm.find(b'\n')
                print(f'![{embed_last}   n{new_line_first}')
                byte_difference = new_line_first - embed_last
                print(mm.read(byte_difference))

                status_output = 'found multiple matches in'
                # https://www.freecodecamp.org/news/python-do-while-loop-example/
                break  # skips rest of code in current iteration and stats next iteration
        if first_index == -1 or last_index == -1:  # 0 substrings in string
            status_output = 'no matches found in'
            break  # terminates innermost loop
    print(f'{status_output}: {relative_path} \n')  # comment out if large dataset


directory_path = os.fsencode("/data/infra/python-projects/list_attachments/dataset2")
for item_name in os.listdir(directory_path):  # loop through every item in directory
    item_absolute_path = os.path.join(directory_path, item_name)  # output item path
    item_relative_path = (str(item_absolute_path)).replace('/data/infra/python-projects/list_attachments/', '')
    item_string_counter = 0
    if os.path.isfile(item_absolute_path):  # if path leads to a file , else next path
        # https://cppsecrets.com/users/1330010911110410511610711710997114504848504950504864103109971051084699111109/Python-mmap-Program-to-Replace-a-Text.php
        # https://pynative.com/python-search-for-a-string-in-text-files/#mmap-to-search-for-a-string-in-text-file
        with open(item_absolute_path, 'r') as file:
            with mmap(file.fileno(), length=0, access=ACCESS_COPY) as mm:
                mmap_stuff(item_relative_path, item_string_counter)


# ==================================================================================================================
# v2 - https://code.tutsplus.com/tutorials/quick-tip-how-to-make-changes-to-multiple-files-within-a-directory-using-python--cms-26452
def v2function():
    # listdir vs scandir - https://docs.python.org/3/library/os.html#os.scandir
    directory = os.scandir(directory_path)
    entries = [it.name for it in directory]
    return entries


# ==================================================================================================================
# v1 - https://stackoverflow.com/questions/10377998/how-can-i-iterate-over-files-in-a-given-directory
# https://www.w3schools.com/python/python_functions.asp
def v1function():
    i = 0
    for v1file in os.listdir(directory_path):
        filename = os.fsdecode(v1file)
        if filename.endswith(".md"):
            # https://youtu.be/qUeud6DvOWI?t=314
            # not sure how to use enumerate() here
            i += 1
            continue
        else:
            continue
    # keyword return - https://www.w3schools.com/python/ref_keyword_return.asp
    return i


# ==================================================================================================================
# v0 - sample python script
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
def v0function(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# ==================================================================================================================
# convert int to str - https://www.geeksforgeeks.org/convert-integer-to-string-in-python/#:~:text=In%20Python%20an%20integer%20can,converts%20it%20into%20a%20string.
# too lazy for log() - https://www.geeksforgeeks.org/log-functions-python/
# btw wasn't there a more readable alternative to: "str" +str(# var)+ "str"

# v3unction()
# print(f' file name list: {v2function()}')
# print(f' found {v1function()} .md files')
# v0function()

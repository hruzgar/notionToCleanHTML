# notionToCleanHTML

### What

There is many projects to export stuff from notion but i couldn't really find a full project, where i can export stuff from notion and remove all the ids or whatever that crap is.

I used 2 other projects in conjunction with my python code to get a fully clean html code with all ids and stuff removed.

The code is custom for now and only works with one layer of subpages but adjusting the code to work on all exports should be a negligible task and would only require a few hours to code. I will do that when I have the time. 

### How to

**So the steps are the following:**

1. Export your notion page with these options:

![](https://github.com/hruzgar/notionToCleanHTML/blob/main/export-options.png)

2. use [notion-export-cleaner](https://github.com/Mrpye/notion-export-cleaner) to remove ids from the filenames
3. use [notionBackup](https://github.com/sueszli/notionBackup) to clean the html files and add page linking
4. use the python code from this project to rename the links inside the .html files to the filenames we changed in the 1. step
5. You should now have a folder with one main .html file and a folder with the rest. Enjoy!

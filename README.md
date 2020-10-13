# Trimor Website
### What is This?
This is a html-based project that I use to run my Dungeon & Dragons campaign! I decided to make this when managing many documents became untenable. I store all of my notes in here which can be searched from the home page, making it very easy to look up information when my players ask of it.
### How does it work?
I store all of my notes in html files. You may notice that the `html` folder is a private submodule. I use this so that my players can't see my notes that I have created and ruin the fun I have prepared! For you to see how this works, clone into this repo, and change `test-html` into `html`. I utilise `lite-server` for the look up function to work. Once you have this all set up, have a play around.

The search script looks through `html\json\info.json`, and matches what you type to anything relevant in there. It is not large enough for efficiency to be an issue. You can also apply filters, if you only want to search for specific types of articles.

I have a python script which converts html to json in `scripts\html_to_json.py`. This makes it easy for me to create notes and instantly have them available for me to search up.

If you click into any of the sections from `index.html`, you wil get a list of articles based on that type. These articles are found in `html\json\articles.json`, which is searched up in `scripts\articleLoad.js`, which makes it easy for me to change which articles I want to be visible.

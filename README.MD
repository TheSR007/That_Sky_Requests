# That Sky Requests
## How to Start
1. Clone This Repo
2. Run Http Debugger to Find new Requests by doing stuff in the game
3. filter out all the other requests and Export it as Sky_Full.json
4. put Sky_Full.json in this directory and run the the Script.py
5. It will go thro each requests and get the first unique request which isn't in the current directory
6. It will create a new .json file with that endpoint and copy the Headers
7. You then need to Include the Request and Response which is the most fit for the .json
8. And Finally push The Changes so we can update the routers accounding to the requests
9. Repeat
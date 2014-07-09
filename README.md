PyRace
================================
PyRace is an interactive bicycle video game installation.  The current plan is for it to consist of four networked Raspberry Pi computers attached to four bicycles (2 adult, 2 child) on trainers with hall effect sensors providing pulses through the GPIO pins.  The software will track all users, allowing them to race against each other (with handicaps). Small screens on each of the bikes will allow the racers to see their current stats and standing in the race, while one large screen will allow spectators to cheer on their favorite competitors. A playlist of MP3s will also be addable to give the contestants some music to cycle to.

TODO:
* Get art assets for all of the characters (the main test character is currently in progress)
* Add sprites flying by in the background (trees, buildings, mountains, clouds). These should be parallax scrolled.
* Create a good sprite system for the player (I have never made a sprite based game from scratch before, going to be following pygame tutorials to learn.)
* Figure out how to network several players (Each one will independently keep track of their world x position, and report it to the other players several times a second.)
* Design a system by which races can be created.  Each race will consist of a main distance, an mp3 playlist, and possibly instructions to do things like stand up on the pedals or sprint at certain times.
* Have a hell of a lot of fun video bike racing!

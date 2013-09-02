PyRace
================================
PyRace is an interactive bicycle video game installation to be shown at NYC Maker Faire 2014.  The current plan is for it to consist of four networked Raspberry Pi computers attached to four bicycles (2 adult, 2 child) on trainers with magnetic sensors providing pulses through the GPIO pins.  The software will display racers as cartoon characters in a video game, allowing them to race against each other (with handicaps allowing everyone to have a shot at winning). Small screens on each of the bikes will allow the racers to see their character's view, while one large screen will allow spectators to cheer on their favorite competitors. A playlist of MP3s will also be addable to give the contestants some music to cycle to.

TODO:
* Fix the bike computer code.  I really don't know how to write code to find the current velocity, and ramp smoothly to whatever the current velocity is.
* Get art assets for all of the characters (the main test character is currently in progress)
* Add sprites flying by in the background (trees, buildings, mountains, clouds). These should be parallax scrolled.
* Create a good sprite system for the player (I have never made a sprite based game from scratch before, and don't know how to do this.)
* Figure out how to network several players (Each one will independently keep track of their world x position, and report it to the other players several times a second.)

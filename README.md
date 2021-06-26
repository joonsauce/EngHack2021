# EngHack2021 project: chAD

<p align="center">
<img src="img/chAD.png" alt="chAD logo" height=300>
</p>

# Table of Contents
- [Sus Discord Bot](#sus-discord-bhot)
- [Table of Contents](#table-of-contents)
- [About the Project](#about-the-project)
- [Usage](#usage)
  - [Command Types](#command-types)
- [License](#license)
- [The Team](#the-team)
# About the Project
A discord bot with influence from the popular indie video game Among Us, with features 
that combines some qualities of other bots. The bot was intended to be used within one server, 
so many parts are very server-specific. There is no public link for this bot. However, you can modify and 
use this bot however you like under the MIT license.
# Usage
At the moment, the bot is configured to be customized per server; some commands need to be 
hardwired in by the person who wants to use them.

There are a plenty of commands to choose from. The prefix is `s!`. You can change the prefix to what you want in setting.py
### Command Types (Among Us variants)
- susrate {user}
  - This command rates a chosen member of the server based on how sus they are. The value is static and does not change.
- sus {user} {action}
  - This command targets a user of doing something sus. The bot will return {author} sussed {user} of {action}.
- scan
  - This command returns a simulated medbay scan from the video game Among Us. The value is static, set per user in each server.
  - If there is more than one user to use the medbay scan, `<@!usertag>` must be used. If only one person, use `<@usertag>` instead.
### Command Types (Music bot variants)
- p
  - Downloads song requested from url or title, then plays through FFMPEG. You MUST have FFMPEG installed on the device you are running the bot on. You can use this command again to queue songs to be played later
- pp
  - Pauses or resumes the music that is playing. It is toggled, so you can use pp to pause AND resume music.
- q
  - Displays songs in queue. Currently very primitive, just displaying the array. This will be updated soon, but it works fine.
- join
  - Makes the bot join the voice channel the command writer is in.
- leave
  - Makes the bot leave the voice channel it is in.
- stop
  - Makes the bot stop the music playing. Stopping the currently playing music will make the next song in the queue play if there is a song in the queue.
- drip
  - This command plays a specific song (in my case, Among Us Drip) in a voice channel. The song can be any you want, as long as it is formatted right. You must download the song yourself, the song isn't included in this repo.
- roll
  - Was meant to be a "gambling" feature but was converted into Rick Roll player.

# License
This project is released under the MIT license, see `LICENSE` for more info.
# The Team
Joonseo Lee - [LinkedIn](https://www.linkedin.com/joonsauce), [Website](http://joonsauce.me)

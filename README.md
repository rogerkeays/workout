# Workout: Tools for your Music Workout

*Workout* turns your music practise into a game. The software has two main
modes: 1) generating a complete list of two and half minute drills from a
musical score for any piece, and 2) creating practise videos and audio to help
practise each phrase and section individually. The required media is
automatically downloaded from YouTube.

Drills are currently only implemented for violin. Practise videos can be
made for any instrument. For an examples of the score format, [browse the
included scores](https://github.com/rogerkeays/workout/blob/main/scores).

## How To Play

Divide your total practise time into three equal slots: drills, practise and
jamming. To practise drills, open the drills folder. Drill cards are text 
files generated using a dependency tree and automatically sorted by hitcount
(i.e. the number of times each skill is needed to play the entire piece or
pieces). Use the generated two and half minute metronome (=TXXX.mp3 files)
and start practising the drill. If you can complete the drill five times in a
row at a good standard, delete the drill card and go to the next drill. If you
run out of time, continue to the next drill without deleting the card.

For the practise slot, open the practise folder and navigate into the folders
until you reach the first phrase. Each phrase, section and piece has a score
that starts at 00, which you increment every time you play that bracket through
correctly. You also get one point for attempting the bracket five times. Recall
or transcribe the bracket using the audio and video files before you play it.
When you're ready to test yourself, play along five times with the audio
bracket and count your points. Increment the folder name by that many points
and go onto the next bracket.

For the jam slot, play through your repertoire using the audio files as a
backing track. Play through any errors and add one point to every piece after
you complete it.

## Installation

These scripts depend on some widely available UNIX utilities. Install them with
your operating system's package manager. E.g.

    sudo apt install python3 ffmpeg abc2midi fluidsynth loudgain timidity node

For video downloads, [`yt-dlp`](https://github.com/yt-dlp/yt-dlp) and a
javascript runtime such as `node` must be installed. The static binaries of
`yt-dlp` are the simplest way to go. Node can be installed using your package
manager as shown above.

Finally, clone this repository:

    git clone https://github.com/rogerkeays/workout.git

## Command Line Tools

The main tool is `make-workout.py`, which reads the score and generates drills
and practise brackets. Run it like this:

    ./make-workout.py scores/violin/*.py

And look for the generated workout files under the `target` directory.

If you want to make your own scores from a YouTube video, you can download the
video manually using the video id:

    ./download-video.py $ID

The downloaded video will be saved to `$HOME/.cache/workout/$ID.mp4`. You can
open this in audacity or whatever tool you plan to use to find the timestamps
for each phrase of music.

Some older, still useful scripts are:

  * `make-arpeggios.sh`: generate arpeggios you can play along with
  * `make-brackets.sh`: cuts mp3s into multiple chunks at different tempos so you can play along with them
  * `make-intervals.sh`: useful for interval recognition and interval singing practise (play on shuffle)
  * `make-metronome.sh`: generates more metronomes than you'll ever need
  * `make-pitches.sh`: useful for tuning, or just to keep as reference
  * `make-scales.sh`: generate scales you can play along with

## Related Resources

  * [ABC](https://abcnotation.com): a musical notation used in parts of *workout*.
  * [Quickstep](https://github.com/rogerkeays/quickstep): another musical notation used in parts of *workout*.
  * [yt-dlp](https://github.com/yt-dlp/yt-dlp): YouTube downloader
  * [More stuff you never knew you wanted](https://rogerkeays.com).


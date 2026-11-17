# old-manifest-bandaid

## how to use it
1. [download the latest binary for your os](https://github.com/ZomkaDEV/old-manifest-bandaid/releases/latest)
1. fully exit steam
1. run it (on windows, it may ask for admin privileges, that's normal)
1. launch steam
1. if you care about the megapicker, run a [file integrity check](https://help.steampowered.com/en/faqs/view/0C48-FCBD-DA71-93EB).

## why does this exist?

a few days ago, jackbox privated the manifest for the old megapicker launch script, this caused issues for anyone who had it installed (so, basically everyone) who was trying to update the game, as the steam client would try to pull the old manifest's metadata to figure out what it needs to update.

this python script rips out the entry for the depot with the megapicker launch script. (you can install it back by running the [file integrity check](https://help.steampowered.com/en/faqs/view/0C48-FCBD-DA71-93EB))

can be run directly via python (with the dependencies installed) or built with pyinstaller ([prebuilt binaries are available here](https://github.com/ZomkaDEV/old-manifest-bandaid/releases/latest))

only depends on the vdf library by valvepython

licensed under [wtfpl](https://github.com/ZomkaDEV/old-manifest-bandaid/blob/main/LICENSE)
import sys, os, vdf, argparse, subprocess

games = {
    "The Jackbox Party Pack": 331670,
    "The Jackbox Party Pack 2": 397460,
    "The Jackbox Party Pack 3": 434170,
    "The Jackbox Party Pack 4": 610180,
    "The Jackbox Party Pack 5": 774461,
    "The Jackbox Party Pack 6": 1005300,
    "The Jackbox Party Pack 7": 1211630,
    "The Jackbox Party Pack 8": 1552350,
    "The Jackbox Party Pack 9": 1850960,
    "The Jackbox Party Pack 10": 2216830,
    "The Jackbox Party Pack 11": 3364070,
    "The Jackbox Party Pack 12": 4199960,
    "The Jackbox Naughty Pack": 2652000,
    "The Jackbox Party Starter": 1755580,
    "The Jackbox Survey Scramble": 2948640,
    "Drawful 2": 442070,
    "Quiplash": 351510,
    "Quiplash 2 InterLASHional": 1111940,
    "Fibbage XL": 448080,
    "The Jackbox Party Pack 9 Demo": 2132470,
    "The Jackbox Party Pack 10 Demo": 2561940,
    "The Jackbox Party Pack 11 Demo": 3827040,
    "The Jackbox Survey Scramble Demo": 3257070,
    "Trivia Murder Party 3": 3048060,
    "Fakin It XL": 5054700
}

def get_default_steam_location():
    match sys.platform:
        case "win32":
            return "C:\\Program Files (x86)\\Steam\\steamapps\\"
        case "darwin":
            return os.getenv('HOME') + "/Library/Application Support/Steam/steamapps/"
        case "linux":
            return os.getenv('HOME') + "/.local/share/Steam/steamapps/"

def steam_is_running():
    try:
        if sys.platform == "win32":
            out = subprocess.run(["tasklist", "/FI", "IMAGENAME eq steam.exe", "/NH"],
                                 capture_output=True, text=True, creationflags=0x08000000).stdout
            return "steam.exe" in out.lower()
        name = "steam_osx" if sys.platform == "darwin" else "steam"
        return subprocess.run(["pgrep", "-x", name], capture_output=True).returncode == 0
    except OSError:
        return False  # couldn't check; don't block

parser = argparse.ArgumentParser(description="Removes the broken Megapicker launch script depot entry from the metadata of installed Jackbox games")
parser.add_argument("library", nargs="?", help="Custom path to a Steam library's steamapps folder")
args = parser.parse_args()

steamapps = args.library or get_default_steam_location()
steamapps = os.path.join(steamapps, "")

if not os.path.isdir(steamapps):
    sys.exit("Steam library folder not found: " + steamapps)

if steam_is_running():
    print("Steam is running. Fully exit Steam first (Steam > Exit), otherwise it will overwrite the changes, then run this again.")
    input("Press Enter to exit...")
    sys.exit(1)

ripped = False

for game in games:
    acf = steamapps + "appmanifest_" + str(games[game]) + ".acf"
    if os.path.isfile(acf):
        d = vdf.load(open(acf))
        if ("2828508" in d["AppState"]["InstalledDepots"]) and (d["AppState"]["InstalledDepots"]["2828508"]["manifest"] == "5145691608909662874"):
            d["AppState"]["InstalledDepots"].pop("2828508")
            vdf.dump(d, open(acf,'w'), pretty=True)
            print(game + " has a broken manifest that was now removed.")
            if ripped == False:
                ripped = True

if (ripped == True):
    print("\n\n------------------------------------------------------------\nThe 'No internet connection' issue should no longer be present. If you do use the Megapicker, you want to run the integrity check for all of the games that were mentioned above.\nhttps://help.steampowered.com/en/faqs/view/0C48-FCBD-DA71-93EB\n------------------------------------------------------------\n\n")
    input("Press Enter to exit...")
set -x ;

find . -name "*.json" | grep ssx | awk -F '/' '{print $2}' | xargs -I {} sudo cp -R ./{}/Contents/Resources/SCMap.json "/Library/Application Support/Softube/SSX/{}/Contents/Resources/SCMap.json";
ps auxww  | grep "Console 1" | grep -v grep | awk '{print $2}' | xargs kill -9;
open /Applications/Console\ 1\ On-Screen\ Display.app;


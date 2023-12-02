set -x ;

ls ./SSX | xargs -I {} sudo cp -R ./SSX/{}/Contents/Resources/SCMap.json "/Library/Application Support/Softube/SSX/{}/Contents/Resources/SCMap.json";
ps auxww  | grep "Console 1" | grep -v grep | awk '{print $2}' | xargs kill -9 && sleep 1 &&
open /Applications/Console\ 1\ On-Screen\ Display.app;


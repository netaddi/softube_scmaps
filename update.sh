set -x ;

ls ./SSX | grep -v VST3 | xargs -I {} sudo cp -R ./SSX/{}/Contents/Resources/SCMap.json "/Library/Application Support/Softube/SSX/{}/Contents/Resources/SCMap.json";
ls ./SSX | grep VST3 | xargs -I {} sudo cp ./SSX/{} "/Library/Application Support/Softube/SSX/";
ps auxww  | grep "Console 1" | grep -v grep | awk '{print $2}' | xargs kill -9 && sleep 1 &&
ps auxww  | grep "PluginDoctor" | grep -v grep | awk '{print $2}' | xargs kill -9 &&
open /Applications/Console\ 1\ On-Screen\ Display.app;
open /Applications/PluginDoctor.app;


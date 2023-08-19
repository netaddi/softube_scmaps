set -x;

export CURRENT_DIR=`pwd`;
cd "/Library/Application Support/Softube/SSX/" && \
find . -name 'SCMap.txt' | xargs  -I {} rsync -R {} $CURRENT_DIR/;


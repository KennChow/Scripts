cd /Users/zhouchen/Scripts

git add .

curDate=$(date "+%Y%m%d")

git commit -m 'updated-'${curDate}'@Ken'

git push origin main


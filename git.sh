git add .

echo 'New feature'
read commitMessage

git commit -m "$commitMessage"

echo 'main'
read branch

git push origin $branch

read
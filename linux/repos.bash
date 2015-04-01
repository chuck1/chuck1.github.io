


while read loc
do
	git_process.bash $loc
done < "$HOME/repos.txt"





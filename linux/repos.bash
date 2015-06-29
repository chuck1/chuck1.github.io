
if [[ $# -eq 0 ]]
then
	echo "usage"
	exit 1
fi

if [ "$1" == "push" ]
then
	#while read loc
	#do
	#	git_process.bash $loc
	#done < "$HOME/repos.txt"

	for d in git/*/ ; do
		git_process.bash $d
	done

	exit 0
fi

if [ "$1" == "remote" ]
then
	#while read loc
	#do
	#	git_remote.bash $loc
	#done < "$HOME/repos.txt"

	for d in */ ; do
		git_remote.bash $d
	done

	exit 0
fi





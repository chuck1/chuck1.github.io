
function git_dirty {
	expr $(git status --porcelain 2>/dev/null| egrep "^(M| M)" | wc -l)
}

process () {
	cd
	cd $1

	echo $1

	if [ `git_dirty` != 0 ]; then
		echo dirty
		git add --all
		git commit -m 'auto'
		git push origin master
	else
		echo clean
	fi
}


process "git/chuck1.github.io"
process "git/c-testing"
process "git/n-body"
process "git/python"
process "git/thesis"
process "git/wiki"



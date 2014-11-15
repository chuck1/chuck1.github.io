cd

# install packages

apt-get build-dep glfw

apt-get install g++ doxygen graphviz

apt-get install libxi-dev libxcursor-dev libglew-dev libpng12-dev libfreetype6-dev

apt-get install libboost-system1.55-dev libboost-thread1.55-dev libboost-serialization1.55-dev

# startup scripts

cp git/chuck1.github.io/linux/vimrc ~/.vimrc
cat git/chuck1.github.io/linux/bashrc >> ~/.bashrc

# git repos

cd git

git clone git clone http://github.com/chuck1/python python
git clone git clone http://github.com/chuck1/pywiki
git clone git clone http://github.com/chuck1/wiki_private
git clone git clone http://github.com/chuck1/wiki_subshot

mkdir nebula-engine
cd nebula-engine
git clone http://github.com/nebula-engine/nebula







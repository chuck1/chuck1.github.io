cd

# install packages

apt-get build-dep glfw

apt-get install g++ doxygen graphviz 

apt-get install python-numpy python3-numpy python-django python-jinja2 python-scipy python-matplotlib python3-matplotlib python-qt4 python3-pyqt4

apt-get install libxi-dev libxcursor-dev libglew-dev libpng12-dev libfreetype6-dev

apt-get install libboost-system1.55-dev libboost-thread1.55-dev libboost-serialization1.55-dev

apt-get install apache2 php5

# apache

a2enmod cgi
apache2 restart

cd git/chuck1/github.io/linux

cat apache2.conf >> /etc/apache2/apache2.conf

# startup scripts

cp vimrc ~/.vimrc
cat bashrc >> ~/.bashrc

# git repos

cd git

git clone git clone http://github.com/chuck1/python python
git clone git clone http://github.com/chuck1/pywiki
git clone git clone http://github.com/chuck1/wiki_private
git clone git clone http://github.com/chuck1/wiki_subshot
git clone git clone http://github.com/chuck1/thesis

mkdir nebula-engine
cd nebula-engine
git clone http://github.com/nebula-engine/nebula







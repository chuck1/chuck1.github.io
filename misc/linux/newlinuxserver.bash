cd

# install packages

apt-get install g++ doxygen graphviz sqlite3

apt-get install python-numpy  python-django python-jinja2  python-scipy python-matplotlib  python-qt4    python-pip python-pygraphviz
apt-get install python3-numpy               python3-jinja2              python3-matplotlib python3-pyqt4

apt-get install apache2 apache2-dev php5

#apt-get install dhcp3-server tftpd-hpa syslinux nfs-kernel-server initramfs-tools

apt-get install libapache2-mod-wsgi

# apache

a2enmod wsgi
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







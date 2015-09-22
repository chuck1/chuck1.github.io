
# install packages

apt-get install \
	g++ \
	doxygen \
	graphviz \
	sqlite3 \
	cmake \
	ruby \
	ruby-dev \
	distcc \
	valgrind -y

apt-get install python-networkx \
	python-numpy \
	python-django \
	python-jinja2 \
	python-scipy \
	python-matplotlib \
	python-qt4 \
	python-pip \
	python-pygraphviz \
	python3-numpy \
	python3-jinja2 \
	python3-matplotlib \
	python3-pyqt4 -y

# packages needed for glfw
apt-get build-dep glfw -y 

apt-get install \
	libxinerama-dev \
	libxi-dev \
	libxcursor-dev \
	libglew-dev \
	libpng12-dev \
	libfreetype6-dev -y

# needed for game engine
apt-get install \
	freeglut3-dev \
	libboost-system1.55-dev \
	libboost-thread1.55-dev \
	libboost-serialization1.55-dev \
	libboost-program-options1.55-dev \
	libboost-python1.55-dev \
	ttf-mscorefonts-installer -y

# for making web server
apt-get install \
	apache2 \
	apache2-utils \
	apache2-dev \
	php5 \
	python-django-extensions \
	python-django-celery \
	wkhtmltopdf -y


# for setting up nfs server?
apt-get install dhcp3-server tftpd-hpa syslinux nfs-kernel-server initramfs-tools -y

# for manual network config
apt-get install \
	nmap \
	net-tools \
	python-nmap \
	python-ethtool \
	wpasupplicant -y

# for mingw compiling
apt-get install \
	gcc-mingw-w64-x86-64 \
	libc6-dev-i386 -y




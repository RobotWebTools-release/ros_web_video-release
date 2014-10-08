Name:           ros-hydro-ros-web-video
Version:        0.1.13
Release:        0%{?dist}
Summary:        ROS ros_web_video package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/ros_web_video
Source0:        %{name}-%{version}.tar.gz

Requires:       bzip2-devel
Requires:       ros-hydro-image-transport
Requires:       ros-hydro-mk
Requires:       ros-hydro-roscpp
Requires:       ros-hydro-rostime
Requires:       ros-hydro-sensor-msgs
Requires:       zlib-devel
BuildRequires:  bzip2-devel
BuildRequires:  git
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-image-transport
BuildRequires:  ros-hydro-mk
BuildRequires:  ros-hydro-roscpp
BuildRequires:  ros-hydro-rostime
BuildRequires:  ros-hydro-sensor-msgs
BuildRequires:  yasm
BuildRequires:  zlib-devel

%description
Streaming of ROS Image Topics via HTTP

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Wed Oct 08 2014 Russell Toris <rctoris@wpi.edu> - 0.1.13-0
- Autogenerated by Bloom


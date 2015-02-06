#define git  5493f448
%define major 0

Name:		gluon
Summary:	A cross-platform free and open source 2D game engine from KDE
Group:		Graphical desktop/KDE
Version:	0.71.0
Release:	4
License:	GPLv2+
URL:		http://gluon.tuxfamily.org/
Source0:	http://gitorious.net/gluon/%{name}-%{version}.tar.bz2
Patch0:		gluon-0.71.0-gcc-4.7.patch

BuildRequires:	kdelibs4-devel
BuildRequires:	pkgconfig(alure)
BuildRequires:	pkgconfig(glew)
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(openal)

%description
Gluon is a cross-platform free and open source 2D game engine from KDE. 
It aims to make life easier for game developers by providing a simple 
but powerful API to handle 2D objects, sounds and inputs.

%files
%{_kde_bindir}/gluon*
%{_kde_datadir}/applications/gluon_kdeextplayer.desktop
%{_kde_datadir}/applications/gluon_kdeplayer.desktop
%{_kde_datadir}/applications/gluon_qmlplayer.desktop
%{_kde_datadir}/applications/gluon_qtplayer.desktop
%{_kde_applicationsdir}/gluon-creator.desktop
%{_kde_appsdir}/gluon_kdeextplayer/
%{_kde_appsdir}/gluoncreator/
%{_kde_appsdir}/gluoneditorpart/
%{_kde_appsdir}/gluonviewerpart/
%{_kde_datadir}/config.kcfg/gluoncreatorsettings.kcfg
%{_kde_datadir}/gluon/
%{_kde_datadir}/mime/packages/x-gluon-mimetypes.xml
%{_kde_services}/*.desktop
%{_kde_servicetypes}/gluoncreator_plugin.desktop
%{_kde_iconsdir}/hicolor/*
%{_kde_libdir}/gluon/
%{_kde_libdir}/kde4/*.so

#-----------------------------------------------------------------------------
%define libgluonaudio %mklibname gluonaudio %{major}

%package -n %{libgluonaudio}
Summary:	%{name} library
Group:		System/Libraries

%description -n %{libgluonaudio}
%{name} library.

%files -n %{libgluonaudio}
%{_kde_libdir}/libGluonAudio.so.%{major}*

#-----------------------------------------------------------------------------
%define libgluoncore %mklibname gluoncore %{major}

%package -n %{libgluoncore}
Summary:	%{name} library
Group:		System/Libraries

%description -n %{libgluoncore}
%{name} library.

%files -n %{libgluoncore}
%{_kde_libdir}/libGluonCore.so.%{major}*

#-----------------------------------------------------------------------------
%define libgluoncreator %mklibname gluoncreator %{major}

%package -n %{libgluoncreator}
Summary:	%{name} library
Group:		System/Libraries

%description -n %{libgluoncreator}
%{name} library.

%files -n %{libgluoncreator}
%{_kde_libdir}/libGluonCreator.so.%{major}*

#-----------------------------------------------------------------------------
%define libgluonengine %mklibname gluonengine %{major}

%package -n %{libgluonengine}
Summary:	%{name} library
Group:		System/Libraries

%description -n %{libgluonengine}
%{name} library.

%files -n %{libgluonengine}
%{_kde_libdir}/libGluonEngine.so.%{major}*

#-----------------------------------------------------------------------------
%define libgluoninput %mklibname gluoninput %{major}

%package -n %{libgluoninput}
Summary:	%{name} library
Group:		System/Libraries

%description -n %{libgluoninput}
%{name} library.

%files -n %{libgluoninput}
%{_kde_libdir}/libGluonInput.so.%{major}*

#-----------------------------------------------------------------------------
%define libgluongraphics %mklibname gluongraphics %{major}

%package -n %{libgluongraphics}
Summary:	%{name} library
Group:		System/Libraries

%description -n %{libgluongraphics}
%{name} library.

%files -n %{libgluongraphics}
%{_kde_libdir}/libGluonGraphics.so.%{major}*

#-----------------------------------------------------------------------------
%define libgluonplayer %mklibname gluonplayer %{major}

%package -n %{libgluonplayer}
Summary:	%{name} library
Group:		System/Libraries

%description -n %{libgluonplayer}
%{name} library.

%files -n %{libgluonplayer}
%{_kde_libdir}/libGluonPlayer.so.%{major}*

#-----------------------------------------------------------------------------
%package devel
Summary:	Headers files for %{name}
Group:		Development/KDE and Qt
Requires:	%{libgluonaudio} = %{version}-%{release}
Requires:	%{libgluoncore} = %{version}-%{release}
Requires:	%{libgluoncreator} = %{version}-%{release}
Requires:	%{libgluonengine} = %{version}-%{release}
Requires:	%{libgluoninput} = %{version}-%{release}
Requires:	%{libgluongraphics} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description devel
Headers files needed to build %{name}.

%files devel
%{_kde_datadir}/cmake/Modules/*
%{_kde_includedir}/gluon/
%{_kde_libdir}/libGluon*.so

#-----------------------------------------------------------------------------
%prep
%setup -q
%patch0 -p0

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build


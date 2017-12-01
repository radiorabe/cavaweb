# C.A.V.A Web

Simple SystemD configuration that exposes the [C.A.V.A.](http://karlstav.github.io/cava/) console audio meter
as a webapp using [gotty](https://github.com/yudai/gotty).

# Installation

```
curl -o /etc/yum.repos.d/home_radiorabe_audio.repo http://download.opensuse.org/repositories/home:/radiorabe:/audio/CentOS_7/home:radiorabe:audio.repo
curl -o /etc/yum.repos.d/home_radiorabe_misc.repo http://download.opensuse.org/repositories/home:/radiorabe:/misc/CentOS_7/home:radiorabe:misc.repo

yum install cavaweb

# Allow the cavaweb user to acces the audio input
usermod -a -G audio cavaweb

# configure cavaweb
cp /var/lib/cavaweb/.config/cava/config.example \
   /var/lib/cavaweb/.config/cava/config

# start service
systemctl enable cavaweb
systemctl start cavaweb
```

Visit hostname:8080 to see the C.A.V.A. audio meter.

#! /bin/sh

### BEGIN INIT INFO
# Provides:          __power_button.py
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
### END INIT INFO

name=__power_button.py

case "$1" in
  start)
    echo "Starting $name"
    /usr/local/bin/$name &
    ;;
  stop)
    echo "Stopping $name"
    pkill -f /usr/local/bin/$name
    ;;
  *)
    echo "Usage: /etc/init.d/$name {start|stop}"
    exit 1
    ;;
esac

exit 0

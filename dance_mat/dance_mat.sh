#! /bin/sh

### BEGIN INIT INFO
# Provides:          __dance_mat.py
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
### END INIT INFO

name=__dance_mat.py

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

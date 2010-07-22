DesktopMeter collects usage stats for your Linux desktop.

How to use it?
==============

+ Checkout from github
        git clone http://github.com/jyro2080/DesktopMeter.git DesktopMeter

+ Start the background daemon
        cd DesktopMeter/src
        python dmeterd &

+ Continue your regular work

+ When you want to check the stats
        cd DesktopMeter/src
        ./dmeter

Implementation
==============
+ DesktopMeter currently consists of a background daemon `dmeterd` and a command line utility `dmeter` to view the stats.
+ `dmeterd` is a python script which sleeps most of the time, but wakes at specified intervals (30sec by default) and checks what application window is currently active. It uses some external X commands for this job (`xprop`). It can also detect if there  was not keyboard activity in the interval elapsed. It logs this information in a sqlite database (stored at $HOME/.dmeterdb)
+ `dmeter` CLI, reads the information logged by daemon in database and calculates various stats for the current day.

Example `dmeter` output
=======================
    unicorn: ~/source/DesktopMeter/src $ ./dmeter 
    Today's Top app usage (for 16 hours)
    ------------------------------
           google-chrome    45 %
                    gvim    37 %
                Terminal     8 %
                git-cola     2 %
                    xchm     1 %
                  okular     1 %
             xfce4-panel     0 %
               quodlibet     0 %
 
    Active factor: 
    ------------------------------
    40.77 %



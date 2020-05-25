TMUX-MPI
========

Introduction
------------

tmux-mpi connects MPI processes to tmux windows. MPI launches n instances of dtach, these n instances are then connected to in tmux windows. 
To launch a command use:
::
    
    tmux-mpi <nproc> <command>

For example,
::
    
    tmux-mpi 2 hostname

will start a tmux session called ``tmux-mpi`` that can be connect to in a different terminal with
::

    tmux attach -t tmux-mpi

or use
::

    tmux attach

if there are no other tmux sessions. You may need to scroll up in the tmux window to see the output of this example.
This dtach approach does mean that if the program crashes manual cleanup may need to happen. For example:
::

    pkill -9 dtach

Copyright 2019, WR Saunders, wrs20@bath.ac.uk

Installation
------------
Requires dtach and tmux to be installed. Pip installable with:
::
    
    pip install --upgrade --no-cache-dir git+https://github.com/wrs20/tmux-mpi@master



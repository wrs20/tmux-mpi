TMUX-MPI
========

Introduction
------------

tmux-mpi connects MPI processes to tmux windows. MPI launches n instances of dtach, these n instances are then connected to in tmux windows. This approach does mean that if the program crashes manual cleanup may need to happen. For example:
::

    pkill -9 dtach

Copyright 2019, WR Saunders, wrs20@bath.ac.uk

Installation
------------
Pip installable with:
::
    
    pip install --upgrade --no-cache-dir git+https://github.com/wrs20/tmux-mpi@master



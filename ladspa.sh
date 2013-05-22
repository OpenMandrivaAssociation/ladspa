#!/bin/sh
# Set LADSPA_PATH for Bash shell
if [ -n "\$LADSPA_PATH" ]; then
   export LADSPA_PATH="/usr/lib/ladspa/"
fi

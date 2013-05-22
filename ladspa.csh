#!/bin/csh
# Set LADSPA_PATH for csh
if ( ${?LADSPA_PATH} ) then
   exit
endif

setenv LADSPA_PATH /usr/lib/ladspa/

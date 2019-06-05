#!/bin/bash
#########################################################################
# File Name: gdc_download.sh
# Author: CJB
# mail: johnlcd@stu.xjtu.edu.cn
# Created Time: Wed Jun  5 11:19:41 CST 2019
#########################################################################


if [ $# == "6" ] && [ $1 == "-m" ] && [ $3 == "-t" ] && [ $5 == "-d" ]
then

	manifest=${2}
	token=${4}
	outdir=${6}

	gdc-client download -m ${manifest} -t ${token} -d ${outdir}


else \

	echo ======================================
	
	echo " "
	echo USAGE:
	echo " "
	echo " $0 -m <manifest file> -t <token file> -d <out directory> "
	echo " "
	
	echo --------------------------------------
	
	echo " "
	echo EXAMPLEs:
	echo " "
	echo " $0 -m gdc_manifest_XXXXX.txt -t gdc-user-token.txt -d . "
	echo " "
	
	echo ======================================
	
	echo " "
	echo Command is: $0 $*
	echo " "

fi


## END


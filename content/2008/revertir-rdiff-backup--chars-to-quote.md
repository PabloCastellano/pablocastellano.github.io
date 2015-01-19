Title: Revertir rdiff-backup -chars-to-quote
Date: 2008-11-16
Category: TODO
Tags: Linux

> IFS=" " for i in $(find|grep '\;'); do mv -i -v $i $(echo $i|sed 's/\;065/A/g' | sed 's/\;066/B/g' | sed 's/\;067/C/g' | sed
> 's/\;068/D/g' | sed 's/\;069/E/g' | sed 's/\;070/F/g' | sed 's/\;071/G/g' | sed 's/\;072/H/g' | sed 's/\;073/I/g' | sed
> 's/\;074/J/g' | sed 's/\;075/K/g' | sed 's/\;076/L/g' | sed 's/\;077/M/g' | sed 's/\;078/N/g' | sed 's/\;079/O/g' | sed
> 's/\;080/P/g' | sed 's/\;081/Q/g' | sed 's/\;082/R/g' | sed 's/\;083/S/g' | sed 's/\;084/T/g' | sed 's/\;085/U/g' | sed
> 's/\;086/V/g' | sed 's/\;087/W/g' |sed 's/\;088/X/g'|sed 's/\;089/Y/g' | sed 's/\;090/Z/g') ; done

Ejecutar varias veces.

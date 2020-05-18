
Shotlisting logic for PHD(Regular)

	qfd=qualifying degree
	qdis=qualifying degree discipline
	qcpi=qualifying degree marks in cpi
	qper= qualifying degree marks in percentage
	ugper=undergraduate percentage
	ugcpi=undergraduate CPI
	imper=intermdediate percentage
	hscpi=highschool CPI
	hsper=highschool percentage


	if[(qfd==M.Tech|M.E.|M.S.) and (qdis=CS|IT|EC|Maths & Comp) and (qcpi>=6.5 or qper>=60) and (ugcpi>=6.5 or ugper>=60) and (imper>=60)and (hscpi>=6.5 or hsper>=60) and (gate_exam=yes)]
{
	if[(category==General and age<=32) or (category==OBCNCL and age<=37) or (category==EWS and age<=37) or (gender==women and age<=37)]
		then print "shortlisted"
}

elseif[(qfd==B.Tech|MCA|MSc.) and (qdis=CS|IT|EC|Maths & Comp) and (qcpi>=8 or qper>=75)  and (ugcpi>=6.5 or ugper>=60) and (imper>=60)and (hscpi>=6.5 or hsper>=60) and (gate_exam=yes) and (gate_rank<=5000)]
{
	if[(categore==General and age<=28) or (category==OBCNCL and age<=33) or (category==EWS and age<=33) or (gender==women and age<=33)]
		then print "shortlisted"
}

elseif[(category==sc|st or pd=yes)]
{
	if[(qfd==M.Tech/M.E./M.S.) and (qdis=CS|IT|EC|Maths & Comp) and (qcpi>=6.5 or qper>=60) and (ugcpi>=6.0 or ugper>=55) and (imper>=60)and (hscpi>=6.5 or hsper>=60) and (gate_exam=yes) and age<=37]
		then print "shortlisted"

			elseif[(qfd==B.Tech or MCA or MSc.) and (qdis=CS|IT|EC|Maths & Comp) and (qcpi>=8 or qper>=75)  and (ugcpi>=6.0 or ugper>=55) and (imper>=60)and (hscpi>=6.5 or hsper>=60) and (gate_exam=yes) and (gate_rank<=6000) and age<=33]
			then print "shortlisted"
}

else
print "Not shortlisted"

Some more clause:
1. If Masters from IIT/IISc/ISI then ugper>=55% or 6.0 also considered.
2. If M.Tech or M.E. or M.S.>=70% or 7.5 CPI then X>=55% or XII>=55% also considered but not both. 
3. If B.Tech from IITs with CGPA>=8.0 then no gate required and X>=55% or XII>=55%  aslo considered but not both. 

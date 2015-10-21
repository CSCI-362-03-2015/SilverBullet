cd ..

cd testCaseExecutables
arr=( * )


#for i in "${arr[*]}" 
#do
#	echo "$i"	
        
#done

S1= ""
for ((i=0; i<${#arr[*]}; i++));
do
	
	python ${arr[i]}
	
	
	
done

 -- Which artists had the most Top 100 songs? 
 
 SELECT 
	artists, 
    count(*) as nb_top100_songs
FROM 
	top2018
GROUP BY 
	1
ORDER BY 2 DESC
LIMIT 1;
 
 -- Are there more artists in the Top 100 with 'Lil' in their name, or with 'DJ' in their name?
 
 SELECT * FROM top2018;
 
 SELECT 
	COUNT(CASE WHEN artists LIKE '%Lil%' THEN artists ELSE NULL END) as lil_in_name,
    COUNT(CASE WHEN artists LIKE '%DJ%' THEN artists ELSE NULL END) as DJ_in_name
FROM 
	top2018;
    
 
 -- Which song attributes are most strongly correlated? What attributes seem to have very little correlation?
 -- Here I decided to work on python and use the pandas library which is way more efficient than MySQL.
 
 -- Which attributes have the most variability? Which tend to be the most similar among the Top 100 songs?
 -- Here I decided to work on python and use the pandas library which is way more efficient than MySQL.
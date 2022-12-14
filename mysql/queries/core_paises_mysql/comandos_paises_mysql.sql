SELECT countries.name, languages.language, languages.percentage 
FROM  countries 
JOIN languages ON countries.code = languages.country_code
WHERE language = 'Slovene'
ORDER by percentage DESC;


SELECT countries.name, languages.language, COUNT(cities.id) 
FROM countries
JOIN cities ON countries.code = cities.country_code
JOIN languages ON countries.code = languages.country_code
WHERE is_official = true
GROUP BY countries.code
ORDER BY COUNT(cities.id) DESC;


SELECT cities.name, cities.population
FROM cities
JOIN countries ON cities.country_id = countries.id
WHERE countries.code = 'MEX'AND cities.population > '500000'  
ORDER BY population DESC;


SELECT countries.name, languages.language, languages.percentage
FROM countries
JOIN languages ON countries.code = languages.country_code
WHERE languages.percentage > '89%'
ORDER BY percentage DESC;


SELECT countries.name, countries.surface_area, countries.population
FROM countries
WHERE surface_area < '501' AND population > '100000';


SELECT countries.name, countries.government_form, countries.capital, countries.life_expectancy
FROM countries
WHERE government_form = 'Constitutional Monarchy' AND capital > '200' AND life_expectancy > '75';    


SELECT countries.name AS country, cities.name AS city, cities.district AS district, cities.population
FROM countries
JOIN cities ON countries.code = cities.country_code
WHERE countries.code = 'ARG' AND cities.district = 'Buenos Aires' AND cities.population > '500000';


SELECT countries.region, COUNT(countries.id) as number_of_countries
FROM world.countries
GROUP BY region
ORDER BY COUNT(countries.id) DESC;
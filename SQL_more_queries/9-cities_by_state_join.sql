-- Lists all cities with their state names in the format: cities.id - cities.name - states.name
SELECT cities.id, cities.name, states.name
FROM cities, states
WHERE cities.state_id = states.id
ORDER BY cities.id ASC;

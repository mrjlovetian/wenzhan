

///查询重复数据
SELECT * FROM wenzhan WHERE title IN ( SELECT title FROM wenzhan GROUP BY wenzhan HAVING count(title) > 1 );


///删除重复数据
DELETE from wenzhan WHERE (title) in
(SELECT title from (SELECT title FROM wenzhan GROUP BY title HAVING COUNT(*)>1));
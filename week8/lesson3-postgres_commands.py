# Добавить данные в бд university

1 INSERT INTO public.student(
	last_name, name, age, spec_id, course_id, facultet_id, form_id)
	VALUES ( 'Bondarenko', 'Roman', 32, null, null, null, null);

2 UPDATE public.facultet
	SET name='Медицинский факультет'
	WHERE name='Медицины';

3 UPDATE public.facultet
	SET name='Медицинский'
	WHERE id=4;

4 SELECT * FROM public.facultet
ORDER BY id ASC

5 SELECT * FROM public.facultet
ORDER BY name ASC

6 INSERT INTO public.student(
	last_name, name, age, spec_id, course_id, facultet_id, form_id)
	VALUES ('Marararov', 'Borsheed', 108, null, null, 4, null);

7 UPDATE public.student
	SET facultet_id=4
	WHERE name='Dastan';

8 DELETE FROM public.student
	WHERE id=7;

9 #TODO DELETE FROM public.student
#TODO	WHERE id=0 or id=10;

10 UPDATE public.student
	SET facultet_id=4
	WHERE id=4 ;

11 INSERT INTO public.spec(
	name, facultet_id)
	VALUES ('Лечебное дело', 4);

12 INSERT INTO public.spec(
	name, facultet_id)
	VALUES ('Педиатрия', 4);






Gertrude Kapllan, [19.10.2023 09:22]
SELECT * FROM student WHERE age::TEXT LIKE '2%';

Gertrude Kapllan, [19.10.2023 09:25]
UPDATE student SET start_year = '2023-11-19 09:04:05.335246' WHERE id=5;

SELECT * FROM student WHERE start_year::TEXT LIKE '%-10-%';

Gertrude Kapllan, [19.10.2023 09:28]
SELECT last_name, length(last_name) as len FROM student ORDER BY len DESC;

Gertrude Kapllan, [19.10.2023 09:31]
SELECT last_name, COUNT(last_name) as len  FROM student GROUP BY last_name;

Gertrude Kapllan, [19.10.2023 09:37]
SELECT COUNT(age) as count  FROM student where age=21;

Gertrude Kapllan, [19.10.2023 09:43]
select last_name, course_id from student order by course_id NULLS first;

Gertrude Kapllan, [19.10.2023 09:45]
select distinct last_name from student;

Gertrude Kapllan, [19.10.2023 09:54]
select *  from student WHERE age BETWEEN 18 AND 23;

Gertrude Kapllan, [19.10.2023 09:54]
select *  from student WHERE age > 18 AND AGE < 23;

Gertrude Kapllan, [19.10.2023 10:07]
SELECT * FROM student order by last_name limit 2 offset 4;

Gertrude Kapllan, [19.10.2023 10:13]
SELECT last_name, start_year  FROM student where CAST(start_year as date)='2023-11-19';

Gertrude Kapllan, [19.10.2023 10:17]
SELECT last_name, start_year  FROM student where DATE_PART('month',start_year)='10';

Gertrude Kapllan, [19.10.2023 09:08]
SELECT * FROM student WHERE age !=17;

Gertrude Kapllan, [19.10.2023 09:09]
SELECT * FROM student WHERE age >17 AND facultet_id=4;

Gertrude Kapllan, [19.10.2023 09:12]
SELECT * FROM student WHERE age >17 AND facultet_id=4 ORDER BY AGE DESC;

Gertrude Kapllan, [19.10.2023 09:19]
SELECT * FROM student WHERE last_name LIKE '%a%';

Gertrude Kapllan, [19.10.2023 09:02]
ALTER TABLE student ADD COLUMN start_year TIMESTAMP;

Gertrude Kapllan, [19.10.2023 09:04]
UPDATE student SET start_year = now();